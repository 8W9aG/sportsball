"""Caching utilities."""

from joblib import Memory  # type: ignore

MEMORY = Memory(".sportsball_cache", verbose=0, compress=True)
