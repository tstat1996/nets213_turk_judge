import pandas as pd

appeals = pd.read_csv("sandbox_reasons.csv")
no_appeals = pd.read_csv("sandbox_no_reasons.csv")

first = appeals['WorkerId']
second = no_appeals['WorkerId']
comb = first.append(second)
print(len(comb.unique()))