import time
import pandas as pd
import numpy as np

CITY_DATA = { 'ch': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'w': 'washington.csv' }
months=['january', 'february', 'march', 'april', 'may', 'june','all']
days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','All']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("Enter the city name you would like to see data for(ch,ny or w)\n").lower()
    while city not in CITY_DATA.keys():
        print("That's an invalid input")
        city=input("Enter the city name you would like to see data for(ch,ny or w)\n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input("\nTo filter data by a choosen month type a month or all for not filtring by a month:\n\njanuary\nfebruary\nmarch\napril\nmay\njune\nall\n\n").lower()
        if month in months:
            break
        else:
            print("That's an invalid month):\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("Type a weekday you want to filter the data by or the string All for no filtering by days:\n\nMonday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\nSunday\nAll\n\n").title()
        if day in days:
            break
        else:
            print("Please enter a valid day\n")
            

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df






def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.columns)    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
