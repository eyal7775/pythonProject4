
def get_second_higgest_number_incorrect(numbers):
    firstmax = numbers[0]
    n = len(numbers)
    for i in range(n):
        if firstmax < numbers[i]:
            firstmax = numbers[i]
    secondmax = numbers[0]
    for i in range(n):
        if secondmax < numbers[i] and numbers[i] != firstmax:
            secondmax = numbers[i]
    return secondmax

def get_second_higgest_number_correct(numbers):
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

numbers = [47,47,2,6,13,7,1,19,26,37,12,4,13,6,5,45,13,7]
test = [18,20,20,5,7,-2,4,-4,-13,2,6,7,-4,2,19]
h1 = get_second_higgest_number_incorrect(numbers) # [47,47,2,6,13,7,1,19,26,37,12,4,13,6,5,45,13,7] => 47
print(h1)
h2 = get_second_higgest_number_correct(numbers) # [47,47,2,6,13,7,1,19,26,37,12,4,13,6,5,45,13,7] => 45
print(h2)
# exit(0)
h3 = get_third_higgest_number(numbers) # [47,47,2,6,13,7,1,19,26,37,12,4,13,6,5,45,13,7] => 37
print(h3)