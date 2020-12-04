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
	''' 
	This function will check to see if obj 1 is within the range of obj2
	'''	

	if obj1 < obj2[0] or obj1 > obj2[1]:
		status = False
	else:
		status = True

	return status

def leap_year(obj):
	'''
	This will check if obj year is a leap year
	'''
	leapTest = obj % 4
	leapTest2 = obj % 400
	if leapTest == 0 :
		return False
	else:
		return True


class Date:
	'''
	This is a class for dates, in this class addition, subtraction, tomorrow, yesterday and day of week functions are provided
	'''
	def __init__(self, year, month, day):
		'''
		This function creates the values in the date class for year, month and day
		'''
		self.year = year
		self.month = month
		self.day = day


	def __repr__(self):
		'''
		This function takes the date returned and returns it in this format yyyy-mm-dd format
		'''
		return '%d-%02d-%02d' % (self.year, self.month, self.day)


	def __str__(self):
		'''
		This function returns the date provided in yyyy/mm/dd format
		'''
		return '%d/%02d/%02d' % (self.year, self.month, self.day)

		
	def __add__(self, other): 
		'''
		This function takes the date and integer, representing days, and returns the amount of days added.
		'''
		test = 1
		counter = 0
		newDay = self.day
		newMonth = self.month
		newYear = self.year
		days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
		while test == 1:
			if newMonth == 2:
				leapcheck = leap_year(newYear)
				if leapcheck == False:
					days_in_month[2] = 29
				else: 
					days_in_month[2] = 28
			newDay += other
			result = range_check(newDay, (1, days_in_month[newMonth]))
			while result == False: 
				newDay = newDay - days_in_month[newMonth]
				newMonth += 1
				if newMonth > 12:
					newYear +=1
					newMonth = 1
				result = range_check(newDay, (1, days_in_month[newMonth]))
				if result == True:
					test = 0
			else:
				test = 0
		newDate = Date(newYear,newMonth,newDay)
		return newDate
		
		
		
	def __sub__(self, other):
		'''
		This function takes a date, and either a date or integer given and subtracts it from the first date. It then returns the new date after calculations.
		'''
		test = 1
		counter = 0
		newDay = self.day
		newMonth = self.month
		newYear = self.year
		days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
		days_in_month_other = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
		if type(other) == int:
			while test == 1:
				leapcheck = leap_year(newYear)
				if leapcheck == False:
					days_in_month[2] = 29
				else:
					days_in_month[2] = 28
				newDay -= other
				result = range_check(newDay, (1, days_in_month[newMonth]))
				while result == False:
					newDay = newDay + days_in_month[newMonth]
					newMonth = newMonth - 1
					if newMonth < 1:
						newYear -= 1
						newMonth = 12
					result = range_check(newDay, (1, days_in_month[newMonth]))
					if result == True:
						test = 0
				else:
					test = 0
			newDate = Date(newYear,newMonth,newDay)
			return newDate
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
		'''
		This function takes the date that is given, and returns tomorrows date
		'''
		days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
		tomorrowsYear = self.year
		tomorrowsMonth = self.month
		tomorrowsDay = self.day
		tomorrowsDay += 1

		rangeCheck = range_check(tomorrowsDay, (1, days_in_month[self.month]))
		leapCheck = leap_year(tomorrowsYear)

		if leapCheck == False:
			days_in_month[2] = 29
		if rangeCheck == False:
			tomorrowsDay = 1
			tomorrowsMonth += 1
		if tomorrowsMonth > 12:
			tomorrowsYear += 1
			tomorrowsMonth = 1
		tomorrowsDate = Date(tomorrowsYear,tomorrowsMonth,tomorrowsDay)
		return tomorrowsDate	
	
	
	def yesterday(self):
		'''
		This function takes the date provided and returns yesterdays date.
		'''
		days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
		yesterdaysYear = self.year
		yesterdaysMonth = self.month
		yesterdaysDay = self.day
		yesterdaysDay -= 1
		
		rangeCheck = range_check(yesterdaysDay, (1, days_in_month[self.month]))
		leapCheck = leap_year(yesterdaysYear)
		if leapCheck == False:
			days_in_month[2] = 29
		
		if rangeCheck == False:
			yesterdaysMonth -=1
			yesterdaysDay = days_in_month[yesterdaysMonth]
		if yesterdaysMonth < 1:
			yesterdaysYear -=1
			yesterdaysMonth = 12
		yesterdaysDate = Date(yesterdaysYear,yesterdaysMonth,yesterdaysDay)
		return yesterdaysDate

	def day_of_week(self):
		'''
		This function takes the date that is inputted, and returns the day of the week it is in number form using the Zellers Congruence formula
		'''
		d = self.day
		m = self.month
		y = self.year

		if m == 1 or m == 2:
			m += 12
			y -= 1

		dayofWeek = (d + 13 * (m+1) // 5 + y + y //4 - y// 100 + y // 400) % 7
		actualdayofWeek = 0
 
		if dayofWeek == 0:
			actualdayofWeek = 6
		elif dayofWeek == 1:
			actualdayofWeek = 0
		elif dayofWeek == 2:
			actualdayofWeek = 1
		elif dayofWeek == 3:
			actualdayofWeek = 2
		elif dayofWeek == 4:
			actualdayofWeek = 3
		elif dayofWeek == 5:
			actualdayofWeek = 4
		elif dayofWeek == 6:
			actualdayofWeek = 5
		
		return actualdayofWeek

		
