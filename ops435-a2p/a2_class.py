#!/usr/bin/python3
'''
OPS435 Assignment 2P - Fall 2020
Program: a2p_ecalaunan.py 
Author: Eddyson Calaunan
The python code in this file (a2p_ecalaunan.py) is original work written by
Eddyson Calaunan. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
'''
import os
import sys


def range_check(obj1, obj2):

#This will check if obj1 is within the parameters of obj2[0] to obj[1]

	if obj1 < obj2[0] or obj1 > obj2[1]:
		status = False
	else:
		status = True

	return status

def leap_year(obj):

#This will check if obj year is a leap year

	leapTest = obj % 4
	leapTest2 = obj % 400
	if leapTest == 0 :
		return False
	else:
		return True


class Date:

	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day


	def __repr__(self):
		return '%d-%02d-%02d' % (self.year, self.month, self.day)


	def __str__(self):
		return '%d/%02d/%02d' % (self.year, self.month, self.day)

		
	def __add__(self, other): 
		test = 1
		counter = 0
		days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
		while test == 1:
			if self.month == 2:
				leapcheck = leap_year(self.year)
				if leapcheck == False:
					days_in_month[2] = 29
				else: 
					days_in_month[2] = 28
			newDay = self.day + other
			result = range_check(newDay, (1, days_in_month[self.month]))
			while result == False: 
				newDay = newDay - days_in_month[self.month]
				self.month += 1
				if self.month > 12:
					self.year +=1
					self.month = 1
				result = range_check(newDay, (1, days_in_month[self.month]))
				if result == True:
					self.day = newDay
					test = 0
			else:
				self.day = newDay 
				test = 0
		return self
		
		
		
	def __sub__(self, other):
		test = 1
		counter = 0
		days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
		days_in_month_other = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
		if type(other) == int:
			while test == 1:
				leapcheck = leap_year(self.year)
				if leapcheck == False:
					days_in_month[2] = 29
				else:
					days_in_month[2] = 28
				newDay = self.day - other
				result =range_check(newDay, (1, days_in_month[self.month]))
				while result == False:
					newDay = newDay + days_in_month[self.month]
					self.month -=1
					if self.month < 1:
						self.year -= 1
						self.month = 12
					result = range_check(newDay, (1, days_in_month[self.month]))
					if result == True:
						self.day = newDay
						test = 0
				else:
					self.day = newDay
					test = 0
			
			return self
		elif type(other) == Date:	
			while test == 1:
				leapcheckSelf = leap_year(self.year)
				if leapcheckSelf == False:
					days_in_month[2] = 29
				else:
					days_in_month[2] = 28
				totalselfDays = self.day
				while counter != self.month - 1:
					totalselfDays += days_in_month[counter + 1]
					counter +=1

				counter = 0
				
				leapcheckOther = leap_year(other.year)
				if leapcheckOther == False:
					days_in_month_other[2] = 29
				else:
					days_in_month_other[2] = 28
				totalotherDays = other.day
				while counter != other.month - 1:
					totalotherDays += days_in_month_other[counter + 1]
					counter +=1	

				return totalselfDays - totalotherDays
				
			
	
	def tomorrow(self):
		days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
		dummy = self
		dummy.day += 1
		result = range_check(dummy.day, (1, days_in_month[dummy.month]))
		while result == False:
			dummy.day = dummy.day - days_in_month[dummy.month]
			dummy.month += 1
			if dummy.month > 12:
				self.year +=1
				self.month = 1
			
		return dummy	
	
	
	def yesterday(self):
		self.day -= 1
		return self

#	def day_of_week(self):
		
