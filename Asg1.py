#AI assignment1
from __future__ import division


def setOfWords2Vec(vocabList,inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
           returnVec[vocabList.index(word)] = 1
        else:
           print"word:%s is not in my Vocabulary" % word
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

traindata_file = '/Users/chongli/IdeaProjects/comp6721asg1/Data_for_the_NB_classifier/traindata.txt'
trainable_file = '/Users/chongli/IdeaProjects/comp6721asg1/Data_for_the_NB_classifier/trainlabels.txt'
stoplist_file = '/Users/chongli/IdeaProjects/comp6721asg1/Data_for_the_NB_classifier/stoplist.txt'
vocabulary = []
stoplist=[]
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

print 'in file1:'
for i in vocabulary:
    print i
print M   #get the size of vocabulary

#--------form vectors-----------------
with open(traindata_file, 'r') as td:
    for line in td:
        line = line.strip()
        test = storeSentence(line)  # get each sentence list
        withLable_vectors.append(setOfWords2Vec(vocabulary, test))
print withLable_vectors
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
#3 compare each sentance with vocalbulary , and combine it with trainable.txt, become vectors
#[[ + class label],[],[]...]
#4store the vocabulary with vectors into proprecess.txt file(need to be finished)

#classifier step
#---------get parameters--------------
filecount = 0
file0Num = 0
file1Num = 0
with open(trainable_file,'r') as ta:
    for line in ta:
        line = line.strip()
        filecount = filecount + 1
        if line == '0':
            file0Num = file0Num + 1
    file1Num = filecount - file0Num
pC0 = file0Num/filecount
pC1 = file1Num/filecount

print pC0
print pC1







