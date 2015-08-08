# -*- coding: utf-8 -*-
import sys
import argparse
import random
import datetime
import data
import math
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Date, MetaData, ForeignKey


Base = declarative_base()
class Person(Base):

    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    last_name = Column(String)
    first_name = Column(String)
    born_date = Column(Date)
    age =  Column(Integer)
    sex = Column(String)
    status = Column(String)
    job =  Column(String)
    street = Column(String)
    country = Column(String)
    hobby = Column(String)

    def __init__(self, last_name, first_name, born_date, age, sex, status, job,
                                                    country, street, hobby ):
        self.first_name = first_name
        self.last_name = last_name
        self.born_date  = born_date
        self.age = age
        self.sex = sex
        self.status = status
        self.job = job
        self.country = country
        self.street = street
        self.hobby = hobby

    def __repr__(self):
	return ("Фамилия: {0}, Имя: {1}, Дата рождения: {2}, Возраст: {3}, \
            Пол: {4}, Семейное положение: {5}, Работа: {6}, Страна: {7}, Адрес:\
            {8}, Хобби: {9}".format(self.last_name.encode('utf-8'),
            self.first_name.encode('utf-8'), self.born_date.strftime("%Y-%m-%d"), self.age,
            self.sex.encode('utf-8'), self.status.encode('utf-8'), self.job.encode('utf-8'),
            self.country.encode('utf-8'), self.street.encode('utf-8'), self.hobby.encode('utf-8') ))


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
    if len(_list) < count:
        for _ in range(count - len(_list)):
            _list.append(random.choice(sex))
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


def greate_db_session():
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('sqlite:///my.db', echo=True)
    metadata = Base.metadata
    metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--sex', help = 'sex of persons throuth a colon, example "70:30"', required=True)
    parser.add_argument ('--age', help = 'age of persons throuth a colon, example "70:30"', required=True)
    parser.add_argument ('--count', type=int, default=1)
    parser.add_argument ('-b', '--base', dest = "base", action='store_true', help='store result in database')
    parser.add_argument ('--countries', dest = "countries",  default='Беларусь')
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
    if len(ages) != 2:
	raise ValueError('Need two values through ":"')
    countries = namespace.countries.split(',')
    sex_list =  generate_sex(sex_prcnt[0],sex_prcnt[1], namespace.count)

    if namespace.base:
	session = greate_db_session()

    for sex in sex_list:
	born_date =  generate_date(ages[0],ages[1])
	age = calculate_age(born_date)
	job = get_random(data.JOBS)
	street = get_random(data.STREET_NAMES)
        country  = random.choice(countries).decode('utf-8')
	hobby = get_random(data.HOBBIES)
	if sex ==u"Мужской":
            first_name = get_random(data.FIRST_NAMES_MALE)
            last_name = get_random(data.LAST_NAMES_MALE)
            status = get_random(data.MALE_STATUS)
	else:
            first_name = get_random(data.FIRST_NAMES_FEMALE)
            last_name = get_random(data.LAST_NAMES_FEMALE)
            status = get_random(data.FEMALE_STATUS)
	user = Person(last_name, first_name, born_date, age, sex, status, job, country, street, hobby )
	if  namespace.base:
            session.add(user)
	else:
            print user
    if namespace.base:
	session.commit()
	session.close()

