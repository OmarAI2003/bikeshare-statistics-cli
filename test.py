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

#################################################################################################################################

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

#################################################################################################################
def time_stats(df):
    
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("the most common month in the dataset is: ",df["month"].mode()[0])

    # TO DO: display the most common day of week
    print("The most common day that people travel in it in this dataset is:",df["day_of_week"].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common hour that people start to travel in it in this dataset is:",df["hour"].mode()[0])
    
#################################################################################################################

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("the most start station people usually use is:",df["Start Station"].mode()[0])
    # TO DO: display most commonly used end station
    print("the most end station people usually use is:",df["End Station"].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df["Whole Trip"]=df["Start Station"] + '----' + df["End Station"]
    print("most travel that usually occurs is between:",df["Whole Trip"].mode()[0])

   #################################################################################################################

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time for this dataset is about:",df["Trip Duration"].sum().round())

    # TO DO: display mean travel time
    print("The average tarvel time for this dataset is about:",df["Trip Duration"].sum().round())


def user_stats(df):
    """Displays statistics on bikeshare users."""
    if "Gender" in  df.columns and "User Type" in  df.columns:
        print('\nCalculating User Stats...\n')
        start_time = time.time()
        # TO DO: Display counts of user types
        print("the sum of Users type in this dataset is :",df['User Type'].value_counts().to_frame())

        # TO DO: Display counts of gender
        print("the sum of genders type in this dataset is :",df['Gender'].value_counts().to_frame())
        # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest year a user was born on it in our dataset is:",int(df['Birth Year'].min()))
        print("The most recent year a user was born on it in our dataset is:",int(df['Birth Year'].max()))
        print("The most common year of birth for the users in our dataset is:",int(df['Birth Year'].mode()))

def display_raw_data(city):
    """
        displays raw data based on whatever the user inputs
    """
    print('\nRaw data is available to check it \n')
    df = pd.read_csv(CITY_DATA[city])
    display_data_count=0
    while True:
        display_decision=input("if you want to see the availbale raw data in scraps of 5 rows type: Yes \n").lower()
        if display_decision not in  ['yes', 'no']:
            print('That\'s invalid decision, please type yes or no')
        elif display_decision == 'yes':
            print(df.iloc[display_data_count:display_data_count+5])
            display_data_count+=5

        elif display_decision == 'no':
            print('\nFleeing...')
            break   


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city):

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
