numbers = list(map(int, input().split()))

for i in range(0, len(numbers)):
    if numbers[i] <= numbers[i - 1]:
        print("NO")
        break
else:
    print("YES")    
