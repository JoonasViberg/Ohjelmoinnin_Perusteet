# Print info message “Calculate fuel consumtion.”

print ("Calculate fuel consumtion.")

# Ask “Enter travel distance(kilometers): ” and store the value to Feed variable

Feed = input("Enter travel distance(kilometers): ")

# Convert the Feed into an integer and assign it to Distance variable

Distance = int(Feed)

# Ask “Enter fuel usage(liters): ”

Feed = input("Enter fuel usage(liters): ")

# Convert the Feed into an integer and assign it to FuelUsage variable

FuelUsage = int(Feed)

# Calculate the Consumption for 100 km

Consumption = (FuelUsage / Distance) * 100

# Convert the Consumption back to an integer

Consumption = int(Consumption)

# Print “Fuel consumption is {Consumption} l per 100 km”

print (f"Fuel consumption is {Consumption} l per 100 km")



# Calculate fuel consumption.
# Enter travel distance(kilometers): 200
# Enter fuel usage(liters): 20
# Fuel consumption is 10 l per 100 km
