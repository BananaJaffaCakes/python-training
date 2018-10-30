import datetime

def print_header():
    print('-----------------')
    print('  BIRTHDAY APP')
    print('-----------------')
    print()
    print('This app will calculate the difference in days between your birthday and today this year.')
    print()


def get_birthday():
    print('Please provide your birthday as follows,')
    b_year = int(input('Year [YYYY]: '))
    b_month = int(input('Month [MM]: '))
    b_day = int(input('Day [DD]: '))

    b_date = datetime.date(b_year, b_month, b_day)
    print('You have provided a birthday of {}'.format(b_date))

    return b_date


def calculate_day_diff(user_date, today_date):
    user_date_thisyear = datetime.date(today_date.year, user_date.month, user_date.day)

    datedelta = user_date_thisyear - today_date
    return datedelta.days


def print_day_diff_message(birthday):
    print()
    if birthday > 0:
        print('Your birthday is in {} days'.format(birthday))
    elif birthday < 0:
        print('Your birthday was {} days back'.format(birthday))
    else:
        print('Congrats, Happy Birthday!')


def main():
    print_header()

    user_birthday = get_birthday()
    today = datetime.date.today()
    
    day_diff = calculate_day_diff(user_birthday, today)
    
    print_day_diff_message(day_diff)

    print()
    print('Thank you for using the Birthday App, now exiting!')


main()