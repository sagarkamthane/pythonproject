def convert_to_list(getdata):
    def wrapper():
        result = getdata()
        result = list(result)
        return result, type(result)
    return wrapper()


@convert_to_list
def getdata():
    a = 1, 2, 3, 4, 5
    return a

print(getdata)