f"""
Assume your house has an alarm system against burglary. 
You live in the seismically active area and the alarm system can get occasionally set off by an earthquake. 
You have two neighbors, Mary and John, who do not know each other. If they hear the alarm they call you, 
but this is not guaranteed. 
We want to represent the probability distribution of events: 
Burglary (B), Earthquake (E), Alarm (A), Mary calls (M) and John calls (J)
"""

f"""
Graph:
[ E ]      [ B ]
     \\   //
       [ A ]
    //      \\
[ J ]       [ M ]
"""


P = {}

# Burglar
P['B'] = 0.001
P['-B'] = 0.999
#Earthquake
P['E'] = 0.002
P['-E'] = 0.998

# J calls given Alarm rings
P['J|A'] = 0.9
# J does not call given Alarm rings
P['-J|A'] = 0.1
# J calls given Alarm does not ring
P['J|-A'] = 0.05
# J does not call given does not Alarm rings
P['-J|-A'] = 0.95

P['M|A'] = 0.9
P['-M|A'] = 0.1
P['M|-A'] = 0.05
P['-M|-A'] = 0.95

P['A|B^E'] = 0.95
P['A|B^-E'] = 0.94
P['A|-B^E'] = 0.29
P['A|-B^-E'] = 0.001
P['-A|B^E'] = 0.05
P['-A|B^-E'] = 0.06
P['-A|-B^E'] = 0.71
P['-A|-B^-E'] = 0.999

P['B^E'] = P['B'] * P['E']
P['B^-E'] = P['B'] * P['-E']
P['-B^E'] = P['-B'] * P['E']
P['-B^-E'] = P['-B'] * P['-E']

P['A'] = \
    P['A|B^E'] * P['B^E'] \
    + P['A|-B^E'] * P['-B^E'] \
    + P['A|B^-E'] * P['B^-E'] \
    + P['A|-B^-E'] * P['-B^-E']

P['-A'] = \
    P['-A|B^E'] * P['B^E'] \
    + P['-A|-B^E'] * P['-B^E'] \
    + P['-A|B^-E'] * P['B^-E'] \
    + P['-A|-B^-E'] * P['-B^-E']

P['A|B'] = 0.94
P['-A|B'] = 0.06


P['J|B'] = P['J|A'] * P['A|B'] + P['J|-A'] * P['-A|B']

Big = \
f"""
{P['J|B'] = }
{P['J|A'] = }
{P['J|-A'] = }
{P['A|B'] = }
{P['-A|B'] = }
"""

print(Big)
