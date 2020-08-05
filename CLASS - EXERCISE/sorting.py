


def merge(left_list, right_list):
    ll_length = len(left_list)
    rl_length = len(right_list)
    sorted = []
    left_list_id = 0
    right_list_id = 0

     # start sorting
    for i in range(ll_length + rl_length):
        if left_list_id < ll_length and right_list_id < rl_length:
            if left_list(left_list_id) <= right_list(right_list_id):
                sorted.append(left_list[left_list_id])
                left_list_id =+ 1
            else:
                sorted.append(right_list[right_list_id])
                right_list_id =+ 1

    # if the sort reached the end/edge
        elif left_list_id == ll_length:
            sorted.append(right_list[right_list_id])
            right_list_id =+ 1
        elif right_list_id == rl_length:
            sorted.append(left_list[left_list_id])
            left_list_id =+ 1

    return sorted

def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums)//2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)

def main():
    random_nums = [1,2,3,5,2,31,23213,213123,231231,23]
    merge_ans = merge_sort(random_nums)
    print("MERGE SORT: ", merge_ans)


main()