def add_number_x_times(num, x):

    print('Im in the function')
    
    
    for i in range(x):
        print(i)
        num += num
    
    print(num)
    return num


add_number_x_times(10, 90)
