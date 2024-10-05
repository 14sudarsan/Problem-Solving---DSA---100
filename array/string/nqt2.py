def count_specific_day(start_day, num_days, target_day):
    # Map each day to an index
    days = {
        "sun": 0,
        "mon": 1,
        "tue": 2,
        "wed": 3,
        "thu": 4,
        "fri": 5,
        "sat": 6
    }
    
    # Get the starting index and the target day's index
    start_index = days[start_day.lower()]
    target_index = days[target_day.lower()]
    
    # Count the number of target days
    target_day_count = 0
    for day in range(num_days):  # Include num_days by using num_days + 1
        if (start_index + day) % 7 == target_index:
            target_day_count += 1
    
    return target_day_count

# Test case for counting Thursdays
start_day = "sun"
num_days = 30
target_day = "tue"
output = count_specific_day(start_day, num_days, target_day)
print(output)  # Output should be the number of Thursdays within 13 days

            
            
            