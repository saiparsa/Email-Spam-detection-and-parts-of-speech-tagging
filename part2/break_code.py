#!/usr/local/bin/python3
# CSCI B551 Fall 2019
#
# Authors: SANATH KEERTHI EDUPUGANTI,SAI PRASAD PARSA,AKHIL NAGULAVANCHA
#
# based on skeleton code by D. Crandall, 11/2019
#
# ./break_code.py : attack encryption
#


import random
import math
import copy 
import sys
import encode
import numpy as np
import time 


# put your code here!

def calculate_prob(dec,prob_dict):
    spl=[]
    for i in range(len(dec)-1):
      spl.append(dec[i]+dec[i+1])
    ini_prob=0
    for i in range(len(spl)):
        if spl[i] in prob_dict.keys():
            ini_prob=ini_prob+np.log(prob_dict[spl[i]])
            
    return ini_prob

def break_code(string, corpus):
    corp=corpus.replace("\n"," ")
    #n=2
    #out = [(corp[i:i+n]) for i in range(0, len(corp), n)] 
    ou=[]
    for i in range(len(corp)-1):
      ou.append(corp[i]+corp[i+1])
    words=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
    rearrange_inp=[0,1,2,3]
    corp1={}
    #count=0
    letter=[]
    for j in range(27):
      for i in range(27):
        letter.append(words[i]+words[j])
    for i in range(len(letter)):
        corp1[letter[i]]=1
    for  i in range(len(ou)):
        if ou[i] in corp1.keys():
            corp1[ou[i]]=corp1[ou[i]]+1
    corp2={}
    for i in range(len(corp1)):
      corp2[letter[i]]=corp1[letter[i]]/(sum(corp1.values())+len(letter))
    word=[]
    for i in range(len(words)):
        word.append(words[i])
    rearrange_shuff=[]
    for i in range(len(rearrange_inp)):
        rearrange_shuff.append(rearrange_inp[i])
    random.shuffle(word)
    replace={}
    for i in range(len(words)):
      replace[words[i]]=word[i]
    
    #for rearrangement
    random.shuffle(rearrange_shuff)
    rearrange={}
    for i in range(len(rearrange_inp)):
      rearrange[rearrange_inp[i]]=rearrange_shuff[i]
    
    curr_decode=encode.encode(string, replace, list(rearrange.values())) 
    prob=calculate_prob(curr_decode,corp2)
    curr_prob=prob
    #curr_dict=dict1.copy()
    total=time.time()+60*10
    while time.time()<total:
            #for replacement
        random.shuffle(word)
        replace={}
        for i in range(len(words)):
          replace[words[i]]=word[i]
        
        #for rearrangement
        random.shuffle(rearrange_shuff)
        rearrange={}
        for i in range(len(rearrange_inp)):
          rearrange[rearrange_inp[i]]=rearrange_shuff[i]

        decode1=encode.encode(string, replace, list(rearrange.values())) 
        prob=calculate_prob(decode1,corp2)
        
        if prob>curr_prob:
            curr_prob=prob
            #curr_dict=dict1.copy()
            curr_decode=decode1
        
    
    return curr_decode

if __name__== "__main__":
    if(len(sys.argv) != 4):
        raise Exception("usage: ./break_code.py coded-file corpus output-file")

    encoded = encode.read_clean_file(sys.argv[1])
    corpus = encode.read_clean_file(sys.argv[2])
    decoded = break_code(encoded, corpus)

    with open(sys.argv[3], "w") as file:
        print(decoded, file=file)

