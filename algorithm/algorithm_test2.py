x = 7
y = 91
z = y
count = 0
operator = []
while(x!=z):
    if not z%2 and x*1.5<=z:
        z/=2
        operator.append('mul')
    else:
        z += 1
        operator.append('minus')

print(operator)
for n in reversed(operator):
    print('{}: {}'.format(count,x))
    # print(operator[n])
    count+=1
    if n == 'mul':
        x*=2
    elif n == 'minus':
        x-=1
print('{}: {}'.format(count,x))