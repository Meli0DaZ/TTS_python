
def find_step(x,y):
    list = [x]
    cnt = 0
    n = 0
    list_temp = [x]
    while(x!=y):
        print(list)
        # print(list_temp)
        n+=1
        for i in list:
            if i == y:
                x = i
                break
        if x != y:
            cnt += 1
            for i in list_temp:
                list.append(i-1)
                list.append(i*2)
            list_temp = list[-(2**cnt):].copy()

        if n>30:
            break
    print(f'Minimum steps required: {cnt}')

    for i in range(len(list)):
        if list[i] == y:
            j = i
            break
    str = ''
    while(i>0):
        if i%2:
            j=i
            i=int((i-1)/2)
        else:
            j=i
            i=int((i-2)/2)
        if list[j] == list[i]-1:
            str = f'\t{list[i]} - 1 = {list[j]}\n' + str
        elif list[j] == list[i]*2:
            str = f'\t{list[i]} * 2 = {list[j]}\n' + str
    print(f'Operations:\n{str}')

find_step(3,15)