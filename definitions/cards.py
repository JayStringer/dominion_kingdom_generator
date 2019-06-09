"""Dominion Cards"""


class Card(object):
    """Base Class for Dominion Card"""

    def __init__(self, name, cost, card_type, in_set, image=None):
        """Define a Dominion Card"""
        self.name = name
        self.cost = cost
        self.in_set = in_set
        self.image = image
        self.blacklisted = False

##############################################################################
# Base Set
##############################################################################

cellar = Card(name="Cellar", cost=2, card_type="Action", in_set="Base Set")
chapel = Card(name="Chapel", cost=2, card_type="Action", in_set="Base Set")
moat = Card(name="Moat", cost=2, card_type="Action/Reaction", in_set="Base Set")
harbinger = Card(name="Harbinger", cost=3, card_type="Action", in_set="Base Set")
merchant = Card(name="Merchant", cost=3, card_type="Action", in_set="Base Set")
vassal = Card(name="Vassal", cost=3, card_type="Action", in_set="Base Set")
village = Card(name="Village", cost=3, card_type="Action", in_set="Base Set")
workshop = Card(name="Workshop", cost=3, card_type="Action", in_set="Base Set")
bureaucrat = Card(name="Bureaucrat", cost=4, card_type="Action/Attack", in_set="Base Set")
gardens = Card(name="Gardens", cost=4, card_type="Victory", in_set="Base Set")
militia = Card(name="Militia", cost=4, card_type="Action/Attack", in_set="Base Set")
moneylender = Card(name="Moneylender", cost=4, card_type="Action", in_set="Base Set")
poacher = Card(name="Poacher", cost=4, card_type="Action", in_set="Base Set")
remodel = Card(name="Remodel", cost=4, card_type="Action", in_set="Base Set")
smithy = Card(name="Smithy", cost=4, card_type="Action", in_set="Base Set")
throne_room = Card(name="Throne Room", cost=4, card_type="Action", in_set="Base Set")
bandit = Card(name="Bandit", cost=5, card_type="Action/Attack", in_set="Base Set")
council_room = Card(name="Council Room", cost=5, card_type="Action", in_set="Base Set")
festival = Card(name="Festival", cost=5, card_type="Action", in_set="Base Set")
laboratory = Card(name="Laboratory", cost=5, card_type="Action", in_set="Base Set")
library = Card(name="Library", cost=5, card_type="Action", in_set="Base Set")
market = Card(name="Market", cost=5, card_type="Action", in_set="Base Set")
mine = Card(name="Mine", cost=5, card_type="Action", in_set="Base Set")
sentry = Card(name="Sentry", cost=5, card_type="Action", in_set="Base Set")
witch = Card(name="Witch", cost=5, card_type="Action/Attack", in_set="Base Set")
artisan = Card(name="Artisan", cost=6, card_type="Action", in_set="Base Set")

##############################################################################
# Seaside
##############################################################################

embargo = Card(name="Embargo", cost=2, card_type="Action", in_set="Seaside")
haven = Card(name="Haven", cost=2, card_type="Action/Duration", in_set="Seaside")
lighthouse = Card(name="Lighthouse", cost=2, card_type="Action/Duration", in_set="Seaside")
native_village = Card(name="Native Village", cost=2, card_type="Action", in_set="Seaside")
pearl_diver = Card(name="Pearl Diver", cost=2, card_type="Action", in_set="Seaside")
ambassador = Card(name="Ambassador", cost=3, card_type="Action/Attack", in_set="Seaside")
fishing_village = Card(name="Fishing Village", cost=3, card_type="Action/Duration", in_set="Seaside")
lookout = Card(name="Lookout", cost=3, card_type="Action/Duration", in_set="Seaside")
smugglers = Card(name="Smugglers", cost=3, card_type="Action", in_set="Seaside")
warehouse = Card(name="Warehouse", cost=3, card_type="Action", in_set="Seaside")
caravan = Card(name="Caravan", cost=4, card_type="Action/Duration", in_set="Seaside")
cutpurse = Card(name="Cutpurse", cost=4, card_type="Action/Attack", in_set="Seaside")
island = Card(name="Island", cost=4, card_type="Action/Victory", in_set="Seaside")
navigator = Card(name="Navigator", cost=4, card_type="Action", in_set="Seaside")
pirate_ship = Card(name="Pirate Ship", cost=4, card_type="Action/Attack", in_set="Seaside")
salvager = Card(name="Salvager", cost=4, card_type="Action", in_set="Seaside")
sea_hag = Card(name="Sea Hag", cost=4, card_type="Action/Attack", in_set="Seaside")
treasure_map = Card(name="Treasure Map", cost=4, card_type="Action", in_set="Seaside")
bazaar = Card(name="Bazaar", cost=5, card_type="Action", in_set="Seaside")
explorer = Card(name="Explorer", cost=5, card_type="Action", in_set="Seaside")
ghost_shop = Card(name="Ghost Ship", cost=5, card_type="Action/Attack", in_set="Seaside")
merchant_ship = Card(name="Merchant Ship", cost=5, card_type="Action/Duration", in_set="Seaside")
outpost = Card(name="Outpost", cost=5, card_type="Action/Duration", in_set="Seaside")
tactician = Card(name="Tactician", cost=5, card_type="Action", in_set="Seaside")
treasury = Card(name="Treasury", cost=5, card_type="Action", in_set="Seaside")
wharf = Card(name="Wharf", cost=5, card_type="Action/Duration", in_set="Seaside")
