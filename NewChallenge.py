#Declarations
X = 5
number_array = [1,2,4,6,4,3,4,56,7,59,45,34,4,45,53,5,345,35]
number_of_repeating_numbers_allowed = 2


#Functions
##Orders an array
def ensureArrayIsInOrder(input_array):
	input_array = sorted(input_array)
	return input_array

#Removes repeating numbers using the variable set on line 4, any that go above that number are removed
def removeRepeatingNumbers(input_array):
	frequency = {}
	filtered_array = []

	for i in input_array:
		if i in frequency:
			frequency[i] += 1
		else:
			frequency[i] = 1
    	
		if frequency[i] <= number_of_repeating_numbers_allowed:
			filtered_array.append(i)
	return filtered_array

#Find the pairs of numbers that add up to the resultant
def findArrayPairResultats(input_array, resultant):
	successful_pairs = []
	for i in input_array:
		for j in input_array:
			if (i + j) == resultant:
				successful_pairs.append([i,j])
	return successful_pairs

#Print the results in a nice looking way
def printResults(initial_array, resultant , final_array):
	print("\nProgram complete using the following parameters\nInitial Array: ", number_array,"\nNumber to find pairs for:", resultant, "\n\n============================================")
	if len(final_array) == 0:
		print("Sorry, there were no pairs in the array that added up to ", resultant, ".\n\nPerhaps rerun the program with different parameters?")
	else:
		print("These are the pairs within the array that added up to ", resultant,":\n\n")
		for i in final_array:
			print(initial_array[i[0]], " + ", initial_array[i[1]], " = ", resultant," positions in the filtered array (",i[0],",",i[1],")")
		print("\n ============================================")





#Main Operations
#Sanitise the user inputs, assuming they are integers
ordered_array = ensureArrayIsInOrder(number_array)
filtered_array = removeRepeatingNumbers(ordered_array)
#Get the final pairings (an issue here is that the pairings all duplicate)
final_array = findArrayPairResultats(filtered_array, X)
#Print the results to the user
printResults(filtered_array, X, final_array)

