'''
These functions of utility have been studied upon from the aima-python code repository, which contains implementations of specific algorithms
from the literature "Articficial Intelligence: A Modern Approach" by Stuart Russell and Peter Norvig.

The MIT License (MIT)
Copyright (c) 2016 aima-python contributors
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-- GITHUB LINK --
https://github.com/aimacode/aima-python
'''
from sympy.logic.boolalg import Or, And


def remove_item(item, seq):
    # Returns a copy of the sequence without the item.
    return [x for x in seq if x != item]


def associate(op, args):
    args = dissociate(op, args)
    if len(args) == 0:
        return op.identity
    elif len(args) == 1:
        return args[0]
    else:
        return op(*args)


def dissociate(op, args):
    result_list = []

    def collect(sub_args):
        for arg in sub_args:
            if isinstance(arg, op):
                collect(arg.args)
            else:
                result_list.append(arg)

    collect(args)
    return result_list


def conjuncts(s):
    return dissociate(And, [s])


def disjuncts(s):
    return dissociate(Or, [s])


def remove_dups(seq):
    '''
    Duplicated elements from the sequence gets removed.
    Sets cannot have duplicate values, therefore we add the sequence to the set and tranforms the set to a list
    '''
    return list(set(seq))
