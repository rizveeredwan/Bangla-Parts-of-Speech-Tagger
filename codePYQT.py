#!/usr/bin/python
# -*- coding: utf-8 -*-
# n := size of sentence
# X we assume that each word has saparate possible tag list
# it will make the algo faster


from PyQt4 import QtGui
import sys



##########For Word-Tags###########
possible_tags=[]
unique_word = dict()
word_tag_dict = dict() 
count_each_tag=dict() 
total_words = 0

#####For Tags##########
count_tag_sequence_tri = dict() 
count_tag_sequence_bi = dict() 
count_tag_sequence_uni=dict() 

def q(w,u,v):
    global count_tag_sequence_tri
    global count_tag_sequence_bi
    global count_tag_sequence_uni
    global total_words
    #previous 
    """
    prob = (count_tag_sequence_tri[w][u][v]*1.0)/(count_tag_sequence_bi[u][v])
    """
    
    prob =  (count_tag_sequence_uni[v]*1.0)/(total_words)
    return prob #taking reverse 


def e(word,tag):
    if(word in word_tag_dict[tag]):
        value = (word_tag_dict[tag][word]*1.0)/(count_each_tag[tag])
    else:
        value = 0.00000000001
    return value

def getTagList():
    global possible_tags
    if(len(possible_tags) == 0):
        #need to read files 
        f=open("Data/possible_tags.txt")
        lines = f.readlines()
        for i in lines:
            temp=i.split()
            possible_tags.append(temp[0])   
        f.close() 
    return possible_tags

def viterbi( sentence ) :
    
    n = len(sentence.split())
    x = sentence.split()
    S = getTagList()
    

    #value
    dp = {}
    dp[ (-1, ('*', '*')) ] = 1
    #path
    dr = {}
    dr[ (-1, ('*', '*')) ] = ""


    #dp/f (K, U, V): loop(W) := K tomo index er word V, K-1 index U r K-2 te W
    #q(v, w,u) : eta ashole q(v|w,u) mane tag sequence ta hoy w,u,v
    #e(s, v) :  mane s word e v tag boshate chai


    # baki sob k er jonno
    for k in range (0, n):
        
        if (k == 0):
            # for k=0
            for v in S:

                dp[ (0, ('*', v) ) ] = q('*', '*',v) * e(x[0], v)
                dr[ (0, ('*', v)) ] = '*'
                #print "v= ",v,dp[ (0, ('*', v) ) ]
                 
                
        elif (k == 1):
            # for k=1
            for v in S:
                for u in S:
                    temp = dp[(0, ('*', u))] * q('*',u,v) * e(x[1], v)
                    if(1,(u,v)) in dp:
                        if dp[ (1, (u, v)) ] < temp: #reversing taking min 
                            dp[ (1, (u, v)) ] = temp
                            dr[ (1, (u, v)) ] = '*'
                    else:
                        dp[ (1, (u, v)) ] = temp
                        dr[ (1, (u, v)) ] = '*'
                    #print "v= ",u,v,dp[ (1, (u, v) ) ]
        else :
            for u in S:
                for v in S:
                    for w in S:
                        temp = dp[(k-1, (w,u))] * q(w,u,v) * e(x[k],v)
                        if(k,(u,v)) in dp:
                            if dp[ (k, (u, v)) ] < temp: #taking min 
                                dp[ (k, (u, v)) ] = temp
                                dr[ (k, (u, v)) ] = w 
                        else:
                            dp[ (k, (u, v)) ] = temp
                            dr[ (k, (u, v)) ] = w

    tagseq = list()

    mx = -1000000000000
    uu = -1000000000000
    vv = -1000000000000
    
    for u in S:
        for v in S:
            if ((n-1, (u, v))) in dp and dp[ (n-1, (u, v)) ] > mx:
                mx = dp[ (n-1, (u, v)) ]
                uu = u
                vv = v

    u = uu
    v = vv
    
    if(mx == -1000000000000):
        for u in S:
            if((0,("*",u)) in dp and dp[(0,("*",u))] > mx):
                mx = dp[(0,("*",u))]
                uu = u 
        save = []
        save.append(uu)
        return save

    #print u,v,mx
    tagseq.append(v)
    tagseq.append(u)

    for k in range(n-1, 1, -1):
        w = dr[ (k, (u, v)) ]
        tagseq.append(w)
        u = w
        v = u

    tagseq.reverse()
    #print tagseq
    return tagseq

forbidde_list = []  
                
