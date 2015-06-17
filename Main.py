#!/usr/bin/python3
# -*- coding: utf-8 -*-
from functools import total_ordering

__author__ = 'Saylenty'

from math import log2


@total_ordering
class Char:
    def __init__(self, name, freq) -> None:
        self._name = name
        self._freq = freq
        self._code = ""

    def __lt__(self, other):
        return True if self._freq < other.get_freq() else False

    def __eq__(self, other):
        return True if self._name == other.get_name() and self._freq == other.get_freq() else False

    def __str__(self):
        return "{0}\t {1}\t {2}".format(self._name, str(self._freq), self._code)

    def __iter__(self):
        return self

    def get_name(self):
        return self._name

    def get_freq(self):
        return self._freq

    def get_code(self):
        return self._code

    def append_code(self, code):
        self._code += str(code)


def find_middle(lst):
    if len(lst) == 1: return None
    s = k = b = 0
    for p in lst: s += p.get_freq()
    s /= 2
    for p in range(len(lst)):
        k += lst[p].get_freq()
        if k == s: return p
        elif k > s:
            j = len(lst) - 1
            while b < s:
                b += lst[j].get_freq()
                j -= 1
            return p if abs(s - k) < abs(s - b) else j
    return


def shannon_fano(lst):
    middle = find_middle(lst)
    if middle is None: return
    for i in lst[: middle + 1]:
        i.append_code(0)
    shannon_fano(lst[: middle + 1])
    for i in lst[middle + 1:]:
        i.append_code(1)
    shannon_fano(lst[middle + 1:])


def main()->None:
    lst = list()
    m = input('Enter 1 to enter message; 2 - dictionary: ')
    if m == '1':
        m = input("message ---> ")
        s = frozenset(m)
        for c in s: lst.append(Char(c, m.count(c)/len(m)))
    elif m == '2':
        i = 1
        while True:
            m = input("{} --->".format(i))
            if m == "":
                print("end")
                break
            m = m.replace(' ', '')
            lst.append(Char(m[: m.find(':')], float(m[m.find(':') + 1:])))
            i += 1
    else:
        lst.append(Char('a', 0.5))
        lst.append(Char('b', 0.25))
        lst.append(Char('c', 0.098))
        lst.append(Char('d', 0.052))
        lst.append(Char('e', 0.04))
        lst.append(Char('f', 0.03))
        lst.append(Char('g', 0.019))
        lst.append(Char('h', 0.011))

    lst.sort(reverse=True)
    shannon_fano(lst)
    h = l = 0
    for c in lst:
        print(c)
        h += c.get_freq() * log2(c.get_freq())
        l += c.get_freq() * len(c.get_code())
    h = abs(h)
    print("H_max = {}".format(log2(len(lst))))
    print("h = {}".format(h))
    print("l_cp = {}".format(l))
    print("K_c.c. = {}".format(log2(len(lst))/l))
    print("K_o.э. = {}".format(h/l))
    return

if __name__ == "__main__": main()