#AI assignment1
from __future__ import division


def setOfWords2Vec(vocabList,inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
           returnVec[vocabList.index(word)] = 1
        else:
            pass
           #print"word:%s is not in my Vocabulary" % word
    return returnVec

def storeSentence(sentence):
    sentenceList =[]
    for word in sentence.split(' '):
        word = word.strip()
        sentenceList.append(word)
    return sentenceList
#----------------------------------start the program------------------------------------
print '----------------------------Start the program-------------------------------'
print '----------------------------Pre-processing Step-----------------------------'

traindata_file = '/Users/chongli/PycharmProjects/NaivebayesClassifier/traindata.txt'
trainlables_file = '/Users/chongli/PycharmProjects/NaivebayesClassifier/trainlabels.txt'
stoplist_file = '/Users/chongli/PycharmProjects/NaivebayesClassifier/stoplist.txt'
vocabulary = []
stoplist=[]
withoutLable_vectors = []
withLable_vectors = []
M = 0
#-------convert stoplist_file into a LIST------------
with open(stoplist_file,'r') as s:
    for line in s:
        for word in line.split(' '):
            word = word.strip()
            stoplist.append(word)

stoplist.sort()
#print 'in stoplist:'
#for i in stoplist:
#  print i
#-------form an vocabulary------------
with open(traindata_file,'r') as td:
    for line in td:
        for word in line.split(' '):
            word = word.strip()
            vocabulary.append(word)

vocabulary = list(set(vocabulary))   #remove duplication
vocabulary.sort()
vocabulary.remove('')                #remove ''

for word in stoplist:
    if word in vocabulary:
        vocabulary.remove(word)
M = len(vocabulary)

'''print 'in file1:'
for i in vocabulary:
    print i
print M  ''' #get the size of vocabulary

#--------form vectors-----------------
with open(traindata_file, 'r') as td:
    for line in td:
        line = line.strip()
        test = storeSentence(line)  # get each sentence list
        withoutLable_vectors.append(setOfWords2Vec(vocabulary, test))
#print withoutLable_vectors

#----add labels in each end-------
trainlabels=[]
with open(trainlables_file,'r') as d:
    for line in d:
        line = line.strip()
        trainlabels.append(int(line))   #convert the content of lable into a list trainlabels[]
#print trainlabels

mid=[]
for x in range(1,len(withoutLable_vectors)):  # x represent the index
    #print len(withoutLable_vectors[x])
    mid.append(trainlabels[x])
    withLable_vectors.append(withoutLable_vectors[x]+ mid) #"+" is suitable for adding two list
    #print len(withLable_vectors[x - 1])
    mid.pop(0)

#--------store the result into proprecess.txt file
filename = "preprocessed.txt"
target = open(filename,'w')
for item in vocabulary:
    target.write(item + ',')
for item in withLable_vectors: ###################need combine vectors with labels and output them into file##################
    for eachNum in item:
        target.write((str)(eachNum) + ',')
    target.write('\n')
target.close()

#preprocessing step
#1  (checked)put stopword into LIST
#2-1 (checked)put traindata into LIST,
#2-2 (checked)remove stopword, convert it into vocalbulary, size = M
#3 (checked)compare each sentance with vocalbulary , and combine it with trainable.txt, become vectors
#[[ + class label],[],[]...]
#4(checked)tore the vocabulary with vectors into proprecess.txt file(need to be finished)

#classifier step
#---------get parameters--------------
filecount = 0
file0Num = 0
file1Num = 0
with open(trainlables_file,'r') as ta:
    for line in ta:
        line = line.strip()
        filecount = filecount + 1
        if line == '0':
            file0Num = file0Num + 1
    file1Num = filecount - file0Num
p_class0 = file0Num/filecount
p_class1 = file1Num/filecount

print p_class0
print p_class1

#get p_word_c from traindate.txt;
#plan to create a dictionary for each class c:{word:count;word:count}
class0_dic = {}
class1_dic = {}
'''how to calculate? there is a stupid method:
use withLabel_vectors, divide this vectors into class0_vec_list and class1_vec_list.
for each vec_list, calculate how many words shows in it===>sum of them is the total num of words in class0;
if we want to calculate a specific word, we need get the index of this word in vocalbulary, use index to check each vector in  class0,
count the num of word showing times. update the value in class0_dic{}.
 '''

#smooth part
#convert log
#predict testdata.txt

#rewrite it within the type of OOP







