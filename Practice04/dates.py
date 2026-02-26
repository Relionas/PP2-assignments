# dates.py

from datetime import datetime, timedelta
import pytz

# Example 1: Current date and time
now = datetime.now()
print("Current datetime:", now)


# Example 2: Creating a specific date
specific_date = datetime(2025, 12, 31, 23, 59)
print("Specific date:", specific_date)


# Example 3: Formatting date
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted_date)


# Example 4: Calculating time difference
future_date = datetime(2026, 1, 1)
difference = future_date - now
print("Days until 2026:", difference.days)


# Example 5: Working with timezone
timezone = pytz.timezone("Asia/Almaty")
almaty_time = datetime.now(timezone)
print("Almaty time:", almaty_time)