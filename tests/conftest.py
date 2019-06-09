from dominion.class_defs import CardSet
import pytest


@pytest.fixture(name="card_set")
def generate_set():
    """Generate a set for testing with"""
    return CardSet(name="Test Set")
