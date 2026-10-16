"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
<<<<<<< HEAD
def get_temperatures():
    temp=[31,25,28,35,26,30,27]
    return temp
def analyze_temps(temp_list):
    average=sum(temp_list)/7
    high=max(temp_list)
    low=min(temp_list)
    return (average,high,low)
def display_analysis(avg,high,low):
    print("temperature analusis for the week:")
    print("average: %.if C"% avg)
    print("hightes: %.if C"% high)   
    print("lowest: %.if C"% low)
temp = get_temperatures()
print(temp)
result = analyze_temps(temp_list)
display_analysis(result[0],)
=======
    
>>>>>>> upstream/main
