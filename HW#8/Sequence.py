def solution(sequence):
    i = 0
    sequence_sort = sequence.copy()
    sequence_sort.sort()
    if len(sequence) == 1 or len(sequence) == 2:
        return True
    elif sequence_sort == sequence:
        return True
    while i < len(sequence):
        first = sequence.copy()
        del first[i]
        second = first.copy()
        second.sort()
        if first == second and len(first) == len(set(second)):
            return True
        i += 1
    else:
        return False


assert solution([1, 2, 3])
assert solution([1, 3, 2])
assert not solution([1, 2, 1, 2])
assert not solution([1, 3, 2, 1])
assert not solution([1, 2, 3, 4, 5, 3, 5, 6])
assert not solution([40, 50, 60, 10, 20, 30])
assert solution([40, 50, 60, 80, 10, 90])
