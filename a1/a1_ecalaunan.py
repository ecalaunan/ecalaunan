#!/usr/bin/env python3
''' template for ops435 assignment 1 script
    The purpose of the script is to take any argument in this form YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD"
    and convert it to a date format like this "MMM DD, YYYY" 
    for example: this argument "2020/10/21" will return Oct 21, 2020
-----------------------------------------------------------------------
OPS435 Assignment 1 - Fall 2020
Program: a1_ecalaunan.py
Author: Eddyson Calaunan
The python code in this file (a1_ecalaunan.py) is original work written by
"Eddyson Calaunan". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import os
import sys

def leap_year(obj):
    
    '''
    This function will check to see if the year provided is a leap year
    '''
    obj_leaptest = obj % 4
    if obj_leaptest > 0 :
    	return False
    else : 
    	return True

def sanitize(obj1,obj2):
    
    '''
    This function will create a new string using characters from obj1 that are in obj2. To remove any unnecesary characters
    '''
    sanitizeStr = ''
    counter = 0 
    for i in obj1 :
    	character = obj1[counter]
    	if character not in obj2:
    		counter += 1
    	else: 
    		sanitizeStr += character
    		counter += 1 

    return sanitizeStr

def size_check(obj, intobj):
    '''
    This function will check to see if the length of obj is equal the intobj 
    '''
    if len(obj) != intobj:
    	status = False
    else: 
    	status = True


    return status

def range_check(obj1, obj2):
    '''
    This function will check to see if obj1 is within the range of obj2 
    '''
    if obj1 < obj2[0] or obj1 > obj2[1]: 
    	status = False
    else :
    	status = True
    
    return status
    
def usage():    
    '''
    This function will print how to use the script, with possible arguments that can be provided
    '''

    status = "Usage: a1_ecalaunan.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD"

    return status

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   # setp 4
   result = size_check(dob,8)
   if result == False:
       print("Error 09: wrong date entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   print(new_dob)  
