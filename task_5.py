def solution(A):
    # Create dictionary of numbers from 0 to N. Only the key matters here so ignore the value (0 in this case)
    numbers = list(range(1, A[1]))
    self_numbers = {key: 0 for key in numbers}

    # Loop from 0 to N, for each integer i, compute the numbers generated. 
    # After that, remove the numbers generated from the dictionary. At the end, the list of self numbers will be obtained
    for i in range(A[0], A[1]):
        generated_number = i
        for c in map(int, str(i)):
            generated_number += c
        if(generated_number in self_numbers):
            del self_numbers[generated_number]
    
    # Get all of the dictionary keys as list.
    self_numbers = list(self_numbers.keys())
    
    # Return the sum of the self_numbers list
    return sum(self_numbers)
 
if __name__ == "__main__":
    # Task 5 Test Case, add in new array to add it to the test
    test_cases = [
        [0, 100],
        [0, 5000]
    ]
    for case in test_cases:
        test_answer = solution(case)
        print("For the test case", case, "\nthe answer is:", test_answer)
    
    