f"""
A factory production line is manufacturing bolts using three machines, A, B and C. Of the total output, machine A is responsible for 25%, machine B for 35% and
machine C for the rest. it is known from previous experience with the machines
that 5% of the output from machine A is defective, 4% from machine B and 2%
from machine C. A bolt is chosen at random from the production line and found
to be defective. What is the probability that it came from
(a) machine A (b) machine B (c) machine C?
"""

P = {}
P['A'] = 0.25
P['B'] = 0.35
P['C'] = 1 - P['A'] - P['B']
P['D|A'] = 0.05
P['D|B'] = 0.04
P['D|C'] = 0.02

P['D'] = P['D|A'] * P['A'] + P['D|B'] * P['B'] + P['D|C'] * P['C']

P['A|D'] = P['A'] * P['D|A'] / P['D']
P['B|D'] = P['B'] * P['D|B'] / P['D']
P['C|D'] = P['C'] * P['D|C'] / P['D']

print(f"{P['A|D'] = }\n{P['B|D'] = }\n{P['C|D'] = }")
