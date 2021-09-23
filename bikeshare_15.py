import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('kindly enter the city to investigate: ').lower()
        if city in ('chicago', 'new york city', 'washington'):
            break
        print("unfortunate request! retry")
        continue
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("kindly enter month identity, or enter 'all' to print all the month: ").lower()
        if month in (
            'january',
            'february',
            'march',
            'april',
            'may',
            'june',
            'all',
        ):
            break
        print("unfortunate request! retry")
        continue
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("kindly enter day identity or enter 'all' to print all the days:").lower()
        if day in (
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
            'all',
        ):
            break

        print("unfortunate request! retry")
        continue
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
#load data file into dataframe
    df = pd.read_csv(CITY_DATA[city])

#convert the start Time to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])

#extract month and day of week from start time to create new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()
    
     # filter by month if applicable
    if month != 'all':
        
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to build the df
        df = df[df['month'] == month]

    # filter by dow
    if day != 'all':
        # filter by dow to create the new dataframe
        
        df = df[df['day_of_week'] == day.title()]

    return df

def display_rawdata(df):
    b = 0
    rawdata = input('\nWould you like to view some 1st 5 lines rawdata? input yes or no.\n').lower()
    pd.set_option('display.max_column', None)
    while True:
        if rawdata != 'yes':
            break

        print(df[b:b+5])
        continue

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month is ", df['month'].mode()[0], "\n")

    # display the most common day of week
    print("The most common day of week  is ", df['day_of_week'].mode()[0], "\n")

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('\ the most frequent start station: {}'.format(df['Start Station'].mode().values[0]))

    # display most commonly used end station

    print('\ the most frequent end station: {}'.format(df['End Station'].mode().values[0]))
    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station']+ " " + df['End Station']
    print('\ the most frequent mix of start station and end station trip is: {}'.format(df['combination'].mode().values[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("the total journey time is:", df['Trip Duration'].sum(), '\n')

    # display mean travel time

    print("the average journey time is:", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('counts of user types:\n', df['User Type'].value_counts());
    if city != 'washington':
    # Display counts of gender
        gender = df.groupby(['Gender'])['Gender'].count()
        print(gender)

    # Display earliest, most recent, and most common year of birth
        print("The earliest year of birth: {}".format(str(int(df['Birth Year'].min()))))

        print("The recent year of birth: {}".format(str(int(df['Birth Year'].max()))))

        print("The most frequent year of birth: {}".format(str(int(df['Birth Year'].mode(). values[0]))))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_rawdata(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
if __name__ == "__main__":
    main()
