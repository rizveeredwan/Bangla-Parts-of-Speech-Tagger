"""
purpose of this file is to preprocess data. To read from Data/base_dataset.txt 
Output will be two separate files.
a) tagged.txt => only tag sequences 
b) word_tag.txt => counter of word/tag 
"""

delete_tags = ['PU','RDS','PU1985','RDF','RDX'] 
found_tags = []
word=[]
cor_tag=[]

o=open("Data/tag_sequence.txt","w")
p=open("Data/word-tag.txt","w") 
q=open("Data/possible_tags.txt","w")


def tag_coverter(choice):
    if(choice == 'N' or choice == 'NC' or choice == 'NP' or choice == 'NV' or choice == 'NST'):
        return "N" 
    if(choice == 'V' or choice == 'VM' or choice == 'VAUX' or choice == "VA"):
        return "V"
    if(choice == 'P' or choice == 'PPR' or choice == 'PRF' or choice == 'PRC' or choice == 'PRL' or choice == 'PWH'):
        return "P"
    if(choice == 'J' or choice == 'JJ' or choice == 'JQ'):
        return "J" 
    if(choice == "D" or choice == 'DAB' or choice == 'DRL' or choice == 'DWH'):
        return "D"
    if(choice == 'A' or choice == 'AMN' or choice == 'ALC'):
        return "A" 
    if(choice[0] == 'L'):
        return "L" 
    if(choice == 'PP'):
        return "PP"
    if(choice[0] == "C"):
        return "C"
    return choice


class ReadFile:
    def __init__(self):
        pass 
    def read(self,filename):
        counter=0
        global o,p
        with open(filename) as infile:
            for line in infile:
                tag_sequence = ""
                counter=counter+1
                save = line.split()
                for j in save:
                    temp = j.split('\\')  # \ is the split 
                    if(temp[1] in delete_tags):
                        continue
                    tag = temp[1].split('.')
                    if(tag[0] == ""):
                        continue
                    if(tag_sequence == ""):
                        tag_sequence=tag[0]
                    else:
                        tag_sequence=tag_sequence+" "+tag_coverter(tag[0])
                    #print "real ",tag[0],"coverting ",tag_coverter(tag[0])
                    tag[0] = tag_coverter(tag[0]) #simplifying tags 
                    #print tag[0]
                    if(tag[0] != "*"):
                        p.write(temp[0]+' '+tag[0]+'\n')
                    if(tag[0] not in found_tags and tag[0] != "*"):
                        found_tags.append(tag[0])
        #print found_tags
                o.write(tag_sequence+'\n')
        for i in found_tags:
            q.write(i+"\n")
                    

obj = ReadFile()
obj.read("Data/base_dataset2.txt")
        