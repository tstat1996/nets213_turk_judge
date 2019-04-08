
import pandas as pd


def majority_vote(mturk_res):
    lst = []
    hits = {}


    for index, row in mturk_res.iterrows():
        if index == 0:
            continue;
        assignment = row['AssignmentId']
        reward = row['Reward']
        validity = row['Input.true_label']
        label = row['Answer.image-rejections.label']
        short_label = ""
        if label == "The Turker should have been rejected.":
            short_label = "FAIR"
        else:
            short_label = "UNFAIR"

        short_true = ""
        if validity == "valid":
            short_true = "UNFAIR"
        elif validity == "invalid":
            short_true = "FAIR"
        else:
            short_true = "NA"

        # key in form of (assignment, short_true, reward): (num_fair, num_unfair)
        key = (assignment, short_true, reward)

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
            tup = (key[2], key[1], "FAIR")
            lst.append(tup)
        else:
            tup = (key[2], key[1], "UNFAIR")
            lst.append(tup)

    lst.sort(
        key=lambda l: (l[0], l[1])
    )
    return lst

# Main function

def main():
    # Call above functions and output required CSV files
    mturk_res = pd.read_csv('sample_output.csv')

    votes = majority_vote(mturk_res)
    df1 = pd.DataFrame(votes,columns =['attr_id', 'adj', 'label'])
    df1.to_csv('agg_output.csv', index=False)

if __name__ == '__main__':
    main()
