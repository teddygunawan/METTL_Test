def solution(A):
    lowest_num = A[0]
    ans = 0
    for number in A:
        if(lowest_num > number):
            lowest_num = number 
        if(number - lowest_num > ans):
            ans = number - lowest_num
    return ans
 
if __name__ == "__main__":
    # Task 1 Test Case, add in new array to add it to the test
    test_cases = [
        [2, 3, 10, 6, 4, 8, 1],
        [7, 9, 5, 8, 3, 2],
        [7, 9, 5, 9, 2, 9]
    ]
    
    for case in test_cases:
        test_answer = solution(case)
        print("For the test case", case, "\nthe answer is:", test_answer)
    
    