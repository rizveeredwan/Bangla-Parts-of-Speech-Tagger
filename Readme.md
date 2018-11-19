This is a python implementation of Bangla Parts of Speech Tagging. We have used microsoft annotated dataset for this purpose.</br>

We have generalized the tags and perfomed our training and testing. This projects has some specific files to do some specific works.</br>

The Process can be given following. 

a) Data/basic_dataset.txt : Its our given training sentences where each word is tagged.</br>
b) Data/basic_dataset2.txt : Its our modified version of input data where START\\* is added with each sentences. This is done by Data/base_dataset_modifier.py.</br>
First keep your dataset named basic_dataset.txt in Data folder and then run base_dataset_modifier.py.</br></br>

Now at first we have to run the data_preprocess.py. It will generate some special files to work with.</br>
a) possible_tags.txt: A special file which contains only the possible tags present in the dataset.</br>
b) tag_sequence.txt: The extraced tag sequences from the dataset.</br>
c) word-tag.txt: the word tag pairs extracted from dataset.</br>
Now run the data_preprocess.py file to generated these essential files to work with. 




