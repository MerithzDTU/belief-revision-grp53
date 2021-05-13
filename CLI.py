import argparse
from cmd import PROMPT

from sympy import to_cnf, SympifyError

from belief_base import BeliefBase

PROMPT = ">>> "


def print_menu():
    print(
        f"""Actions Available:
    r: Belief revision
    e: Empty belief base
    p: Print belief base
    q: Quit
    """
    )


def run(bb):
    print(bb)
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
    elif menu_input == 'p':
        print(bb)
    elif menu_input == 'q':
        exit()


if __name__ == '__main__':
    #parser = argparse.ArgumentParser(description='Belief base revision CLI tool.')
    #parser.add_argument('--debug', action='store_true', help='enable debugging')
    #args = parser.parse_args()

    bb = BeliefBase()
    while True:
        run(bb)
