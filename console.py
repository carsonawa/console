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

if (__name__ == '__main__'):
    print('''
帮助:
          
变量：
consoles\t以列表形式引入控制台日志

函数：
cout\t\t日志打印
warn\t\t警告打印
error\t\t报错打印
console\t\t打印控制台日志
consoleList\t以字符串形式返回控制台日志
writeLog\t将日志内容写入到文件里

注：如果是直接import引入，需要加“console.”
    ''')
    input('按回车继续……')
    #print("示例：")
