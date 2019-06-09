"""Dominion Card Sets"""

from definitions import cards


class CardSet(object):
    """Base Class for a Dominion card set"""

    def __init__(self, name):
        """Dominion Card Set"""
        self.name = name
        self.cards = []
        self.blacklisted = False

##############################################################################
# Base Set
##############################################################################

base_set = CardSet(name="Base Set")
base_set.cards = [cards.cellar,
                  cards.chapel,
                  cards.moat,
                  cards.harbinger,
                  cards.merchant,
                  cards.vassal,
                  cards.village,
                  cards.workshop,
                  cards.bureaucrat,
                  cards.gardens,
                  cards.militia,
                  cards.moneylender,
                  cards.poacher,
                  cards.remodel,
                  cards.smithy,
                  cards.throne_room,
                  cards.bandit,
                  cards.council_room,
                  cards.festival,
                  cards.laboratory,
                  cards.library,
                  cards.market,
                  cards.mine,
                  cards.sentry,
                  cards.witch,
                  cards.artisan]

##############################################################################
# Seaside
##############################################################################

seaside = CardSet(name="Seaside")
seaside.cards = [cards.embargo,
                 cards.haven,
                 cards.lighthouse,
                 cards.native_village,
                 cards.pearl_diver,
                 cards.ambassador,
                 cards.fishing_village,
                 cards.lookout,
                 cards.smugglers,
                 cards.warehouse,
                 cards.caravan,
                 cards.cutpurse,
                 cards.island,
                 cards.navigator,
                 cards.pirate_ship,
                 cards.salvager,
                 cards.sea_hag,
                 cards.treasure_map,
                 cards.bazaar,
                 cards.explorer,
                 cards.ghost_shop,
                 cards.merchant_ship,
                 cards.outpost,
                 cards.tactician,
                 cards.treasury,
                 cards.wharf]
