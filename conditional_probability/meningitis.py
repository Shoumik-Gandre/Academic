f"""
Suppose a doctor knows that a meningitis causes a stiff neck in 50% of cases
She also knows that the probability in the general population of someone having a stiff neck at any time is 1/20
She also has to know the incidence of meningitis in the population (1/50,000)
calculate the probability the patient has meningitis given she/he has stiff neck
"""

f"""
# Note: 
# meningitis = M
# Stiff neck = S
"""

P = {}

f"""
Suppose a doctor knows that a meningitis causes a stiff neck in 50% of cases
This means: probability of a stiff neck given the person already has meningitis
"""
P['S|M'] = 0.5

f"""
She also knows that the probability in the general population of someone having a stiff neck at any time is 1/20
This means: probability of stiffneck is 1/20
"""
P['S'] = 1/20

f"""
She also has to know the incidence of meningitis in the population (1/50,000)
This means: probability of meningitis is 1/50,000
"""
P['M'] = 1/50000

P['M|S'] = P['S|M'] * P['M'] / P['S']

print(f"{P['M|S'] = }")