
import pandas as pd


def majority_vote(mturk_res):
    lst = []
    hits = {}


    for index, row in mturk_res.iterrows():
        if index == 0:
            continue;
        assignment = row['HITId']

        correct = True
        if row['Input.aneg_qual_ctrl'] != "No":
            correct = False
        if row['Input.apos_qual_ctrl_1'] != "Yes":
            correct = False
        if row['Input.apos_qual_ctrl_2'] != "Yes":
            correct = False
        if row['Input.apos_qual_ctrl_3'] != "Yes":
            correct = False
        if row['Input.apos_qual_ctrl_4'] != "Yes":
            correct = False
        if row['Input.apos_qual_ctrl_5'] != "Yes":
            correct = False

        true_label = ""
        if correct:
            true_label = "UNFAIR"
        else:
            true_label = "FAIR"


        label = row['Answer.ruling.label']
        short_label = ""
        if label == "Yes, the task should have been rejected":
            short_label = "FAIR"
        else:
            short_label = "UNFAIR"

        # key in form of (assignment, true_label): (num_fair, num_unfair)
        key = (assignment, true_label)

        if key in hits:
            if short_label == "FAIR":
                val = hits[key]
                hits[key] = (val[0] + 1, val[1])
            else:
                val = hits[key]
                hits[key] = (val[0], val[1] + 1)
        else:
            if short_label == "FAIR":
                hits[key] = (1, 0)
            else:
                hits[key] = (0, 1)

    for key, val in hits.items():
        if val[0] > val[1]:
            tup = (key[0], key[1], "FAIR")
            lst.append(tup)
        else:
            tup = (key[0], key[1], "UNFAIR")
            lst.append(tup)

    lst.sort(
        key=lambda l: (l[0])
    )
    return lst

# Main function

def main():
    # Call above functions and output required CSV files
    mturk_res = pd.read_csv('Batch_235466_batch_results.csv')

    votes = majority_vote(mturk_res)
    df1 = pd.DataFrame(votes,columns =['hit_id', 'true_label', 'label'])
    df1.to_csv('agg_output.csv', index=False)

if __name__ == '__main__':
    main()
