"""Base Classes"""

# Built In
import uuid


class State(object):
    """State object for card handler"""

    def __init__(self, sets=[], blacklisted_sets=[], blacklisted_cards=[]):
        """Hold the state of a session"""
        self.id = uuid.uuid4()
        self.sets = sets
        self.blacklisted_sets = blacklisted_sets
        self.blacklisted_cards = blacklisted_cards
