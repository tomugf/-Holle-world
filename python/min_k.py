#_*_coding:utf-8_*_

import random

def select_fct(array, k):
    if len(array) <= 10:
        array.sort()
        return array[k]
    pivot = get_pivot(array)
    array_lt, array_gt, array_eq = patition_array(array, pivot)
    if k < len(array_lt):
        return select_fct(array_lt, k)
    elif k < len(array_lt) + len(array_eq):
        return array_eq[0]
    else:
        normalized_k = k - (len(array_lt) + len(array_eq))
        return select_fct(array_gt, normalized_k)

def get_pivot(array):
    subset_size = 5
    subsets = []
    num_medians = len(array) // subset_size
    if (len(array) % subset_size) > 0:
        num_medians += 1
    for i in range(num_medians):
        beg = i * subset_size
        end = min(len(array), beg+subset_size)
        subset = array[beg:end]
        subsets.append(subset)
    medians = []
    for subset in subsets:
        median = select_fct(subset, len(subset)//2)
        medians.append(median)
    pivot = select_fct(medians, len(subset)//2)
    return pivot

def patition_array(array, pivot):
    array_lt = []
    array_gt = []
    array_eq = []
    for item in array:
        if item < pivot:
            array_lt.append(item)
        elif item > pivot:
            array_gt.append(item)
        else:
            array_eq.append(item)
    return array_lt, array_gt, array_eq


def main():
    num = 20
    array = [random.randint(1,100) for x in range(num)]
    random.shuffle(array)         #random.shuffle(x[, random])：用于将一个列表中的元素打乱
    random.shuffle(array)
    k = 7
    print(sorted(array))
    kval = select_fct(array, k)
    print("第八小："+str(kval))
    sorted_array = sorted(array)
    assert sorted_array[k] == kval    #python assert断言是声明其布尔值必须为真的判定，如果发生异常就说明表达示为假。
    
if __name__ == '__main__':
    main()