import pandas as pd
import numpy as np

# a) Create time series using datetime object in pandas indexed by timestamps
def create_datetime_series():
    print("a) Creating Time Series with Datetime Index:")
    # Creating a series with datetime index
    dates = pd.date_range(start='2024-01-01', periods=5)
    data = [10, 20, 30, 40, 50]
    series = pd.Series(data, index=dates)
    print(series)
    print("\n")
    return series

# b) Use pandas.date_range to generate a DatetimeIndex
def generate_datetime_range():
    print("b) Generating DatetimeIndex:")
    # Generate a DatetimeIndex with specified length
    date_index = pd.date_range(start='2024-01-01', periods=7, freq='D')
    print("DatetimeIndex:", date_index)
    print("\n")
    return date_index

# c) Date Range with Time Zones
def time_zone_operations():
    print("c) Time Zone Operations:")
    # Create a DatetimeIndex with a specific time zone
    ny_dates = pd.date_range(start='2024-01-01', periods=5, freq='D', tz='America/New_York')
    print("New York Dates:", ny_dates)
    
    # Convert to another time zone
    london_dates = ny_dates.tz_convert('Europe/London')
    print("Converted to London Time:", london_dates)
    
    # Localize a naive datetime to a time zone
    naive_dates = pd.date_range(start='2024-01-01', periods=5)
    localized_dates = naive_dates.tz_localize('America/New_York')
    print("Localized Dates:", localized_dates)
    print("\n")
    
    return ny_dates, london_dates

# d) Period Arithmetic
def period_operations():
    print("d) Period Arithmetic:")
    # Create a range of periods
    periods = pd.period_range(start='2024-01-01', periods=5, freq='M')
    print("Periods:", periods)
    
    # Perform period arithmetic
    print("Adding 2 to periods:", periods + 2)
    print("Subtracting 1 from periods:", periods - 1)
    
    # Create a PeriodIndex
    period_series = pd.Series(np.random.rand(5), index=periods)
    print("\nPeriod Series:")
    print(period_series)
    print("\n")
    
    return periods

# Run all functions
def main():
    create_datetime_series()
    generate_datetime_range()
    time_zone_operations()
    period_operations()

# Execute the main function
if __name__ == "__main__":
    main()
