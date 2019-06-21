# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here

df = pd.read_csv(path)

fico = df['fico']

fico_700 = df[fico>700]

p_a = len(fico_700)/len(fico)

df1 =df[df['purpose']=='debt_consolidation']

p_b = len(df1)/len(fico)

join = df[(df['purpose']=='debt_consolidation') & (fico>700)]



p_a_b = len(join)/len(fico_700)


print(p_a_b)

if p_a_b == p_a : 
    result = True

else:
    result = False

 
# code ends here


# --------------
# code starts here
prob_lp =len(df[df['paid.back.loan']== 'Yes'])/len(fico)

prob_cs =len(df[df['credit.policy']== 'Yes'])/len(fico)

new_df = df[df['paid.back.loan']== 'Yes']

prob_pd_cs = len(new_df[new_df['credit.policy']=='Yes'])/len(new_df)

bayes = prob_pd_cs*prob_lp/prob_cs

print(bayes)

# code ends here


# --------------
# code starts here
df1 = df[df['paid.back.loan']=='No']



res = df1.groupby(['paid.back.loan']).size()
print(res)
# Label X-axes and Y-axes

res.plot(kind='bar', stacked=False, figsize=(15,10))

# code ends here


# --------------
# code starts here
inst_median = df['installment'].median()

inst_mean = df['installment'].mean()

df['installment'].hist()
df['log.annual.inc'].hist()


# code ends here


