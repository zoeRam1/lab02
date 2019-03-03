
def find_reverse(numbers):
    numbers.reverse()
    return numbers

def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def find_sum(numbers):
    return sum(numbers)

def find_average(numbers):
    #TODO: find the average of all the numbers in the list
    return sum(numbers)/len(numbers)

def find_descending(numbers):
    # numbers.sort(reverse=True)
    return sorted(numbers, reverse=True)
    

def second_smallest(numbers):
    return sorted(set(numbers))[1] 
    

def kth_smallest(numbers, k):
    return sorted(set(numbers))[k-1] 

if __name__ == '__main__':
    # If you are testing, place your print statements here
    pass
