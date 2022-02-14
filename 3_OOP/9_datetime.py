#from chapter 11
import datetime


xmas2022 = datetime.date(year=2022, month=12, day=25) #creating a date object

#creating a date object that returns today
currentDate = datetime.date.today()

print(f'Xmas 2022 = {xmas2022}')
print(f'today = {currentDate}')


#creating a time delta object which is the differece betwewen two time stamps

print((xmas2022 - currentDate).days, 'days to christmas this year.')

# date time .datetime example
class_end_time = datetime.datetime(year=2022, month=2, day=8, hour =11 , minute=30) # create a datetime
currentTime = datetime.datetime.now() # get a current datetime

print(class_end_time - currentTime)  # create a time delta object
print(currentTime)





