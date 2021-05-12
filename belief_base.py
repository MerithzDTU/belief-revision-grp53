from sympy.logic.boolalg import to_cnf, And, Or, Equivalent

from entailment import pl_resolution
from utilities import associate, dissociate

def check_order(order):
    if 0 <= order <= 1:
        return True
    else:
        return False


def _new_order(belief, order):
    return max[belief.order, order]


class BeliefBase:
    def __init__(self):
        self.beliefs = []

    def _remove_query(self, query, order):
        for belief in self.beliefs:
            if belief.query == query:
                belief.order  = _new_order(belief, order)
                return False
        return True


    def add(self, query, order):
        '''Add belief to belief base'''
        query = to_cnf(query)
        # Er det en rigtig order???
        if check_order(order) is True:
            if self._remove_query(query , order) is True:
                self.beliefs.append(Belief(query,order))


    def expand(self, query, order):
        query_in_cnf = to_cnf(query)
        check_order(order)
        self.add(query, order)


    def contract():


    def revise():


    def clear(self):
        self.beliefs.clear()


class Belief: # [a, b, a & b, a->c]
    def __init__(self, query, order):
        self.query = query
        self.order = order