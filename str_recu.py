#reverse string using recursion
string = "hello"

def rev(string):
    if string == "":
        return string
    else:
        return string[-1] + rev(string[:-1])  #calls itself

print(rev(string))
