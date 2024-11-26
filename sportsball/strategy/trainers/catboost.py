"""The catboost class for a trainer."""

import json
import os
from typing import Any

import optuna
import pandas as pd
import torch
from catboost import CatBoostClassifier, Pool  # type: ignore
from sklearn.model_selection import train_test_split  # type: ignore

from ..weights import WEIGHTS, CombinedWeight
from .output_column import OUTPUT_COLUMN, output_prob_column
from .trainer import HASH_USR_ATTR, Trainer

_MODEL_FILENAME = "model.cbm"
_USR_ATTR_FILENAME = "usr_attr.json"


class CatboostTrainer(Trainer):
    """The catboost trainer class."""

    # pylint: disable=too-many-instance-attributes

    def __init__(
        self,
        folder: str,
        categorical_features: list[str],
        text_features: list[str],
        trial: optuna.trial.Trial | optuna.trial.FrozenTrial | None = None,
    ) -> None:
        super().__init__(folder)
        self._categorical_features = categorical_features
        self._text_features = text_features
        if trial is None:
            self._features_ratio = 0.0
            self._steps = 0
            self._model = CatBoostClassifier(
                task_type=None if not torch.cuda.is_available() else "GPU",
                devices=None if not torch.cuda.is_available() else "0",
            )
        else:
            self._features_ratio = trial.suggest_float("features_ratio", 0.1, 0.9)
            self._steps = trial.suggest_int("steps", 1, 10)
            self._test_size = trial.suggest_float("test_size", 0.0, 0.5)
            self._weight = CombinedWeight(
                trial.suggest_categorical("weight", list(WEIGHTS.keys()))
            )
            self._usr_attrs = trial.user_attrs
            self._model = CatBoostClassifier(
                iterations=trial.suggest_int("iterations", 100, 10000),
                learning_rate=trial.suggest_float("learning_rate", 0.01, 0.3),
                depth=trial.suggest_int("depth", 3, 10),
                l2_leaf_reg=trial.suggest_float("l2_leaf_reg", 1.5, 4.5),
                early_stopping_rounds=100,
                task_type=None if not torch.cuda.is_available() else "GPU",
                devices=None if not torch.cuda.is_available() else "0",
            )

    @property
    def clf(self) -> Any:
        """The underlying classifier"""
        return self._model

    @property
    def salt(self) -> str:
        """The salt to use when hashing the predictions."""
        return "catboost-" + self._usr_attrs[HASH_USR_ATTR]

    def fit(self, x: pd.DataFrame, y: pd.DataFrame):
        """Fit the data."""
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=self._test_size, random_state=42
        )
        train_pool = self._create_pool(x_train, y_train)  # type: ignore
        eval_pool = self._create_pool(x_test, y_test)  # type: ignore
        self._model.fit(train_pool, eval_set=eval_pool, early_stopping_rounds=100)

    def save(self):
        """Save the trainer."""
        self._model.save_model(os.path.join(self._folder, _MODEL_FILENAME))
        with open(
            os.path.join(self._folder, _USR_ATTR_FILENAME), "w", encoding="utf8"
        ) as handle:
            json.dump(self._usr_attrs, handle)

    def load(self):
        """Load the trainer."""
        self._model.load_model(os.path.join(self._folder, _MODEL_FILENAME))
        with open(
            os.path.join(self._folder, _USR_ATTR_FILENAME), encoding="utf8"
        ) as handle:
            self._usr_attrs = json.load(handle)

    def predict(self, x: pd.DataFrame) -> pd.DataFrame | None:
        """Predict the Y values."""
        y = super().predict(x)
        if y is not None:
            return y
        train_pool = self._create_pool(x, None)
        y = pd.DataFrame(
            index=x.index, data={OUTPUT_COLUMN: self._model.predict(train_pool)}
        )
        self.save_prediction(x, y)
        return y

    def predict_proba(self, x: pd.DataFrame) -> pd.DataFrame | None:
        """Predict the Y probabilities."""
        y = super().predict_proba(x)
        if y is not None:
            return y
        pool = self._create_pool(x, None)
        proba = self._model.predict_proba(pool)
        y = pd.DataFrame(
            index=x.index,
            data={output_prob_column(i): proba[:, i] for i in range(proba.shape[1])},
        )
        self.save_prediction_proba(x, y)
        return y

    def select_features(self, x: pd.DataFrame, y: pd.DataFrame) -> list[str]:
        """Select the features from the training data."""
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=self._test_size, random_state=42
        )
        train_pool = self._create_pool(x_train, y_train)  # type: ignore
        eval_pool = self._create_pool(x_test, y_test)  # type: ignore
        summary = self._model.select_features(
            train_pool,
            num_features_to_select=int(self._features_ratio * len(x.columns.values)),
            steps=self._steps,
            train_final_model=True,
            features_for_select=x.columns.values,
            eval_set=eval_pool,
        )
        return summary["selected_features_names"]

    def _create_pool(self, x: pd.DataFrame, y: pd.DataFrame | None) -> Pool:
        text_features = list(set(x.columns.values) & set(self._text_features))
        x[text_features] = x[text_features].fillna("").astype(str)
        cat_features = list(set(x.columns.values) & set(self._categorical_features))
        x[cat_features] = x[cat_features].fillna(0).astype(int)
        weight = None
        if y is not None:
            weight = self._weight.process(y)
        return Pool(
            x,
            label=y,
            cat_features=cat_features,
            text_features=text_features,
            weight=weight,
        )
