#include <stdio.h>

/* declaring the function to find the minimum */
int find_min(int array[], int length);

/* our main function */
int main(void)
{

	/* defining some arrays*/
	int myarray1[] = {5,9,10,11,4,8,6,7,3};
	int myarray2[] = {4,5,9,10,56,54};

	/* to determine the length of the arrays:
	sizeof the array divided by the size of a single element*/
	int array1_size = sizeof myarray1 / sizeof myarray1[0];
	int array2_size = sizeof myarray2 / sizeof myarray2[0];

	/* defines the minimum of each array as the integer value returned by the function */
	int min1 = find_min(myarray1, array1_size);
	int min2 = find_min(myarray2, array2_size);
	
	/* format prints the minimum values for each array */
	printf("min1: %d\n", min1);
	printf("min2: %d\n", min2);

	/* standard return 0 to end the execution */
	return 0;
}

/* our function for finding the minimum value in the array */
int find_min(int array[], int length)		// inputs of this function are the array in question + the length of that array
{
	int min;								// creates an integer variable to store the value of the min in the array
	min = array[0];							// initial definition of the minimum value as the first value in the array
	for (int i = 1; i < length; i++)		// for loop to walk through the index of each array
	{
		if (array[i] < min)					// boolean value to determine if it's smaller than the first entry of the array
		{
			min = array[i];					// refines the value of the min variable if the value is smaller than the original definition
		}
	}

	return min;								// returns the finalized value of the minimum
}