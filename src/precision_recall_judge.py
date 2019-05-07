import csv
f = open('output_final_no_appeal.csv')
csv_f = csv.reader(f)
false_p = 0
false_n = 0
true_p = 0

for row in csv_f:
	if row[0] == 'hit_id':
		continue
	if row[1] == 'UNFAIR' and row[2] == 'UNFAIR':
		true_p = true_p + 1
	elif row[1] == 'FAIR' and row[2] == 'UNFAIR':
		false_p = false_p + 1
	elif row[1] == 'UNFAIR' and row[2] == 'FAIR':
		false_n = false_n + 1

recall = true_p/(true_p + false_n)
precision = true_p/(true_p + false_p)
f = 2 * ((precision * recall)/(precision + recall))

print('F_1 SCORE:')
print(f)
print('RECALL SCORE:')
print(recall)
print('PRECISION SCORE:')
print(precision)
