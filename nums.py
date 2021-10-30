def find_missing_nums(nums):
    N = nums[1:-1]
    F = (N.split(','))
    i = iter(F)
    B = list(iter(lambda: int(next(i)), None))
    Max = len(B)
    I=[]
    for i in range (1, Max+1):
        for j in B:
            if i == j:
                break
        else:
            I.append(i)
    return I
nums = []
print ('Список вводится, начиная со знака [ и заканчивая знаком ], через запятую, без пробелов')
nums = input('nums = ')
print (find_missing_nums(nums))
