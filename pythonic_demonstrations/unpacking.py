def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    print(total)

nums = [1,2,3,4,5,6]
sum_all_values(nums)
# creates a one value tuple out of a whole list
#### ^^sum_all_values(*nums)^^ = *unpacks* a list or tuple set to each individual value
#### using ** as an argument helps unpack dictionaries 