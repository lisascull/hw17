#1
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
list = [1, 2, 3, 4,]
print('Приймає:', list)
change(list)
print('Змінений:', list)
#2
def to_dict(lst):
    return {key: key for key in lst}
list = ['j', 'z', 'g']
result = to_dict(list)
print(result)
#3
def sum_range(start, end):
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))
result = sum_range(2, 13)
print(result)
result = sum_range(13, 2)
print(result)
