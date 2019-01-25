# -*- coding: utf-8 -*-

import pandas as pd # This is the standard
import re

def analyze(reviewFile, stopwordFile, numWords = 20):
    '''reviewFile: the path to a .txt file containing customer reviews. 
                    The format is assumed to be the same as the test data sets attached to this assignment.
    stopwordFile: the path to a .txt file containing a list of commonly occurring English 
                    words to ignore (such as “a”, “the”, “and”, etc). The format is assumed to be the same as
                    the "stopwords.txt" file attached to this assignment.
    numWords (default value 20): An integer specifying the number of rows to include in the DataFrame returned.
    
    The function should return a Pandas DataFrame'''
    
    #reviewFile = "reviews3.txt"
    #stopwordFile = "stopwords.txt"
    
    ## the logic about stop words
    stopwords = open(stopwordFile, 'r')
    stopword_list = []
    for stopw in stopwords:
        stopw = stopw.strip()
        stopword_list.append(stopw)
        
    
    reviewfile = open(reviewFile, 'r')
    words = [] # define an empty list
    
    each_review_word_dic = {} #define an empty dictionary to accept the word and count for each review
    occurences = {} #define an empty dictionary to accept all the word and occurences for all the reviews
    reviews = {} #define an empty dictionary to count how many reviews have XX review word
    
    #review_num = 0
    
    for review in reviewfile:
        review = review.strip()
        
        if review.startswith("Review #:"): 
            #review_num += 1
            #print("Review #:", review_num) #for debug: show current review number
            continue
        elif review.startswith("Date:"): 
            continue
        else: 
            #start to analyze the content of a single review
            #delete all the punctuations using Regex. (better than string.punctuation)
            #and then strip the whitespaces and split into words list in lowercase 
            words = re.sub(r'[^\w\s]',' ',review).strip().lower().split(' ')
            
            for word in words:
                word = word.strip()
  
                #skip all the stopwords
                if word in stopword_list:
                    continue
                if word == '':
                    continue
                    
                # count how many times the word occurs in this review separately
                if word not in each_review_word_dic:
                    each_review_word_dic[word] = 0
                each_review_word_dic[word] += 1

            #before finish the process for each review, we add each_review_word_dic to occurences
            for each_review_word in each_review_word_dic:
                if each_review_word not in occurences:
                    occurences[each_review_word] = 0
                occurences[each_review_word] += each_review_word_dic[each_review_word]
        
                #before finish the process for current review, add 1 to the # of reviews if the word occures
                if each_review_word not in reviews:
                    reviews[each_review_word] = 0
                reviews[each_review_word] += 1
        
        each_review_word_dic = {} #reset the each_review_word_dic dictionary for next review        


    reviewfile.close()
    stopwords.close()
  
    
    ###Create a DataFrame
    occurences_df = pd.DataFrame.from_dict(occurences, orient = 'index', columns = ['Occurences'])
    reviews_df = pd.DataFrame.from_dict(reviews, orient = 'index', columns = ['Reviews'])
    
    #join the two dataframe on index(word)
    finalDataFrame = pd.merge(occurences_df, reviews_df,left_index=True, right_index=True)
    
    #Sort the DataFrame by the column "Occurrences" and return only the first numWords many rows.
    finalDataFrame = finalDataFrame.sort_values('Occurences', ascending = False)
    
    return finalDataFrame.head(numWords)
        
    