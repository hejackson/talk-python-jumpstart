#!/usr/local/bin/python3

import datetime

def print_header():
    print('----------------------------------------')
    print('            YOUR BIRTHDAY!')
    print('----------------------------------------')


def get_birthday_from_user():
    print('Tell us when you were born: ')
    year = int(input('Year [YYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    birthday = datetime.datetime(year, month, day)
    return birthday


def compute_days_between_dates(birthday, today):
    birth_this_year = datetime.datetime(today.year, birthday.month, birthday.day)
    dt = today - birth_this_year
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print('There are {} day(s) until your birthday.'.format(-days))
    elif days > 0:
        print('There have been {} day(s) since your birthday.'.format(days))


def main():
    print_header()
    bday = get_birthday_from_user()
    now = datetime.datetime.now()
    number_of_days = compute_days_between_dates(bday, now)
    print_birthday_information(number_of_days)


main()
