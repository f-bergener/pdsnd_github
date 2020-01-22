import time
import pandas as pd
import numpy as np

CITY_DATA = {'Chicago': 'chicago.csv',
             'New York City': 'new_york_city.csv',
             'Washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    global city, month, day
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Would you like to see data for Chicago, New York, or Washington?')
    city = input().title()
    while (city != 'Washington' and city != 'Chicago' and city != 'New York' and city != 'New York City'):
        print('Please enter a valid city name.')
        city = input().title()
    if city == 'Washington':
        print('Thank You')
    elif city == 'Chicago':
        print('Thank You')
    elif city == 'New York' or city == 'New York City':
        print('Thank You')
        city = 'New York City'
    # TO DO: get user input for month (all, january, february, ... , june)
    print('Would you like to filter the data by month, day, both, or not at all?')
    date_filter = input().lower()
    while True:
        if date_filter != 'month' and date_filter != 'day' and date_filter != 'both' and date_filter != 'not at all':
            print('Please enter a valid answer.')
            print('Would you like to filter the data by month, day, both, or not at all?')
            date_filter = input().lower()
            continue
        elif date_filter == 'month':
            print('Which month? January, February, March, April, May, or June?')
            month = input().lower()
            if month != 'january' and month != 'february' and month != 'march' and month != 'april' and month != 'may' \
                    and month != 'june':
                print('Please enter a valid month.')
                continue
            else:
                print('Thank You')
                day = 'all'
                break
        elif date_filter == 'day':
            try:
                print('Which day of the week?')
                day = input().lower()
            except:
                print('Please enter a valid day.')
                continue
            if day == 'sunday' or day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday':
                print('Thank You')
                break
            else:
                print('Please enter a valid day.')
                continue
        elif date_filter == 'both':
            print('Which month? January, February, March, April, May, or June?')
            month = input().lower()
            if month != 'january' and month != 'february' and month != 'march' and month != 'april' and month != 'may' \
                    and month != 'june':
                print('Please enter a valid month.')
                continue
            else:
                while True:
                    try:
                        print('Which day of the week?')
                        day = input().lower()
                    except:
                        print('Please enter a valid day.')
                        continue
                    if day == 'sunday' or day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday':
                        print('Thank You')
                        break
                    else:
                        print('Please enter a valid day.')
                        continue
                break
        elif date_filter == 'not at all':
            print('Thank You')
            day = 'all'
            month = 'all'
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('-' * 40)
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
    global df

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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    if month == 'all':
        print('Most Common Month: ', common_month)
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    if month == 'all':
        print('Most Common Day of the Week: ', common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print('Most Common Start Hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    df['start station'] = df['Start Station']
    common_start_station = df['start station'].mode()[0]
    print('Most Common Start Station: ', common_start_station)
    # TO DO: display most commonly used end station
    df['end station'] = df['End Station']
    common_end_station = df['end station'].mode()[0]
    print('Most Common End Station: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['station combination'] = df['start station'] + ' to ' + df['end station']
    common_station_combination = df['station combination'].mode()[0]
    print('Most Common Combination of Start Station and End Station Trip: ', common_station_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['trip duration'] = df['Trip Duration'] / 60
    total_travel_time = df['trip duration'].sum()
    print('Total Travel Time: ', total_travel_time, ' Minutes')
    # TO DO: display mean travel time
    df['trip duration'] = df['Trip Duration'] / 60
    mean_travel_time = df['trip duration'].mean()
    print('Mean Travel Time: ', mean_travel_time, ' Minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Count by User Type:')
    print(user_types)
    # TO DO: Display counts of gender
    if city == 'New York City' or city == 'Chicago':
        gender = df['Gender'].value_counts()
        print('Count by Gender:')
        print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'New York City' or city == 'Chicago':
        df['birth year'] = df['Birth Year']
        most_recent_birth_year = df['birth year'].max()
        earliest_birth_year = df['birth year'].min()
        common_birth_year = df['birth year'].mode()[0]
        print('Most Recent Birth Year: ', most_recent_birth_year)
        print('Earliest Birth Year: ', earliest_birth_year)
        print('Most Common Birth Year: ', common_birth_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
    # TO DO: Ask user if they would like to see the raw data
    print('Would you like to see the raw data?')
    answer = input().lower()
    x = df.count()
    i = 0
    while True:
        if answer != 'yes' and answer != 'no':
            print('Please enter a valid answer.')
            print('Would you like to see the raw data?')
            answer = input().lower()
            continue
        elif answer == 'yes':
            while True:
                i = i + 5
                print(df.iloc[0:i])
                print('Would you like to see five more lines of data?')
                answer = input().lower()
                if answer != 'yes' and answer != 'no':
                    print('Please enter a valid answer.')
                    print('Would you like to see five more lines of data?')
                    answer = input().lower()
                    continue
                elif answer == 'yes':
                    continue
                elif answer == 'no':
                    break
        elif answer == 'no':
            print('Thank You')
            break


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
