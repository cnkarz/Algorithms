# Calculates exact catalan number value. Most efficient among others
# O(n^2) time complexity - O(n^2/4) to be more precise
# O(n) space complexity
def getCatalanSquare(n):
    def catalan(arr, c):
        if c <= 1:
            arr.append(1)
        else:
            acc = 0
            for i in range(c):
                j = c-i-1
                if i < j:
                    acc += 2*arr[i]*arr[j]
                elif i == j:
                    acc += arr[i]*arr[i]
                else:
                    break
            arr.append(acc)
        return arr

    arr = []
    for i in range(n + 2):
        arr = catalan(arr, i)

    return arr[-1]

# Calculates exact catalan number value
# O(n^2) time complexity - O(n^2/2) to be more precise
# O(n) space complexity
def getCatalanSquare(n):
    def catalan(arr, c):
        if c <= 1:
            arr.append(1)
        else:
            arr.append(sum([arr[i]*arr[c-i-1] for i in range(c)]))
        return arr

    arr = []
    for i in range(n + 2):
        arr = catalan(arr, i)

    return arr[-1]


# Recursive solution. Worst performance.
# O(3^n) time complexity
# O(3^n) space complexity

def getCatalanSquare(n):
    def catalan(c):
        if n <= 1:
            return 1
        else:
            sum([catalan(c) * catalan(c - i - 1) for i in range(c)])

# Calculates approximate catalan number value
# O(n) time complexity
# O(1) space complexity
def getCatalanSquare(n):
    def catalan(cat):
        c = cat + 1
        arr = [1, 1]
        for i in range(c):
            if i > 1:
                num = [m for m in range(2 * i, i, -1)]
                denom = [n for n in range(i, 0, -1)]

                acc = 1
                for j in range(len(num)):
                    acc *= float(num[j]) / float(denom[j])

                arr.append(acc / (i +1))

        return int(arr[-1])

    return catalan(n)

