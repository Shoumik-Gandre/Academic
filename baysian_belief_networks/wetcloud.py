from pprint import pprint

P = {}

P['W'] = 0.001
P['C'] = 0.002
P['-W'] = 1 - P['W']
P['-C'] = 1 - P['C']
P['R|W^C'] = 0.95
P['R|-W^C'] = 0.29
P['R|W^-C'] = 0.95
P['R|-W^-C'] = 0.06

P['R'] = \
    P['R|W^C'] * P['W'] * P['C'] + \
    P['R|-W^C'] * P['-W'] * P['C'] + \
    P['R|W^-C'] * P['W'] * P['-C'] + \
    P['R|-W^-C'] * P['-W'] * P['-C']

P['-R'] = 1 - P['R']

P['WG|R'] = 0.95
P['WG|-R'] = 0.05

P['WG'] = P['WG|R'] * P['R'] + P['WG|-R'] * P['-R']

print(f"{P['WG'] = }")
pprint(P)