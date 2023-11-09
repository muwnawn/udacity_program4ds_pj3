import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter city: ")
    city = city.lower()
    if city in ['chicago','new york city', 'washington']:
        pass
    else:
        city = input("Invalid value, please enter city again: ")
        city = city.lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter month (all to apply no filter): ")
    month = month.lower()
    if month in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        pass
    else:
        month = input("Invalid value, please enter month again (all to apply no filter): ")
        month = month.lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter day of week (all to apply no filter): ")
    day = day.lower()
    if day in ['all','monday', 'tuesday','wednesday', 'thursday','friday', 'saturday', 'sunday']:
        pass
    else:
        day = input("Invalid value, please enter again day of week again (all to apply no filter): ")
        day = day.lower()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name.str.lower()
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month =  months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
    return df

def display_data(df):
    start_time = time.time()
    print('\nData descriptive statistics\n')
    print(df.describe())
    
    raw_data = input("Do you want to see 5 rows of data? (yes/no)")
    if raw_data == 'yes':
        i = 5
        print(df[:i])
        row_num = input("Do you want to see the next 5 rows of data? (yes/no)")
        while row_num == 'yes':
            i += 5
            print(df[(i-5):i])
            row_num = input("Do you want to see the next 5 rows of data? (yes/no)")
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
            
import calendar
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(calendar.month_name[(df['month'].mode()[0])],"is the most common month")

    # TO DO: display the most common day of week
    print(df['day_of_week'].mode()[0].title(),"is the most common day of week")

    # TO DO: display the most common start hour
    print(df['Start Time'].dt.hour.mode()[0],"is the most common start hour")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(df['Start Station'].mode()[0],"is the most common start station")

    # TO DO: display most commonly used end station
    print(df['End Station'].mode()[0],"is the most common end station")

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination'] = "From "+ df['Start Station']+" to "+ df['End Station']
    print(df['Combination'].mode()[0],"is the most common combination of start station and end station trip")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time is",df['Trip Duration'].sum(),"seconds")

    # TO DO: display mean travel time
    print("Mean travel time is",round(df['Trip Duration'].mean(),2),"seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print(df['Gender'].value_counts())
    else:
        print("Gender stats cannot be calculated because Gender does not appear in the dataframe")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print(df['Birth Year'].describe()[['min','50%','max']])
    else:
        print("Birth Year stats cannot be calculated because Gender does not appear in the dataframe")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        data = load_data(city, month, day)
        
        display_data(data)
        time_stats(data)
        station_stats(data)
        trip_duration_stats(data)
        user_stats(data)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
