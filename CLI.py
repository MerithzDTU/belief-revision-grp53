import argparse
from cmd import PROMPT

from sympy import to_cnf, SympifyError

from belief_base import BeliefBase

PROMPT = ">>> "


def print_menu():
    print(
        """Menu Options:
r: Belief revision
e: Empty belief base
q: Quit Program
    """
    )


def run(bb):
    print('Curent BeliefBase:')
    print('------------------')
    print(bb)
    print('------------------')
    print_menu()
    menu_input = input(PROMPT).lower()

    if menu_input == 'r':
        print('Enter Query:')
        revision_input = input(PROMPT)
        try:
            revision_input = to_cnf(revision_input)
            print('Enter Order:')
            order = input(PROMPT)
            bb.revise(revision_input, float(order))
        except SympifyError:
            print('Invalid formula')
        except ValueError:
            print('Order has to be a real number from 0 to 1')
        print()

    elif menu_input == 'e':
        bb.clear()
    elif menu_input == 'q':
        exit()


if __name__ == '__main__':
    bb = BeliefBase()
    while True:
        run(bb)
