from time import ctime
cons = ''
consoles = []
ctimes = ctime().split()[3]

def times() :
    return(ctime().split()[3])

def cout(string):
    global consoles
    consoles.append(((('[' + times()) + ']') + string))
    print(((('[' + times()) + ']') + string))

def warn(string):
    global consoles
    consoles.append((((('[' + times()) + ' WARNING') + ']') + string))
    print((((('[' + times()) + ' WARNING') + ']') + string))

def error(string):
    global consoles
    consoles.append((((('[' + times()) + ' ERROR') + ']') + string))
    print((((('[' + times()) + ' ERROR') + ']') + string))

def console():
    print('\n'.join(consoles))

def consoleList():
    return('\n'.join(consoles))

def writeLog(file) :
    with open(file, "w") as f:
        f.write(consoleList())
