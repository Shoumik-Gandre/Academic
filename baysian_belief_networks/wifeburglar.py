from pprint import pprint

f"""
P - parent - P1, P2
C - child - C1, C2, C3


      [ W ]        [ B ]
     /      \      /      \
[ C ]       [ O ]        [ D ]
"""

P = {}
P['W'] = 0.05
P['-W'] = 1 - P['W']
P['B'] = 0.001
P['-B'] = 1 - P['B']

P['O|W^B'] = 0.01
P['O|-W^B'] = 0.25
P['O|W^-B'] = 0.05
P['O|-W^-B'] = 0.75

P['C|W'] = 0.95
P['C|-W'] = 0.95
P['D|B'] = 0.5
P['D|-B'] = 0.001
P['-D|-B'] = 1 - P['D|-B']

P['C'] = P['C|W'] * P['W'] + P['C|-W'] * P['-W']

P['D'] = P['D|B'] * P['B'] + P['D|-B'] * P['-B']

# P['find'] = P['O|W^-B'] * P['C'] * P['D']
P['O^W^-B^C^-D'] = P['O|W^-B'] * P['C|W'] * P['-D|-B'] * P['W'] * P['-B']

print(f"{P['O^W^-B^C^-D'] = }")
pprint(P)