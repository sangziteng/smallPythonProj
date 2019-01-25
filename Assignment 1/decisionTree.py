#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:28:03 2019

@author: xiaojue zhang
Assignment 1 for DSO599-Python

"""

def implement():
    '''This is a function that implements a decision tree for triaging 
    suspected patients for acute cardiac ischemia using the command line.
    The tree is developed by Lee Goldman, and tested in a field study in
    the article: https://jamanetwork.com/journals/jama/fullarticle/195118'''
    
    
    print("Clinical Decision Support for Suspected Acute Cardiac Ischemia V1.0")
  
    # definition of the diagnosis print text
    diag_high = "Diagnosis: Patient has HIGH risk, refer to Coronary Care Unit"
    diag_moderate = "Diagnosis: Patient has MODERATE risk, refer to Inpatient Telemetry Unit."
    diag_low = "Diagnosis: Patient has LOW risk, refer to Inpatient Telemetry Unit."
    diag_verylow = "Diagnosis: Patient has VERY LOW risk, refer to Observation Unit."
    invalid_response = "Invalid response. Please restart"

    # logic part of diagnosis
    mi = input("Q1: Is there ECG evidence of acute Myocardial Infarction (MI)? (Y/N)\n")
    if mi == 'Y':
        print(diag_high)
    elif mi == 'N':
        evidence = input("Q2: Is there ECG evidence of acute Ischemia?\n")
        if evidence == 'Y':
            num = input("How many urgent factors are present? (0/1/2/3)\n")
            if num == '2' or num == '3':
                print(diag_high)
            elif num == '1' or num == '0':
                print(diag_moderate)
            else:
                print(invalid_response)
        elif evidence == 'N':
            num = input("How many urgent factors are present? (0/1/2/3)\n")
            if num == '2' or num == '3':
                print(diag_moderate)
            elif num == '1':
                print(diag_low)
            elif num == '0':
                print(diag_verylow)
            else:
                print(invalid_response)
        else:
            print(invalid_response)
    else:
        print(invalid_response)
