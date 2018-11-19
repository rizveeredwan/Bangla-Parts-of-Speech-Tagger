This is a python implementation of Bangla Parts of Speech Tagging. We have used microsoft annotated dataset for this purpose.</br>

We have generalized the tags and perfomed our training and testing. This projects has some specific files to do some specific works.</br>

The Process can be given following. 

a) Data/base_dataset.txt : Its our given training sentences where each word is tagged.</br>
b) Data/base_dataset2.txt : Its our modified version of input data where START\\* is added with each sentences. This is done by Data/base_dataset_modifier.py.</br>
First keep your dataset named base_dataset.txt in Data folder and then run base_dataset_modifier.py.</br></br>

Now at first we have to run the data_preprocess.py. It will generate some special files to work with.</br>
a) possible_tags.txt: A special file which contains only the possible tags present in the dataset.</br>
b) tag_sequence.txt: The extraced tag sequences from the dataset.</br>
c) word-tag.txt: the word tag pairs extracted from dataset.</br>
Now run the data_preprocess.py file to generated these essential files to work with. </br>

Now the training and testing section. Our implementation uses a gui to take input and show output. It needs pyqt4 module to work with. Our implementation uses viterbi algorithm to predict a possible tag sequence. Now viterbi uses two special function q function and e function. For q function it says q(w,u,v): How much likely this tag sequence (w,u,v) is possible and it is estimated
using uni gram probability. But you can set weight here to tri gram probability and bi gram probability if you want and bring modification in q function. For any kind of help mail me at rarndc@gmail.com. 



