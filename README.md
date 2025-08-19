# time-calculator-project
This is a Python project built for the [freeCodeCamp Scientific Computing with Python Certification](https://www.freecodecamp.org/learn/).
It calculates a new time by adding a duration to a given start time in 12-hour format, handling day changes and optional weekdays.

## Features
- Adds duration (hours and minutes) to a 12-hour formatted start time
- Supports optional starting day of the week, case insensitive
- Correctly handles AM/PM transitions
- Displays day of the week after calculation when provided
- Indicates if the resulting time is on the next day or multiple days later
- Returns output with exact formatting including commas, parentheses, and spacing

### Project Structure
- time_calculator_project.py: Main Python module containing the add_time function and logic
- README.md: Project documentation with usage and details
