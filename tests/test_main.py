"""Tests"""

import pytest


@pytest.mark.parametrize("attribute", ["name", "cards"])
def test_card_set_has_attribute(attribute, card_set):
    """Card set has name attribute"""
    assert hasattr(card_set, attribute)


def test_card_set_cards_is_list(card_set):
    """Cards list in set is type list"""
    assert isinstance(card_set.cards, list)
