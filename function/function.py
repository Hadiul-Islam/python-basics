from tracemalloc import start


def add(x,y,z):
    sum = x + y + z
    print(sum)

def sub(x,y):
    sum = x - y 
    print(sum)


#binary search
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None





add(2,55 , 66)
sub(255, 5)
print(binary_search([1,3,5,7,9], 9))
