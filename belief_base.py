from math import isclose
from sympy.logic.boolalg import to_cnf, And, Or, Equivalent
from entailment import pl_resolution
from utilities import associate, dissociate


def check_order(order):
    if 0 <= order <= 1:
        return True
    else:
        return False


def _new_order(belief, order):
    if belief.order > order:
        return belief.order
    else:
        return order


class BeliefBase:

    def __init__(self):
        self.beliefs = []

    def _update_duplicates(self, query, order):
        for belief in self.beliefs:
            if belief.query == query:
                belief.order = _new_order(belief, order)
                return True
        return False

    def add(self, query, order):
        '''
        Add belief to belief base
        '''

        query = to_cnf(query)
        # Converts query to CNF form

        if check_order(order) is True:
            # is the order correct, if yes we proceed
            if self._update_duplicates(query, order) is False:
                # checks for duplicates, if found changes the order to the highest one of the two
                self.beliefs.append(Belief(query, order))
                # if no duplicates found it simply adds to the beliefs list

    def expand(self, query, order, add=True):
        new_query = to_cnf(query)
        # Converts query to CNF form
        check_order(order)
        # is the order correct

        if not pl_resolution([], ~new_query):
            # Does query contradict itself
            if pl_resolution([], new_query):
                # Is query a tautologi
                order = 1
            else:  # It is not a tautologi, we now need to check for other possible changes in order
                for belief in self.beliefs:
                    if belief.order > order:
                        # The current order is more plauseble and the new one, we dont change it.
                        continue

                    deg = self.degree(new_query >> belief.query)
                    if pl_resolution([], Equivalent(new_query, belief.query)) or belief.order <= order < deg:
                        '''
                        if query and belief.query entails each other (biconditional) or given order is as follows: 
                        belief.order <= order < deg
                        '''
                        self._temp_order_list.append((belief, order))
                        # add the belief with the original order, to the temp list
                    else:
                        self._temp_order_list.append((belief, deg))
                        # add the belief with the degree order, to the temp list
                self._push_temp_list()

            if add:
                self.add(new_query, order)

    def contract(self, query, order):
        new_query = to_cnf(query)  # Converts query to CNF form
        check_order(order)  # is the order correct

        for belief in self.beliefs:  # Lowers order if new_query and new_query|old_query have same degree
            if belief.order > order:
                deg = self.degree(new_query)
                new_or_old = associate(Or, [new_query, belief.query])  # create a new belief
                # with the new_query and the current query in our list, with or between.
                deg_NorO = self.degree(new_or_old)
                if deg == deg_NorO and (belief.query_str in str(query) or str(query) in belief.query_str):
                    self._temp_order_list.append((belief, order))
        self._push_temp_list()

    def revise(self, query, order, add=True):
        new_query = to_cnf(query)  # Converts query to CNF form
        check_order(order)  # is the order correct
        deg = self.degree(new_query)

        if not pl_resolution([], ~new_query):
            # Does query contradict itself
            if pl_resolution([], new_query):
                # Is query a tautologi
                order = 1
            elif order <= deg:
                self.contract(new_query, order)
            else:
                self.contract(~new_query, 0)
                self.expand(new_query, order, False)

            if add:
                self.add(new_query, order)

    def clear(self):
        self.beliefs.clear()

    def degree(self, query):

        if pl_resolution([], query):  # is query a tautologi
            return 1

        base = []
        for order, row in self.sort_beliefs():
            base += [b.query for b in row]
            if pl_resolution(base, query):
                return order
        return 0

    def sort_beliefs(self):

        result = []
        last_order = None

        for belief in self.beliefs:
            if last_order is None:  # first run of method
                result.append(belief)
                last_order = belief.order
                continue

            if isclose(belief.order,
                       last_order):  # If the orders are equal/close then will belief be put into the same row
                result.append(belief)

            else:
                yield last_order, result
                result = [belief]
                last_order = belief.order

        yield last_order, result

    def _push_temp_list(self):
        for belief, order in self._temp_order_list:
            self.beliefs.remove(belief)
            if order > 0:
                belief.order = order
                self.beliefs.append(belief)

        self._temp_order_list = []

    def print_beliefs(self):
        for belief in self.beliefs:
            print(belief.query, belief.order)

    def __repr__(self):
        if len(self.beliefs) == 0:
            return 'empty'
        return '\n'.join(str(x) for x in self.beliefs)


class Belief:  # [a, b, a & b, a->c]
    def __init__(self, query, order):
        self.query = query
        self.order = order
        self.query_str = str(query)

    def __repr__(self):
        return f'Belief({self.query}, order={self.order})'
