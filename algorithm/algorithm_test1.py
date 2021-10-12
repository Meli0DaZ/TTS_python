# Segregate str to list
def toList(a):
    list = [str(i) for i in a]
    return list

# If given list is [1, 2, 3]
# then the subset would be [1, 2, 3, [1, 2], [2, 3], [1, 2, 3]]
def continuousSubset(li):
    if len(li)!=1:
        root = continuousSubset(li[:-1])
        op = li[-1:]
        new = root
        new.append(op)
        # print(new)
        for i in new:
            if int(i[-1]) == int(op[0])-1:
                new.append(i+op)
                # print(new)
        print(new)
        return new
    else:
        return [[li[0]]]

def finalSubset(li):
    # Remove subsets have only 1 element like ['1'], ['2']
    new_li = []
    for i in range(len(li)):
        if (len(li[i]) > 1):
            new_li.append(li[i])

    # Input [1,2] and [2,3] => Has a common element of 2 => Return TRUE
    # Input [1,2] and [3,4] => Has a common element of 2 => Return FALSE
    def checkCommon(li1,li2):
        hasCommon = False
        for i in li1:
            for j in li2:
                if set(i).intersection(set(j)):
                    hasCommon = True
                    break
        return hasCommon
    if len(new_li)!=0:
        root = finalSubset(new_li[:-1])
        op = new_li[-1:]
        new = root.copy()
        for i in new:
            if not checkCommon(i,op):
                new.append(i+op)
        print(new)
        return new
    else:
        return [[]]

def convertToNumbers(stringNumberList):
    # Example:
    # input numbers = ['1','2'], end = 6 output: [['1','2'], '3', '4', 5]
    # input numbers = ['5','6'], start = 1, end = 10  output: ['1','2', '3', '4', ['5','6'],'7','8','9']
    def fillNumber(numbers, **kwargs):
        startList = []
        endList = []
        if 'start' in kwargs.keys():
            startList = [str(x) for x in range(kwargs['start'], int(numbers[0]))]
        if 'end' in kwargs.keys():
            endList = [str(x) for x in range(int(numbers[-1]) + 1, kwargs['end'])]
        new_numbers = ["".join(numbers)]
        result = startList + new_numbers + endList
        return result

    if len(stringNumberList) == 1:
        result = fillNumber(stringNumberList[0], start=1, end=10)
        # print(stringNumberList)
        # print(result)
    elif len(stringNumberList) == 2:
        result = fillNumber(stringNumberList[0], start=1) +\
                 fillNumber(stringNumberList[1], start=int(stringNumberList[0][-1]) + 1, end=10)
        # print(stringNumberList)
        # print(result)
    else:
        new_list = []
        for i in range(len(stringNumberList)):
            if (i == 0):
                new_list.append(fillNumber(stringNumberList[i], start=1))
            elif (i == len(stringNumberList) - 1):
                new_list.append(fillNumber(stringNumberList[i], end=10))
            else:
                new_list.append(fillNumber(stringNumberList[i],
                                           start=int(stringNumberList[i - 1][-1]) + 1,
                                           end=int(stringNumberList[i + 1][0])))
        result = new_list
        # print(stringNumberList)
        # print(result)

    try:
        result = sum(result, [])
        return [int(x) for x in result]
    except:
        return [int(x) for x in result]

a='12345'
b = toList(a)

subSetContinue = continuousSubset(b)
# print(f'{subSetContinue}\n')

# Find all possible sequen with None
sequenceWithNone = finalSubset(subSetContinue)
# print(f'{sequenceWithNone}\n')
sequenceWithNone = sequenceWithNone[1:]
# print(f'{sequenceWithNone}\n\n')

for se in sequenceWithNone:
    se = convertToNumbers(se)
    print(f'{se}\n')