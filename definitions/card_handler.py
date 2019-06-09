""""""

# Built In
import random
from copy import deepcopy

# Local
from definitions import sets, state_def


set_lookup = {"Base Set": sets.base_set,
              "Seaside": sets.seaside}


class CardHandler(object):
    """Do Stuff with cards"""

    def __init__(self, state=None):
        self.state = state_def.State() if state is None else state
        self.load_state(state=self.state)
 
    def concat_sets(self, sets_list):
        """Join card sets into one list, ignore blacklisting"""
        cards = []
        for card_set in sets_list:
            cards += card_set.cards
 
        return cards

    def add_sets(self, *sets_to_add):
        """Add a set to handler"""
        for card_set in sets_to_add:
            self.all_sets.append(deepcopy(set_lookup[card_set]))

    def generate_state(self):
        """Generate state object"""
        state = state_def.State(sets=[card_set.name for card_set in self.all_sets],
                                blacklisted_sets=self.list_blacklisted_sets(),
                                blacklisted_cards=self.list_blacklisted_cards())
        return state

    def load_state(self, state):
        """Read state information for card handler"""
        self.all_sets = []
        self.add_sets(*state.sets)
        
        self.all_cards = self.concat_sets(sets_list=self.all_sets)

        for card_set in state.blacklisted_sets:
            self.blacklist_set(set_name=card_set, blacklist=True)
        for card in state.blacklisted_cards:
            self.blacklist_card(card_name=card, blacklist=True)

    def list_blacklisted_sets(self):
        """Return a list of blacklisted sets"""
        return [card_set.name for card_set in self.all_sets if card_set.blacklisted]

    def list_blacklisted_cards(self):
        """Return a list of blacklisted cards"""
        return [card.name for card in self.all_cards if card.blacklisted]

    def blacklist_set(self, set_name, blacklist):
        """Mark a card set as blacklisted"""
        for card_set in self.all_sets:
            if card_set.name == set_name:
                card_set.blacklisted = blacklist

    def blacklist_card(self, card_name, blacklist):
        """Mark a card as blacklisted"""
        for card in self.all_cards:
            if card.name == card_name:
                card.blacklisted = blacklist

    def print_card_list(self, cards_list):
        """Print names in list alongside the set that they belong too"""
        for card in cards_list:
            print("{} - {}".format(card.name, card.in_set))

    def filter_sets(self):
        """Return filtered sets list with respect to blacklisting"""
        return [card_set for card_set in self.all_sets if not card_set.blacklisted]

    def filter_cards(self, cards_list):
        """Return filtered cards list with respect to blacklisting"""
        return [card for card in cards_list if not card.blacklisted]

    def filter_all(self):
        """Return a filtered cards list with respect blacklisted sets and cards"""
        filtered_sets = self.filter_sets()
        concatednated_sets = self.concat_sets(sets_list=filtered_sets)
        return self.filter_cards(cards_list=concatednated_sets)

    def generate_random_kingdom(self):
        """Generate a random kingdom from cards in handler sets"""
        return random.sample(self.filter_all(), 10)
