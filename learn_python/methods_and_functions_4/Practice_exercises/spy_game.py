#Spy game

#Write a function that takes in a list of integers and returns True if
#it contains 007 in order.

#Example:
#spy_game([1,2,4,0,0,7,5]) --> True
#spy_game([1,0,2,4,0,5,7]) --> True
#spy_game([1,7,2,0,4,5,0]) --> False

#One method
def spy_game2(arr):
    for index in range(len(arr)):
        if [0,0,7]==arr[index:index+3]:
            return True
    return False

print(spy_game2([1, 0, 3, 0, 6, 7]))
print(spy_game2([1, 0, 3, 0, 0, 7]))
print(spy_game2([0, 0, 7, 1, 0, 3]))
print(spy_game2([1, 0, 0, 7, 2, 3]))

#Second method - complex
# def spy_game(nums):
#     code = [0,0,7,'x']
#     [0,7,'x']
#     [7,'x']
#     ['x']     length=1
#     for num in nums:
#         if num == code[0]:
#             code.pop(0)   # code.remove(num) also works
#     return len(code) == 1

# print(spy_game([1,0,4,5,4,0,7]))