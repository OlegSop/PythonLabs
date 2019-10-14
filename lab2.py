dictionary={'&': '&amp','<':'&lt','>':'&gt','*':'&lowast','~':'&tilde'}

def escape_func(str):
    ch_str = ''
    for x in str:
        if x in list(dictionary.keys()):
            ch_str = dictionary[x]
        else:
            ch_str = x
    return ch_str

def decorator(func):
    def wrapper(t):
        func(t)
        ch_str = escape_func(t)
        print("Escape HTML tag: {}".format(ch_str))
    return wrapper

@decorator
def print_string(str):
    print("Your HTML tag: {}".format(str))


while True:
    Tag = input("Write a HTML tag: ")
    if(Tag != "pyEnd"):
        print_string(Tag)
    else: break