def solution(A):
    number_binary = bin(A)[2:]
    ans = 0 
    count = 0
    for binary in number_binary:
        if(binary == "1"):
            if(count > ans):
                ans = count
                count = 0
        else:
            count += 1
    return ans
 
if __name__ == "__main__":
    # Task 1 Test Case, add in new array to add it to the test
    test_cases = [
        4,
        9,
        529,
        20,
        15,
        32,
        1041
    ]
    
    for case in test_cases:
        test_answer = solution(case)
        print("For the test case", case, "\nthe answer is:", test_answer)
    
    