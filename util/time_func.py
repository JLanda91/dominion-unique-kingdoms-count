from time import perf_counter, perf_counter_ns


def __time_func_impl(perf_counter_func, f, *args, **kwargs):
    t1 = perf_counter_func()
    result = f(*args, **kwargs)
    t2 = perf_counter_func()
    return result, t2-t1


def time_func_s(f, *args, **kwargs):
    print(f"Timing function {f.__name__} in seconds.. ")
    result, dt = __time_func_impl(perf_counter, f, *args, **kwargs)
    print(f"Elapsed time in {f.__name__}: {dt} s")
    return result


def time_func_ns(f, *args, **kwargs):
    print(f"Timing function {f.__name__} in nanoseconds.. ")
    result, dt = __time_func_impl(perf_counter_ns, f, *args, **kwargs)
    print(f"Elapsed time in {f.__name__}: {dt} ns")
    return result
