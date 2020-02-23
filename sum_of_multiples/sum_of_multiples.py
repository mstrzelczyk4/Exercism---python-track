def sum_of_multiples(limit, multiples):
    nums = []
    for x in multiples:
        if x == 0:
            break
        i = 1
        while x * i < limit:
            nums.append(x * i)
            i += 1
    return sum(set(nums))
