#_*_coding:utf-8_*_
#date:2019-5-20
#分治法
def separate_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left_array = array[:middle]
    right_array = array[middle:]
    left = separate_sort(left_array)
    right = separate_sort(right_array)
    return part_sort(left,right)
    
        

def part_sort(left_array, right_array):
    array = []
    i, j = 0, 0
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            array.append(left_array[i])
            i += 1
        else:
            array.append(right_array[j])
            j += 1
    while i < len(left_array):
        array.append(left_array[i])
        i += 1
    while j < len(right_array):
        array.append(right_array[j])
        j += 1
    return array


def main():
    A = [5,4,1,2,3]
    A = separate_sort(A)
    print(A)

if __name__ == "__main__":
    main()