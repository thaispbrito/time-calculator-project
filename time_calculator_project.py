def add_time(start, duration, starting_day=None):
    """
    Adds a duration time to a start time and returns the resulting time.

    Parameters:
        start (str): The starting time in 12-hour format (e.g., "3:00 PM").
        duration (str): The duration to add, in "H:MM" format (e.g., "2:30").
        starting_day (str, optional): The starting day of the week (e.g., "Monday"). Case-insensitive.

    Returns:
        str: The resulting time in 12-hour format, optionally including the new day of the week 
             and the number of days later (e.g., "5:30 PM", "2:02 PM, Tuesday", "12:03 AM, Thursday (2 days later)").

    Notes:
        - The function assumes all input times are valid.
        - It does not use any external libraries.
        - The result will indicate day transitions with "(next day)" or "(n days later)" if applicable.
    """
    # Empty list to store the output
    output = []

    # Separate the strings to manipulate them
    start_rep = start.replace(' ', ':')
    start_list = start_rep.split(':')
    duration_list = duration.split(':')

    # Step 1: Work on the final time output
    # Handle minutes + carry first
    minutes = (int(start_list[1]) + int(duration_list[1])) % 60
    carry = (int(start_list[1]) + int(duration_list[1])) // 60

    # Handle start time in 24-hour format
    if start_list[2] == 'PM':
        temp_hour = 12 if int(start_list[0]) == 12 else int(start_list[0]) + 12
    elif start_list[2] == 'AM':
        temp_hour = 0 if int(start_list[0]) == 12 else int(start_list[0])

    # Add duration time and handle overflow into the next day
    hour = temp_hour + int(duration_list[0]) + carry

    # Handle day overflow
    days = hour // 24
    hour = hour % 24  # Wrap hour into the 24-hour format

    # Handle AM/PM
    if hour >= 12:
        ending = 'PM'
    else:
        ending = 'AM'

    # Adjust back for the 12-hour clock system
    if hour > 12:
        hour -= 12  
    elif hour == 0:
        hour = 12

    # Include leading zero for minutes when applicable
    final_min = f"{minutes:02}"

    # Concatenate the final time (hour:minute AM/PM)
    if starting_day:
        final_time = f"{hour}:{final_min} {ending},"
    else:
        final_time = f"{hour}:{final_min} {ending}"

    # Append the final time to the output list
    output.append(final_time)

    # Step 2: Handle the day of the week if starting day is provided
    if starting_day:
        # Process the starting day to make sure only the first letter is capitalized
        starting_day = starting_day.capitalize()
        # Store days of the week in a list
        week_days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', \
        'Thursday', 'Friday', 'Saturday']
        
        day_index = week_days.index(starting_day) # Get the index of the input starting day
        final_day = week_days[(day_index + days) % 7]  # Wrap around if more than 7 days
        
        # Append the final day, if starting day is provided, to the output list
        output.append(final_day)

    # Step 3: Handle the message in parenthesis if the final day is not the same as starting day
    if days == 1:
        output.append('(next day)')
    elif days > 1:
        output.append(f'({days} days later)')

    # Step 4: Return the result as a string
    return ' '.join(output)

# Test case
print(add_time('11:59 PM', '24:05', 'Wednesday'))  # Expected: '12:04 AM, Friday (2 days later)'

