a_list = [3,4,5,6,7,8,9,10]

iteration_count = 0

def search_func(num, input_list):
    global iteration_count
    iteration_count += 1
    list_len = len(input_list)
    len_half = int(list_len/2)
    if input_list[len_half] == num:
        return num, iteration_count
    elif input_list[len_half] > num:
        ret_val, count = search_func(num, input_list[:len_half])
        return ret_val, count
    else:
        ret_val, count = search_func(num, input_list[len_half:])
        return ret_val, count

ret_val,count = search_func(3, a_list)
print("Return value - {}, Iteration count - {}".format(ret_val, count))
