From training we aimed at acquiring the following probabilities:

Probability of a particular part of speech to begin a sentence.
Probability of a part of speech to follow other part of speech.
Probability of a word for a given part of speech.

Naive Bayes:

For each word in a sentence we check for the parts of speech and select the best one using the probabilities calculated in the training. Then we multiply the probability of each part of speech given the word with the probability of the part of speech.The max of these is the best result of the given word.

Viterbi:

In viterbi for the first word depends on the probability that the part of speech comes first in a sentence and the probability of the word given speech,then we store the max values.For the second word we use transition, emission, previous viterbi values.We take the max of product of transition probability and previous viterbi values of it and multiply it with the emission probability.
We repeat the same for all words and store the values during this forward cycle.Then we backtrack along the previously used viterbi coefficients leading to the best path.
To break the encrypted code we pass Corpus,encrypted string.
Expected outputs:

Best possible decrypted file based on the probabilities calculated from the given english corpus with in a given time.
Approach:

1)First step we generate the probabilites for every 2 alphabet pairs i.e,  26 * 26 value pairs.From the English corpus we split the read string considering two character pairs at time and push the count of such occuring pairs into a dictionary.Space was also considered as a character while generating the probabilities. 

2)We create a Replacement table by shuffling the alphabets and Rearrangement table based on shuffled 1-4 integers.

3)We pass the randomly initialized tables and the input text to the encode function(which was given)

4)The resultant string was analysed in the following ways:
  
  a)Two characters taken at a time
  
  b)Each word taken at a time
  
  c)4 characters taken at a time

5)For the above mentioned ways we calculate each of the probabilities for 2 consecutive pairs traversing through the string these pobabilities are multiplied till the final character and update it as a current maximum probability.

6)From the next iterations we modify the Rearrangement and Replacement tables and repeat step 5

7)From all the analysed cases if space is included case:a gives a better output compared to the other 2 

Inputs:
Spam and Notspam emails as a training data.

Test files for predicting the accuracy of the trained model

Expected output:
Test files to be correctly detected as spam if so.

Approach:

NAIVE-BAYES Implementation:

1)We read the files from Training directories(spam and not spam) and each file is split on space without any preprocessing.

2)We create 2 dictionaries for spam and notspam where the splitted words are keys and their frequency as the values.

3)We read the input string and split the same way as the training data and create a dictionary.  

4)We calculate the probability for each word in the testing dictionary if it is present in the created training dictionaries i.e, 
frequency of the word/total number of word count in a particular dictionary.

5)If the word is not in the dictionary we get 0.so we add 1 to each word while calculating the probabilites and the total number of added 1s to the denominator

6)We add up the log values of the resuting probabilites from spam and not spam cases with the initial probability for each case as probability of spam files and probability of nonspam files respectively.

7)Next we compare the resultant probabilities and the output is decided by the max value from the comparision.

8)We get the accuracy by comparing the predictions to the given groundtruth values.
  For the applied model we get the 94.6 Percent accuracy. 

9)We append the Predictions to the test files and write it out to the output file.IT is added to repository for reference.
