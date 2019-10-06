def addHTML_func(tag=""):
    def html_decorator(func):
        def wrapper(*args):
            return "<"+tag+">"+func(*args)+"</"+tag+">"
        return wrapper
    return html_decorator

value=input("Enter html tag: ")

@addHTML_func(value)
def get_string(str):
    return str

text = input("Write your HTML text: ")
print(get_string(text))
