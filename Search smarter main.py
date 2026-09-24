#01 - binary search.py
#Topic : O(log n) and binary search
#Binary search always checks the middle and drops half the link

scores= [1, 2, 3, 4, 5, 6, 7, 8 ,9 ]

input("List: " + str(scores) +" n=9 Press Enter")
guess = input("Max checks any number to find any number in this list")
target = int(input("Pick a number from this list: "))

input("Binary search - checks the middle, drops half each round. Please Enter")
low, high=0, len(scores) - 1
steps = 0
while low <= high:
    mid = (low + high) //2
    steps += 1
    print("    round," steps, " -> checked", scores [mid])
    if scores [mid] == target:
        break
    elif scores [mid] < target:
        low= mid + 1
    else: 
      high=  mid - 1

for n , s in [(9, 4), (100, 7), (1000, 10)]:
    print("n = ", n, " max steps= "s, " ->O(log)n")

