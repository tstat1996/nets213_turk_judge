
import pandas as pd


def majority_vote(mturk_res):
    lst = []
    hits = {}


    for index, row in mturk_res.iterrows():
        if index == 0:
            continue;
        assignment = row['AssignmentId']
        reward = row['Reward']
        validity = row['true_label']
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
                pass
        else:
            pass




    lst = []
    labels = {}

    adj_descr = ['Input.adj_1', 'Input.adj_2', 'Input.adj_3', 'Input.adj_4', 'Input.adj_5', 'Input.adj_6',
                 'Input.adj_7', 'Input.adj_8', 'Input.adj_9', 'Input.adj_10']
    adj_label = ['Answer.adj_1', 'Answer.adj_2', 'Answer.adj_3', 'Answer.adj_4', 'Answer.adj_5',
                 'Answer.adj_6', 'Answer.adj_7', 'Answer.adj_8', 'Answer.adj_9', 'Answer.adj_10']

    for index, row in mturk_res.iterrows():
        if index == 0:
            continue;
        attr_id = row['Input.attr_name']
        # for each adjective per row, increment its count in labels dictionary
        # if worker voted yes
        for i in range(10):
            adj = row[adj_descr[i]]
            label = row[adj_label[i]]
            key = (attr_id, adj)
            if key in labels:
                if label == 'Yes':
                    labels[key] = labels[key] + 1
            else:
                if label == 'Yes':
                    labels[key] = 1
                else:
                    labels[key] = 0

    # now I want to create list with majority votes
    for (x, y) in labels:
        if labels[(x, y)] >= 2:
            tup = (x, y, 'TRUE')
            lst.append(tup)
        else:
            tup = (x, y, 'FALSE')
            lst.append(tup)

            # sort list by alphabetical order by first column, then second column
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
    df1.to_csv('output1.csv', index=False)

if __name__ == '__main__':
    main()
