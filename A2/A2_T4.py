# Prompt the user to insert the minutes spent on each previous topic task. 
# Calculate the sum and the average. Display those in the example program run format(Note! precision). 
# Make sure to calculate the required average for two decimal digits and later integer as rounded integer (precision 0 + type conversion)


# Program starting.
print("Program starting.")
# Estimate how many minutes you spent on programming...
print("Estimate how many minutes you spent on programming...", end="\n\n")

# A1_T1: 3
T1 = int(input("A1_T1: "))
# A1_T2: 7
T2 = int(input("A1_T2: "))
# A1_T3: 9
T3 = int(input("A1_T3: "))
# A1_T4: 8
T4 = int(input("A1_T4: "))
# A1_T5: 13
T5 = int(input("A1_T5: "))
# A1_T6: 14
T6 = int(input("A1_T6: "))
# A1_T7: 21
T7 = int(input("A1_T7: "))

# In total you spent 75 minutes on programming.
Total = T1 + T2 + T3 + T4 + T5 + T6 + T7
print(f"\nIn total you spent {Total} minutes on programming.")

# Average per task was 10.71 min and same rounded to the nearest integer 11 min.
Average = float(Total / 7)
print(f"Average per task was {round(Average, 2)} min and same rounded to the nearest integer {round(Average)} min.", end="\n\n")

# Program ending.
print("Program ending.")