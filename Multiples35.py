

def find3and5():
    sum = 0
    for i in range(1, 1001):
        if i % 3 == 0:
          sum += i
        elif i % 5 == 0:
          sum += i     
    return sum    
 

sum = find3and5()
print(sum)
