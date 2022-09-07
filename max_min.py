
def get_first_higgest_number(numbers):
    n = len(numbers)
    if n >= 1:
        firstmax = numbers[0]
        for i in range(1, n):
            if numbers[i] > firstmax:
                firstmax = numbers[i]
        return firstmax
    else:
        raise Exception("the size list smaller from 1")

def get_first_lowest_number(numbers):
    n = len(numbers)
    if n >= 1:
        firstmin = numbers[0]
        for i in range(1, n):
            if numbers[i] < firstmin:
                firstmin = numbers[i]
        return firstmin
    else:
        raise Exception("the size list smaller from 1")

def get_second_higgest_number(numbers):
    n = len(numbers)
    if n >= 2:
        firstmax = max(numbers[0], numbers[1])
        secondmax = min(numbers[0], numbers[1])
        for i in range(2, n):
            if numbers[i] > firstmax:
                secondmax = firstmax
                firstmax = numbers[i]
            elif numbers[i] > secondmax and firstmax != numbers[i]:
                secondmax = numbers[i]
            elif firstmax == secondmax and secondmax != numbers[i]:
                secondmax = numbers[i]
        return secondmax
    else:
        raise Exception("the size list smaller from 2")

def get_second_lowest_number(numbers):
    n = len(numbers)
    if n >= 2:
        firstmin = min(numbers[0], numbers[1])
        secondmin = max(numbers[0], numbers[1])
        for i in range(2, n):
            if numbers[i] < firstmin:
                secondmin = firstmin
                firstmin = numbers[i]
            elif numbers[i] < secondmin and firstmin != numbers[i]:
                secondmin = numbers[i]
            elif firstmin == secondmin and secondmin != numbers[i]:
                secondmin = numbers[i]
        return secondmin
    else:
        raise Exception("the size list smaller from 2")

def get_third_higgest_number(numbers):
    n = len(numbers)
    if n >= 3:
        firstthree = numbers[:3]
        firstmax = max(firstthree)
        firstthree.remove(firstmax)
        secondmax = max(firstthree)
        thirdmax = min(firstthree)
        del firstthree
        for i in range(3, n):
            if firstmax == secondmax and secondmax != numbers[i] and numbers[i] > thirdmax:
                secondmax = numbers[i]
            elif secondmax == thirdmax and thirdmax != numbers[i]:
                thirdmax = numbers[i]
            elif numbers[i] > firstmax:
                thirdmax = secondmax
                secondmax = firstmax
                firstmax = numbers[i]
            elif numbers[i] > secondmax and firstmax != numbers[i]:
                thirdmax = secondmax
                secondmax = numbers[i]
            elif numbers[i] > thirdmax and secondmax != numbers[i]:
                thirdmax = numbers[i]
        return thirdmax
    else:
        raise Exception("the size list smaller from 3")

def get_third_lowest_number(numbers):
    n = len(numbers)
    if n >= 3:
        firstthree = numbers[:3]
        firstmin = min(firstthree)
        firstthree.remove(firstmin)
        secondmin = min(firstthree)
        thirdmin = max(firstthree)
        del firstthree
        for i in range(3, n):
            if firstmin == secondmin and secondmin != numbers[i] and numbers[i] < thirdmin:
                secondmin = numbers[i]
            elif secondmin == thirdmin and thirdmin != numbers[i]:
                thirdmin = numbers[i]
            elif numbers[i] < firstmin:
                thirdmin = secondmin
                secondmin = firstmin
                firstmin = numbers[i]
            elif numbers[i] < secondmin and firstmin != numbers[i]:
                thirdmin = secondmin
                secondmin = numbers[i]
            elif numbers[i] < thirdmin and secondmin != numbers[i]:
                thirdmin = numbers[i]
        return thirdmin
    else:
        raise Exception("the size list smaller from 3")

numbers = [8,8,1,19,26,37,12,4,13,6,5,45,13,7]
firstmax = get_first_higgest_number(numbers) # [1,19,26,37,12,4,13,6,5,45,13,7] => 45
print(firstmax)
firstmin = get_first_lowest_number(numbers) # [1,19,26,37,12,4,13,6,5,45,13,7] => 1
print(firstmin)
secondmax = get_second_higgest_number(numbers) # [1,19,26,37,12,4,13,6,5,45,13,7] => 37
print(secondmax)
secondmin = get_second_lowest_number(numbers) # [1,19,26,37,12,4,13,6,5,45,13,7] => 4
print(secondmin)
thirdmax = get_third_higgest_number(numbers) # [1,19,26,37,12,4,13,6,5,45,13,7] => 26
print(thirdmax)
thirdmin = get_third_lowest_number(numbers) # [1,19,26,37,12,4,13,6,5,45,13,7] => 5
print(thirdmin)
