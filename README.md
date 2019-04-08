README
=======

## Components 
* Collect images of cars from the web. Work required: 2. Our ideas so far are: 

	1. An image clearly with a car
	2. An image clearly without a car
	3. An image that may have a car in the corner	
	4. A blurry image
	5. A cartoon car
	6. A truck 
* Write up appeals for each image. Work required: 3 Our ideas so far are (numbered corresponding to the image list above):
	1. (a) "I said there is a car and there clearly is" (b) I misclicked that there is not a car.
	2. (a) "I said there is not a car there clearly is not" (b) I misclicked that there is a car.
	3. (a) "That tire and hood in the corner looks like a car" (b) "That tire and hood is not an entire car" (c) "The instructions were not clear on whether it needed to be a full car"
	4. (a) "The image was too blurry to tell"
	5. (a) "The instructions did not specify whether cartoon cars count" Works for both yes/no
	6. (a) "The isntructions did not specify whether trucks count" Works for both yes/no
* Quality Control. We will limit this to workers with approval rating > 90%, workers who did not write the appeal, and workers who have completed > 100 HITS. We may or may not tell the judges this information when they review the appeal. We can also implement some ethical questions survey before the workers judge the appeal to do quality control, or have an idea of the baseline of who is voting on the appeals. Work required: 1
* Crowdsourcing the judgement on the appeals on Mechanical Turk at 3 different pay levels: 1 cent, 5 cents, and 10 cents. We will publish each type of appeal, one where the worker got rejected for a right answer and one where the worker got rejected for a wrong answer. Each individual appeals receives its judgement after it has been voted on by 5 workers (could be another number). Work required: 4
* Aggregation Control. We will collect the results for each payment amount by majority vote and weighted majority vote. Potentially will also do a unanimous vote check to try to simulate an actual jury. Work required: 4.
* Analyzing the results. We will judge whether there is a difference in the voting/honesty of workers based on how much they are being paid to judge the appeal. We will also analyze whether there is a tendency for workers to side with otehr workers for getting paid. Work required: 4.


##DATA
We have collected image urls for each of the categories above (image_urls.xlsx).  The input file (see input_file.csv) for Mechanical Turk consists of three columns.  The first is the image url, the second is the appeal we are testing, and the third states whether the appeal is objectively valid, objectively invalid, or is in a "grey zone" with no right or wrong answer.  We have included 5 images from each category.  The appeal next to each image is the appeal in the respective category listed above.  If there is two appeals for the category, the image url appears in two rows, one for each appeal.

There is a sample output file (sample_output.csv) for our quality control model based on what the csv file we would get from Mechanical Turk once our task is completed.  It has fake data in it right now, but the output of the real file would look the same.

The input file for our aggregation step is the sample output file from the previous step (sample_output.csv). The output file for our aggregation step is called sample_output_agg.csv. This outlines the reward, the corresponding valid label, and the workers' aggregated label, based on our aggregation methods.

One aggregation method we implemented was simple majority vote. This took the majority opinion of fair/unfair and labeled a corresponding HIT accordingly. The sample code for this step can be found in the file /src/s_majority.py.