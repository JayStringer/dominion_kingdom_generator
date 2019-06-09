"""Main file for Dominion Kingdom Builder"""

from definitions.card_handler import CardHandler
from definitions.state_def import State


state = State(sets=["Base Set", "Seaside"],
              blacklisted_sets=[],
              blacklisted_cards=[])

handler = CardHandler(state=state)
# handler.load_state(state=state)
# handler.add_sets("Base Set", "Seaside")
kingdom = handler.generate_random_kingdom()
handler.print_card_list(cards_list=kingdom)
# handler.print_card_list(cards_list=handler.all_cards)
# print(handler.all_sets)