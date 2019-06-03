
def kangaroo(A):
    v1 = 1
    v2 = 2
    x1 = A[0]
    x2 = A[0]

    for i in range(x1, len(A) - 1, v1):

        for j in range(x2, len(A) - 1, v2):
            if A[i] == A[j]:
                print(A[i], A[j])

    return A


A = list(range(0, 10001))
print("Matching Sets:")
print("---------------")
# code is probably related to big o since problem is asking about iteration rate
kangaroo(A)


