def peek(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        middle_index = (low + high) // 2

        # Check if middle_index is at the boundaries
        if middle_index == 0:
            return 0 if A[0] > A[1] else -1
        elif middle_index == len(A) - 1:
            return len(A) - 1 if A[len(A) - 1] > A[len(A) - 2] else -1

        if A[middle_index] > A[middle_index - 1] and A[middle_index] > A[middle_index + 1]:
            return middle_index
        elif A[middle_index] < A[middle_index - 1]:
            high = middle_index - 1
        elif A[middle_index] < A[middle_index + 1]:
            low = middle_index + 1

    return -1

n = int(input())
A = list(map(int, input().split()))
result = peek(A)
print(result)

