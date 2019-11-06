# Approx 
def solution(A):
    halfLen = len(A) / 2
    if(isinstance(halfLen, float)):
        halfLen = int(halfLen) + 1

    ans = 0
    for i in range(1, halfLen):
        if(A[0:i] == A[-i:]):
            ans = i
    return ans
 
if __name__ == "__main__":
    # Task 2 Test Case, add in new array to add it to the test
    test_cases = [
        "aabcdaabc",
        "abcab",
        "aaaa"
    ]

    for case in test_cases:
        test_answer = solution(case)
        print("For the test case \"" + case + "\"\nthe answer is:", test_answer)
    
    