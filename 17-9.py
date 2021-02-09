sequence = (input("Введите последовательность чисел через пробел: ").split())
number = int(input("Введите любое число: "))

def merge_sort(sequence):
    if len(sequence) < 2:
        return sequence[:]
    else:
        middle = len(sequence) // 2
        left = merge_sort(sequence[:middle])
        right = merge_sort(sequence[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

sort_seq = merge_sort(sequence)
num_seq = list(map(int, sort_seq))

def search():
    mid = len(num_seq) // 2
    low = 0
    high = len(num_seq) - 1
    while number <= num_seq[mid]:
        high = mid - 1
        mid = (low + high) // 2
    while number > (num_seq[mid+1]):
        mid += 1
    return mid

print(num_seq)
print("ID =", search())



