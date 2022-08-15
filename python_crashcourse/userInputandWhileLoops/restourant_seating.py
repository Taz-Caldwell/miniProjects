'''
The number of people eating in the users dinner group.
'''
dinning_group = input("How many people are in your dinner group? ")
dinning_group = int(dinning_group)

if dinning_group > 8:
    print(f"\nSorry, we dont have a table for {dinning_group}.\
 You will have to wait for a table.")
else:
    print(f"\nYour table for {dinning_group} is ready!")