import cProfile, pstats, io



def profile(func):
    """
        A decorator that uses cProfile to profile a function
        Tells you more where the code needs to be optimized
        :param func: Function (no need to worry about what argument the function takes)
        :return: Whatever the function returns
    """
    def inner_func(*args, **kwargs):
        profile_obj = cProfile.Profile()
        profile_obj.enable()
        ret_val = func(*args, **kwargs)
        profile_obj.disable()
        io_stream = io.StringIO()
        sort_by = "cumulative"
        ps_obj = pstats.Stats(profile_obj, stream=io_stream).sort_stats(sort_by)
        ps_obj.print_stats()
        print(io_stream.getvalue())
        return ret_val

    return inner_func