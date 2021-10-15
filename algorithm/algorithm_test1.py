# Turn input string into list.
# Input: '123' => result: ['1', '2', '3']
def toList(li):
    return [str(i) for i in li]

# For a given list of [1, 2, 3]
# the new list with subsets would be    [['1'], ['2'], ['3'],
#                                        ['1', '2'], ['2', '3'],
#                                        ['1', '2', '3']]
def continuousSubset(li):
    result = []
    for a in li:
        result.append([a])
        if len(result)>1:
            for b in result:
                if int(b[-1]) == int(a)-1:
                    result.append(b+[a])
    return result

# Remove subsets have only 1 element like ['1'], ['2']
def removeSingle(li):
    result = []
    for i in range(len(li)):
        if (len(li[i]) > 1):
            result.append(li[i])
    return result

# Check within 2 set if they have commen element, if they do => return True
def checkCommon(li1, li2):
    common = False
    for i in li1:
        for j in li2:
            if set(i).intersection(set(j)):
                common = True
                break
        if common:
            break
    return common

# Group subsets that don't have common element
# Subset1 ['1', '2'] and Subset2 ['3', '4'] => Result [[], ['1', '2'], ['3', '4'], [['1', '2'], ['3', '4']]]
# Subset1 ['1', '2'] and Subset3 ['2', '3'] => Result [[], ['1', '2'], ['2', '3']]
def stackSubset(li):
    li = removeSingle(li)
    if len(li)!=0:
        op = li[-1:]
        base = stackSubset(li[:-1])
        result = base.copy()
        for i in base:
            if not checkCommon(i,op):
                # print(i+op)
                result.append(i+op)
                # print(result)
    else:
        return [[]]
    return result

# Fill the subset with the missing number
# Subset: ['3', '4'] => Result: ['1', '2', '34', '5', '6', '7', '8', '9']
def fillNumStr(strLi,**kwargs):
    startLi = []
    endLi = []
    if 'start' in kwargs:
        startLi = [str(i) for i in range(kwargs['start'], int(strLi[0]))]
    if 'end' in kwargs:
        endLi = [str(j) for j in range(int(strLi[-1]) + 1, kwargs['end'])]
    num = [''.join(strLi)]
    return startLi+num+endLi

# Elements in list are now string type data.
# They need to all be converted to int type data for the next step.
# Every subsets will be handled individually.
# First, fill the each subset with the missing number.
# Then, convert each element of every subset's new list to int type data.
def strToInt(strLi):
    result = []
    if len(strLi) == 1:
        result = fillNumStr(strLi[0], start=1, end=10)
    elif len(strLi) == 2:
        result += fillNumStr(strLi[0], start=1)
        result += fillNumStr(strLi[1], start=int(strLi[0][-1]) + 1, end=10)
    elif len(strLi) >=3:
        for i in range(len(strLi)):
            if i == 0:
                result+= fillNumStr(strLi[i], start=1)
            elif i == len(strLi)-1:
                result+= fillNumStr(strLi[i], end=10)
            else:
                result+= fillNumStr(strLi[i], start=int(strLi[i - 1][-1]) + 1, end=int(strLi[i + 1][0]))

    return [int(x) for x in result]

# Create a string of numbers, '+', '-', and '=' to print out.
def resultStr(numLi, minusPosList, target):
    result = str(numLi[0])
    for i in range(1, len(numLi)):
        if i in minusPosList:
            result+= ' - ' + str(numLi[i])
        else:
            result+= ' + ' + str(numLi[i])
        if i == len(numLi)-1:
            result+= ' = ' + str(target)
    return result

# Find all subset within the input that have the sum = target and return a list of sets of the numbers' position
# Input: [1,2,3,4,5,6,7,8,9] and target = 13 => result =    [[0, 1, 2, 3], [0, 1, 6], [0, 2, 5],
#                                                            [0, 3, 4], [1, 2, 4], [2, 6], [3, 5]]
def findMinusPos(numLi, target, result = [], minusPos = [], recursiveIndex = 1):
    if not minusPos:
        minusSet = []
    else:
        minusSet = [numLi[x] for x in minusPos]
    s = sum(minusSet)

    # We need to check whether the numbers' sum is = or > than the target
    # If the sum is = target then add the lists of position the the result
    # If the sum is < target, continue to the next recursive loop
    # If the sum is >= target, end current recursive loop and go back to the previous one.
    if s == target:
        result.append(minusPos)
    if s >= target:
        return  # Return nothing to end the current recursive loop

    # Everytime the loop starts in the recursive loop, the start of the 'for' loop increase by 1 and add a new minus position to the minus index list.
    # If the sum has yet to reach target, minus position list will continue to add the next number's position (from the number list).
    # If the sum is >= target, the last number's position in the minus position list will be replaced by the next one in the number list,
    # and the process repeats until the end of the loop, then go back to the 'for' loop of the previous recursive loop.
    for i in range(recursiveIndex, len(numLi)):
        newMinusIndex = i
        recursiveIndex += 1
        findMinusPos(numLi, target, result, minusPos + [newMinusIndex], recursiveIndex)
    return result

# When adding '-' or '+' or nothing, first we need to get all the groups of number from the given string.
# Then, determines whether to add '+' or '-'.
# By defaul, we will add '+' to before all numbers (except for the 1st one).
# After that, we check to see if the value of the result (the sum of the numbers) = target.
# If the result is < target => discard it;
# If the result is = target => print it out;
# If the result is > target => check to see if we can change '+' to '-' to reduce the value,
#                               If we can, print it out;
#                               If we can't, discard it.
def solution(numbers, target):
    var = 0
    # Find all continuous subsets and add them to the lists individually.
    subsetsList = continuousSubset(toList(numbers))

    # Removes all single elements (['1'], ['2'], ...), only keep elements like ['1', '2'] or ['1', '2', '3'],
    # and group the subsets that don't have common elements together.
    # And remove the 1st element since it's empty [] (it's was created for the purpose of the program)
    stackedSubsetsList = stackSubset(subsetsList)[1:]
    stackedSubsetsList.append(toList(numbers))

    for set in stackedSubsetsList:
        set = strToInt(set)
        
        if sum(set) == target:
            var += 1
            print(f'{var}:\t{resultStr(set, [], target)}')
        elif sum(set) < target:
            continue

        # When changing from '+' to '-', we need to decrease the value by 2*numbers.
        # Example: 1+2+3+4+5=15 and 1+2+3+4-5=5.
        # The difference before and after changing '+5' into '-5' is 10=2*5
        else:
            difference = abs(sum(set)-target)
            minusPosList = findMinusPos([i*2 for i in set], difference, [])
            if minusPosList:
                for minusPos in minusPosList:
                    var += 1
                    print(f'{var}:\t{resultStr(set, minusPos, target)}')

if __name__ == '__main__':
    test = '123456789'
    solution(test, 100)