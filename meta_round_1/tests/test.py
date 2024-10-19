def parse_input(input_string):
    # Function to parse the input from string to usable int/float values
    lines = input_string.strip().split('\n')
    deliveries = []
    # For each line, extract station and time
    for line in lines:
        station, intervals = line.split(':')
        for interval in intervals.split(','):
            start, end = map(float, interval.split('-'))
            deliveries.append((station.strip(), start, end))
    return deliveries

def can_deliver_sandwiches(deliveries):
    # Sort based on delivery start times
    deliveries.sort(key=lambda x: x[1])
    last_end_time = float('-inf')
    
    for station, start, end in deliveries:
        if start < last_end_time:
            return False  # Overlapping time window found
        last_end_time = end  # Update the last end time
    return True

# Main function to run the checks based on input
def main(input_string):
    deliveries = parse_input(input_string)
    return can_deliver_sandwiches(deliveries)

# Example input in specified string format
input_string = """
StationA: 0-1, 2-3
StationB: 1.5-2.5
StationC: 3-4
"""

with open('full_in.txt', 'r') as f:
    input_string = f.read()
    output = main(input_string)  # Expected: True
    with open('output.txt', 'w') as f:
        f.write(str(output))
