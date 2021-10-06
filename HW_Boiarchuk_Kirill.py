import time


# Todo Ex: 1
#  Напишите декоратор, замеряющий время выполнения функции.
#  Декоратор должен вывести на экран время выполнения задекорированной функции


def timer(function):
    def tmp(*args, **kwargs):
        t = time.time()
        res = function(*args, **kwargs)
        print("Function execution time: %f" % (time.time() - t))
        return res

    return tmp


@timer
def user_addition(data1, data2):  # the function takes 2 arguments
    # below if both arguments are of numb types, return their multiply
    if isinstance(data2, (int, float)) and isinstance(data1, (int, float)) \
            or isinstance(data2, (float, int)) and isinstance(data1, (int, float)):
        return data1 * data2
    if isinstance(data1, str) and isinstance(data2, str):  # if to strings, concatenate into one string and return
        return data1 + data2
    if isinstance(data1,
                  str) and data2 is not str:  # if the first line is, and the second is not, return a dictionary,
        return {data1: data2}
    else:  # return a tuple of arguments
        return data1, data2


data = user_addition(data1=9, data2=8.7)
print("Ex2 -->", data)
