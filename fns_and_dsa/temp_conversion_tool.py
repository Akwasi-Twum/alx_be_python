# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using the global conversion factor.
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
        
    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using the global conversion factor.
    
    Args:
        celsius (float): Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    # Prompt user for temperature input
    try:
        temperature = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return
    
    # Prompt user for unit (Celsius or Fahrenheit)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    # Perform conversion based on unit
    if unit == 'F':
        celsius = convert_to_celsius(temperature)
        print(f"{temperature:.1f}°F is {celsius:.1f}°C")
    elif unit == 'C':
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature:.1f}°C is {fahrenheit:.1f}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
