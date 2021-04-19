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
        try:
            city = input("Would you like to see the data for Chicago, New York, or Washington?\n").lower()
        except ValueError as e:
            print("Sorry i didn't understand that!")
            continue
        if city not in CITY_DATA:
            print("{} is not one of our cities!".format(city))
            continue
        else:
            break



    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']

    while True:
        try:
            month = input("Which month? January, February, March, April, May, June?\n").lower()
        except ValueErro as e:
            print("Sorry i didn't understand that!")
            continue
        if month not in months:
            print("{} not one of our months!".format(month))
            continue

        else:
            break



    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Which day? Please type your response a String (e.g.,Sunday, Monday)\n").lower()
        except ValueErro as e:
            print("Sorry i didn't understand that!")
            continue
        else:
            break


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

    # convert the Start Time coulmn to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month
    if month !='all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        #filter by month to create a new dataframe
        df = df[df['month'] == month]
    # filter by day of week
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].mode()[0]


    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]

    # extract hour from Start Time
    df['hour'] = df['Start Time'].dt.hour
    # display the most common start hour
    popular_hour = df['hour'].mode()[0]


    print("Most common month: {}".format(most_common_month))
    print("Most common day of week : {}\n".format(most_common_day_of_week))
    print("most common start hour : {}\n".format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_start = df['Start Station'].mode()[0]


    # display most commonly used end station
    most_end = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    most_frequent_station = df['combination'].mode()[0]

    print("most commonly used start station : {}\n".format(most_start))
    print("most commonly used end station : {}\n".format(most_end))
    print("most Frequent combination of start and ending station trip : {}\n".format(most_frequent_station))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()


    print("total travel time : {}\n".format(total_travel_time))
    print("mean travel time: {}\n".format(mean_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    cnt_user_types = df['User Type'].value_counts()
    # Display counts of gender
    try:
        cnt_of_gender = df['Gender'].value_counts()
        earlies_yobirth = df['Birth Year'].max()
        most_recent = df['Birth Year'].mode()[0]
        print("{}\n".format(cnt_of_gender))
        print("Most common year of birth: {}".format(most_recent))
        print("Earliest year of birth : {}".format(earlies_yobirth))
    except KeyError as e:
        print("This City has No Gender OR Birth Year!")
    # Display earliest, most recent, and most common year of birth
    print("{}\n".format(cnt_user_types))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while (view_data != 'no'):
      print(df.iloc[start_loc:start_loc+5])
      start_loc += 5
      view_data = input("Do you wish to continue?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
