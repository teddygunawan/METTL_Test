import sys
def solution(A):
    ans = ""
    count = 1
    prevCharacter = A[0]
    for i in range(1, len(A)):
        if(A[i] == prevCharacter):
            count+= 1
            prevCharacter = A[i]
        else:
            if(count > 1):
                ans += prevCharacter + str(count)
            else:
                ans += prevCharacter
            count = 1
            prevCharacter = A[i]
    
    if(count > 1):
        ans += prevCharacter + str(count)
    else:
        ans += prevCharacter
        
    return ans



if __name__ == "__main__":
    # Task 3 Test Case, add in new array to add it to the test
    test_cases = [
        "aaaaabbbbcccccccdaa",
        "abcde",
        "abcccxcccddddzdddde"
    ]
    
    for case in test_cases:
        test_answer = solution(case)
        print("For the test case \"" + case + "\"\nthe answer is:", test_answer)
    
    