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


def visualize(no_appeal,w_appeal):		# Code to make a multi-series bar graph found at https://pythonspot.com/matplotlib-bar-chart/
	fig, ax = plt.subplots()
	index = np.arange(len(no_appeal))
	bar_width = 0.35
	opacity = 0.8

	rects1 = plt.bar(index, no_appeal, bar_width, alpha=opacity, color='r',label="No Appeal")
	rects2 = plt.bar(index + bar_width, w_appeal, bar_width, alpha=opacity, color='b', label="With Appeal")

	plt.xlabel('Analysis')
	plt.ylabel('Scores')
	plt.title("Scores by HIT Type")
	plt.xticks(index + bar_width / 2, ('Recall', 'Precision', 'F'))
	plt.legend()

	plt.tight_layout()
	plt.show()


def main():			# Calls functions to calculate scores and create graph

	recall_no_appeal,precision_no_appeal,f_no_appeal = results_for_csv('agg_output_final_no_appeal.csv')
	recall_w_appeal,precision_w_appeal,f_w_appeal = results_for_csv('agg_output_final_w_appeal.csv')

	results_no_appeal = (recall_no_appeal,precision_no_appeal,f_no_appeal)
	results_w_appeal = (recall_w_appeal,precision_w_appeal,f_w_appeal)

	visualize(results_no_appeal,results_w_appeal)


if __name__=='__main__':
	main()

