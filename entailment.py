'''
ET ELLER ANDET OMKRING VI HAR BRUGT
AIMA-Python bibliotek, MIT LICENSE bla bla bla
https://github.com/aimacode/aima-python/blob/master/logic.py

The MIT License (MIT)
Copyright (c) 2016 aima-python contributors
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-- GITHUB LINK --
https://github.com/aimacode/aima-python
'''

from sympy.logic.boolalg import to_cnf, Or

'''
Import the functions from the utilities file
'''
from utilities import conjuncts, disjuncts, dissociate, associate, remove_item, remove_dups


def pl_resolution(bb, sentence):
    '''
    From Figure 7.12
    Propositional-logic resolution
    Returns true if the sentence follows from BeliefBase
    Returns false if not
    '''
    clauses = []
    new = set()
    sentence = to_cnf(sentence)

    '''
    Splits the base into conjuncts and adds the contradiction to start resolution
    '''
    for f in bb:
        clauses += conjuncts(f)

    clauses += conjuncts(to_cnf(~sentence))

    while True:
        n = len(clauses)
        pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i + 1, n)]

        for ci, cj in pairs:
            resolvents = pl_resolve(ci, cj)
            if False in resolvents:
                return True
            new = new.union(set(resolvents))

        if new.issubset(set(clauses)):
            return False
        for c in new:
            if c not in clauses:
                clauses.append(c)


def pl_resolve(ci, cj):
    clauses = []
    dci = disjuncts(ci)
    dcj = disjuncts(cj)

    for di in dci:
        for dj in dcj:
            '''
            If the elements di and dj are complementary
            Then
              - create a list of all disjuncts not including di and dj (remove_item)
              - remove all duplicates (remove_dups)
              - join the list into a new clause (associate)
            '''
            if di == ~dj or dj == ~di:
                reso = remove_item(di, dci) + remove_item(dj, dcj)
                reso = remove_dups(reso)
                new_clause = associate(Or, reso)
                clauses.append(new_clause)
    return clauses