def train_for_e_func():
    global possible_tags
    global unique_word
    global word_tag_dict
    global count_each_tag
    f=open("Data/possible_tags.txt")
    line=f.readlines() 
    for i in line:
        save=i.split()
        possible_tags.append(save[0]) 
        word_tag_dict[save[0]]=dict() 
        count_each_tag[save[0]]=0
    f.close()

    f=open("Data/word-tag.txt")
    line=f.readlines() 
    
    guni=0
    for i in line:
        save=i.split()
        if(save[0] not in unique_word):
            guni=guni+1
            unique_word[save[0]]=True
            for j in word_tag_dict:
                word_tag_dict[j][save[0]]=1
                count_each_tag[j]=count_each_tag[j]+1
        word_tag_dict[save[1]][save[0]]=word_tag_dict[save[1]][save[0]]+1 
        count_each_tag[save[1]]=count_each_tag[save[1]]+1
    
    return 

def traning_for_q_func():
    #generating all possible tri/bi_sequences 
    #* cases 
    count_tag_sequence_tri["*"]=dict() 
    count_tag_sequence_tri["*"]["*"]=dict()
    
    count_tag_sequence_uni['*'] = 1
    global total_words
    total_words=total_words+1

    count_tag_sequence_bi["*"]=dict() 
    count_tag_sequence_bi["*"]["*"]=1
    for i in possible_tags:
        count_tag_sequence_tri["*"]["*"][i] = 1
        count_tag_sequence_bi["*"][i]=1
        count_tag_sequence_uni[i] = 1
        total_words=total_words+1 
    for i in possible_tags:
        count_tag_sequence_tri["*"][i]=dict() 
        for j in possible_tags:
            count_tag_sequence_tri["*"][i][j] = 1

    for i in possible_tags:
        count_tag_sequence_tri[i]=dict()
        count_tag_sequence_bi[i] = dict()
        for j in possible_tags:
            count_tag_sequence_tri[i][j]=dict()
            count_tag_sequence_bi[i][j] = 1
            for k in possible_tags:
                count_tag_sequence_tri[i][j][k]=1
    #count section 
    f=open("Data/tag_sequence.txt")
    lines = f.readlines()
    f.close()
    for i in lines:
        temp=i.split()
        for j in range(0,len(temp)):
            count_tag_sequence_uni[temp[j]]=count_tag_sequence_uni[temp[j]]+1 
            total_words=total_words+1 
            if((j+1)<len(temp) and (j+2)<len(temp)):
                count_tag_sequence_tri[temp[j]][temp[j+1]][temp[j+2]]=count_tag_sequence_tri[temp[j]][temp[j+1]][temp[j+2]]+1
            if((j+1)<len(temp)):
                count_tag_sequence_bi[temp[j]][temp[j+1]]=count_tag_sequence_bi[temp[j]][temp[j+1]]+1      
    return 

print "Training starting for e"
train_for_e_func()
print "Training Complete for e"

print "Training starting for q"
traning_for_q_func()
print "Training complete for q"




def convert_list_to_string(list_of_words):
    ans = "" 
    for i in list_of_words:
        #print i
        if(ans == ""):
            ans=i
        else:
            ans=ans+" "+i
    return ans 

def two_string_comp(str1,str2):
    #print str1,str2
    a=str1.split()
    b=str2.split()
    milse=0
    global threshold
    for i in range(0,len(a)):
        if(a[i] == b[i]):
            milse=milse+1 
    if((milse*1.0)/(len(a)) >= threshold):
        return (True,milse,len(a))
    return (False,milse,len(a))

threshold=0.7

i=0
corrected=0
corrected_tag= 0
total_tag=0 

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
    def initUI(self):
        self.input_sentence = QtGui.QLabel('Bangla Sentence')
        self.output_tag_sequence = QtGui.QLabel('POS Sequence')

        self.input_edit = QtGui.QLineEdit()
        self.output_tag_sequence_edit = QtGui.QLineEdit()

        #authorEdit = QtGui.QLineEdit()
        self.check_button = QtGui.QPushButton("check")
        self.check_button.clicked.connect(self.check_button_press)

        self.clear_button = QtGui.QPushButton("clear")
        self.clear_button.clicked.connect(self.clear_button_press)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.input_sentence, 1, 0)
        grid.addWidget(self.input_edit, 1, 1)

        grid.addWidget(self.output_tag_sequence, 2, 0)
        grid.addWidget(self.output_tag_sequence_edit, 2, 1)

        grid.addWidget(self.check_button, 3, 1)
        grid.addWidget(self.clear_button, 4, 1)

        self.setLayout(grid) 
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Bangla Poss Tagger') 
        self.show() 
        return
    
    def check_button_press(self):
        input_sentence = unicode(self.input_edit.text())
        input_sentence = input_sentence.encode('utf-8')
        result = viterbi(input_sentence)
        input_sentence=input_sentence.strip() 
        print input_sentence
        output=""
        for i in range(0,len(result)):
            if(output==""):
                output=result[i]
            else:
                output=output+" "+result[i]
        print output
        self.output_tag_sequence_edit.setText(output.decode('utf-8'))
        print result
    def clear_button_press(self):
        self.input_edit.clear()
        self.output_tag_sequence_edit.clear() 
        return


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()