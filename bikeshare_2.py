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
    print('Hello! Let\'s explore some US bikeshare data! \n')
    while True:
        try:
            city = input('Would you like to see data for Chicago, New York City, or Washington ? \n')
            if city.lower() in ('chicago', 'new york city', 'washington'):
                city = city.lower()
                break
            else:
                print('Please choose between these cities : Chicago, New York City, Washington \n')
        except ValueError:
            print('wrong value \n')
    while True:
        try:
            time = input('Would you like to filter data by month, day, both, or not at all ? Type "none" for no time filter \n')
            if time.lower() == 'both':
                while True:
                    month = input('Which month? January, February, March, April, May, June \n')
                    if month.lower() in ('january', 'february', 'march', 'april', 'may', 'june'):
                        month = month.lower()
                        while True:
                            day = input('Which day? Please between these days : all, Monday, Tuesday, Wednesday, Thursday, Saturday, Sunday \n')
                            if day.lower() in ('all','monday','tuesday','wednesday','thursday','saturday','sunday'):
                                day = day.lower()
                                break
                            else:
                                print('Please choose day like this : 0= all, 1=Sunday,2=monday,3=tuesday,... \n')
                                
                        break
                    else:
                        print('Please choose month between January, February, March, April, May, June \n')
                break
            elif time.lower() == 'month':
                while True:
                    month = input('Which month? January, February, March, April, May, June \n')
                    if month.lower() in ('january', 'february', 'march', 'april', 'may', 'june'):
                        month = month.lower()
                        day = 'all'
                        break
                    else:
                        print('Please choose month between January, February, March, April, May, June \n')			
                break
        except:
            print('error')
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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
	
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
