#!/usr/bin/env python3

import pandas as pd

# PART 1
print("PART 1: Building a DataFrame from Atomic Elements\n")
elems = pd.read_csv('elements.csv')
new_rows = pd.DataFrame.from_dict({'name': ['Flourine', 'Neon'], 
                                   'symbol': ['F', 'Ne'],
                                   'atomic number': [9, 10]})
elems = pd.concat([elems, new_rows], ignore_index=True)
atomic_weights = [1, 4, 7, 9, 11, 12, 14, 16, 19, 20]
elems['atomic weights'] = atomic_weights

print(elems)

# PART 2
print("\nPART 2:")
import numpy as np

greek_letters = ['gamma', 'pi', 'beta', 'omega', 'kappa', 'theta', 'chi', 'delta', 'sigma']

arr1 = np.random.normal(10, 1.5, 9)
arr2 = np.random.normal(10, 1.5, 9)

angle = np.linspace(0, 2 * np.pi, 9)

cos_angle = np.cos(angle)

d = {'Letters': greek_letters,
     'Array-1': arr1,
     'Array-2': arr2,
     'Angle': angle,
     'Cosine': cos_angle
    }

df = pd.DataFrame.from_dict(d)

print("\nFull DataFrame:")
print(df)

df.sort_values(by='Letters', inplace=True)
df.drop(columns=['Array-2','Cosine'], inplace=True)
df.drop(index=4, inplace=True)

print("\nDropped two columns and a row:")
print(df)

# PART 3
print("\nPART 3:")
def fibonacci(n):
    if n < 1:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    nums = [1, 1]
    for _ in range(2, n):
        nums.append(nums[-1] + nums[-2])
    return nums

print("\nFirst 12 Fibonacci numbers:")
for x in fibonacci(12):
    print(x, end=' ')
print()

fib12 = fibonacci(12)
ratios = [x/y for x, y in zip(fib12[-5:], fib12[-6:-1])]
print("\nRatios for last 5 numbers:")
print(ratios)

# PART 4
print("\nPART 4:")
def kelvin_to_rankine(temp):
    return temp * 9 / 5

kelvin_temps = [273, 373, 420, 900, 1200]
print("\nKelvin Temps:" + str(kelvin_temps))
print("\nConverting to Rankine using a function:")
for temp in kelvin_temps:
    print(kelvin_to_rankine(temp), end=' ')
print()

print("\nConverting to Rankine using a lambda:")
for temp in kelvin_temps:
    print((lambda x: x * 9 / 5)(temp), end=' ')
print()
