# def arg_func(some_argument, *args=[], **kwargs={}):
#     pass


#-- *args -- Arguments #
def arg_func(fixed_param, *args):
    ret_val = 0
    print(fixed_param)
    for argument in args:
        ret_val += argument
    return ret_val

print(arg_func("Addition of all numbers",1,2,3,4,5))

print("\n")

# -- **kargs -- Keyword Arguments#
def kwarg_func(fixed_param, **kwargs):
    print(fixed_param)
    for keywrd, argumnt in kwargs.items():
        print("{} - {}".format(keywrd, argumnt))

kwarg_func(fixed_param="Here are all the kwarg arguments --",
           name="Ambarish",
           lastname="Pandharikar",
           dog="Joey",
           brother="Hrishi")


# -- *args and **kargs together -- Arguments and Keyword Arguments #
def combined_func(some_arg, *args, **kwargs):
    print(some_arg)
    for arg in args:
        print(arg)
    for keyword, argument in kwargs.items():
        print("{} - {}".format(keyword, argument))

combined_func("Here are the args and kwargs -- ",
              "arg1",
              "arg2",
              "arg3",
              name="Ambarish",
              lastname="Pandharikar",
              dog="Joey",
              brother="Hrishi")