"""Existing tests for pricing."""
from src.pricing import calculate_discount


def test_premium_discount():
    assert calculate_discount(100, "premium") == 80


def test_regular_customer():
    assert calculate_discount(100, "regular") == 100