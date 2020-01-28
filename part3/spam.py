import numpy as np
import os
import sys

if __name__== "__main__":
    if len(sys.argv) != 4:
        raise Exception("Error: expected 3 arguments")
    training_Directory = sys.argv[1]
    testing_Directory = sys.argv[2]
    Outputfile = sys.argv[3]
ospath= os.getcwd()

trainspam_path=ospath+"/"+training_Directory+"/spam"
train_notspam_path=ospath+"/"+training_Directory+"/notspam"
test_path=ospath+"/"+testing_Directory
spam_filelist = os.listdir(trainspam_path)
notspam_filelist = os.listdir(train_notspam_path)
test_list=os.listdir(test_path)

numtest=len(test_list)
numSpam=len(spam_filelist)
numnonSpam=len(notspam_filelist)
total=numSpam+numnonSpam
pa=numSpam/total
pna=numnonSpam/total

fis={}
for i in range(numSpam):
  with open(trainspam_path+"/"+spam_filelist[i], 'r', encoding="Latin-1") as f: 
        h=str.split(f.read())
        for j in range(len(h)):
          if h[j] in fis.keys():
            fis[h[j]]=fis[h[j]]+1
          else:
            fis[h[j]]=1

fins={}
for i in range(numnonSpam):
  with open(train_notspam_path+"/"+notspam_filelist[i], 'r', encoding="Latin-1") as f1: 
        h1=str.split(f1.read())
        for j in range(len(h1)):
          if h1[j] in fins.keys():
            fins[h1[j]]=fins[h1[j]]+1
          else:
            fins[h1[j]]=1
addition=len(set(list(fis.keys())+list(fins.keys())))
sum1=sum(fis.values())
tot=sum1+addition
sum2=sum(fins.values())
tot2=sum2+addition

final_out=[]
def output(x,y):
  if x>y:
    return "spam"
  else:
    return "notspam"

for i in range(numtest):
  with open(test_path+"/"+test_list[i], 'r', encoding="Latin-1") as f2:
      h3=str.split(f2.read())
      tes={}
      for j in range(len(h3)):
          if h3[j] not in tes.keys():
            tes[h3[j]]=1
      d=len(tes)
      #for spam
      #def spamprob(files)
      spam_prob=np.log(pa)
      for i in range(d):
         if h3[i] in fis.keys():
            spam_prob=spam_prob+np.log(fis[h3[i]]+1/tot)
         else:
            spam_prob=spam_prob+np.log(1/(tot))
        #for non spam
      spam_prob1=np.log(pna)
      for i in range(d):
         if h3[i] in fins.keys():
             spam_prob1=spam_prob1+np.log(fins[h3[i]]+1/(tot2))
         else:
             spam_prob1=spam_prob1+np.log(1/(tot2))
      final_out.append(output(spam_prob,spam_prob1))


final_outf=[]
for i in range(numtest):
    final_outf.append(test_list[i]+"  "+final_out[i]+"\n")

fo = open(Outputfile,"w")
for i in range(len(test_list)):
    j = fo.write(final_outf[i])
fo.close()


