from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date(current_date, days_to_add):
    """
    Calculates and displays the future date after adding specified days.
    
    Args:
        current_date (datetime): The starting date
        days_to_add (int): Number of days to add
        
    Returns:
        datetime: The calculated future date
    """
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return future_date

def main():
    # Part 1: Display current date and time
    current_date = display_current_datetime()
    
    # Part 2:
from
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays and returns the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    
    Returns:
        str: Formatted current date and time
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return formatted_date

def calculate_future_date(current_date, days_to_add):
    """
    Calculates and returns the future date after adding specified days.
    
    Args:
        current_date (datetime): The starting date
        days_to_add (int): Number of days to add
        
    Returns:
        str: Formatted future date in 'YYYY-MM-DD' format
    """
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    return formatted_future_date

def main():
    # Part 1: Display and get current date and time
    formatted_current_date = display_current_datetime()
    
    # Convert formatted_current_date back to datetime for calculation
    current_date = datetime.strptime(formatted_current_date, "%Y-%m-%d %H:%M:%S")
    
    # Part 2: Calculate future date
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        if days < 0:
            print("Please enter a non-negative number of days.")
        else:
            formatted_future_date = calculate_future_date(current_date, days)
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()
