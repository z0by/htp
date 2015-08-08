# -*- coding: utf-8 -*-
import sys
import argparse
import random
import datetime
import data

class Person(object):
    def __init__(self, first_name, last_name, born_date, age, sex, status, job, street, hobby ):
        self.first_name = first_name
        self.last_name = last_name
        self.born_date  = born_date
        self.age = age
        self.sex = sex
        self.status = status
        self.job = job
        self.street = street
        self.hobby = hobby
        
    def __repr__(self):
	print type( self.first_name)
	print type(self.last_name)
	print type( self.born_date)
	print type(self.age)
	print type( self.sex)
	print type(self.status)
	print type(self.job)
	print type(self.street)
	print type(self.hobby)
	return ("{0}".format(self.first_name.encode('utf-8')))
        #return (u"<Person({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})>".format(self.first_name, self.last_name, self.born_date, self.age,  self.sex, self. status, self.job, self.street, self.hobby ))
    
    #def __unicode__(self):
    #    return ("<Person({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8})>".format (self.first_name, self.last_name, self.born_date.strftime("%Y-%m-%d"), self.age,  self.sex, self. status, self.job, self.street, self.hobby ))
def generate_sex(male_prcnt,female_prcnt, count):
    boolean = (True,False)
    sex = (u"Мужской", u"Женский")
    _list = []
    
    if count == 1:
	 return [random.choice(sex)]
    for i in range(int((float(male_prcnt)/100.0)*count)):
	
	_list.append(sex[0])
    for i in  range(int((float(female_prcnt)/100.0)*count)):
	_list.append(sex[1])
    random.shuffle(_list)
    return _list

def generate_date(age_min,age_max):
    today = datetime.date.today()
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    a = (today.month, today.day) < (month,day)
    year = random.randint(today.year-int(age_max) -a  ,today.year - int(age_min) - a )
    birth_date = datetime.datetime(year, month, day)
    return birth_date

def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def get_random(_list):
    return random.choice(_list).decode('utf-8')



def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--sex')
    parser.add_argument ('--age')
    parser.add_argument ('-c', '--count', type=int, default=1)
    return parser
 
 
if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
 
    
    sex_prcnt = namespace.sex.split(':')
    if len(sex_prcnt) != 2:
	raise ValueError('Need two values through ":"')
    if float(sex_prcnt[0])+float(sex_prcnt[1]) != 100:
	raise ValueError('sum of values must be 100')
    ages =  namespace.age.split(':')
    sex_list =  generate_sex(sex_prcnt[0],sex_prcnt[1], namespace.count)
    for sex in sex_list:
	born_date =  generate_date(ages[0],ages[1])
	age = calculate_age(born_date)
	job = get_random(data.JOBS)
	street = get_random(data.STREET_NAMES)
	hobby = get_random(data.HOBBIES)
	if sex ==u"Мужской":
	    first_name = get_random(data.FIRST_NAMES_MALE)
	    last_name = get_random(data.LAST_NAMES_MALE)
	    status = get_random(data.MALE_STATUS)
	else:
	    first_name = get_random(data.FIRST_NAMES_FEMALE)
	    last_name = get_random(data.LAST_NAMES_FEMALE)
	    status = get_random(data.FEMALE_STATUS)
        print  Person(first_name, last_name, born_date, age, sex, status, job, street, hobby )
