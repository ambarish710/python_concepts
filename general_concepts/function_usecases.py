def func1():
    print("Ambarish")

func2 = func1
del func1
func2()



def funcret(num):
    if num == 0:
        return print
    if num == 1:
        return sum

print(funcret(num=1))



def execfunc(func):
    func("Ambarish")

execfunc(print)



# Decorator in python
def decor_func(input_func):
    def execution_func():
        print("Execute now")
        input_func()
        print("Done Executing")
    return execution_func

@decor_func                             # Either this
def sample_func():
    print("Ambarish understands python property decorator!")

sample_func()

#ret_func()
#ret_func = decor_func(sample_func)      # Or this





#Example 2
def decor_func(func):
    def executor(num1, num2):
        print("Started formatting the main func")
        if num2 > num1:
            func(num2, num1)
        else:
            func(num1, num2)
        print("Done formatting")
    return executor

@decor_func
def div_func(num1, num2):
    print(num1/num2)

div_func(5,10)



