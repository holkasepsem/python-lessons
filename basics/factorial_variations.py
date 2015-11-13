#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Program s několika variacemi implementace funkce faktorial.

http://www.pythontutor.com/visualize.html#mode=edit
"""

def factorial_iter(n):
	if n == 0:
		return 1

	result = 1
	while n >= 1:
		result = result * n
		n = n - 1

	return result


def factorial_iter_opt(n):
	if n == 0 or n == 1:
		return 1

	result = 1
	while n > 1:
		result = result * n 
		n = n - 1

	return result


def factorial_rec(n):
	if n == 0 or n == 1:
		return 1

	return n * factorial_rec(n - 1)		


if __name__ == "__main__":
	print(factorial_iter(3))
	print(factorial_iter_opt(3))
	print(factorial_rec(3))


