#!/bin/python

import math
import os
import random
import re
import sys


from collections import Counter
class Multiset(object):

    def __init__(self):
        self.elements = Counter()
    def add(self, val):
        # adds one occurrence of val from the multiset, if any
        self.elements[val] += 1

    def remove(self, val):
        # removes one occurrence of val from the multiset, if any
        if self.elements[val] >0 :
            self.elements[val] -= 1
            if self.elements[val] ==0:
                del self.elements[val]
    
    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return val in self.elements
    
    def __len__(self):
        # returns the number of elements in the multiset
        return sum(self.elements.values())
        
if __name__ == '__main__':
    def performOperations(operations):
        m = Multiset()
        result = []
        for op_str in operations:
            elems = op_str.split()
            if elems[0] == 'size':
                result.append(len(m))
            else:
                op, val = elems[0], int(elems[1])
                if op == 'query':
                    result.append(val in m)
                elif op == 'add':
                    m.add(val)
                elif op == 'remove':
                    m.remove(val)
        return result

    q = int(raw_input())
    operations = []
    for _ in xrange(q):
        operations.append(raw_input())

    result = performOperations(operations)
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()