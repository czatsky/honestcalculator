msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [0,1,2,3,4,5,6,7,8,9,"Are you sure? It is only one digit! (y / n)","Don't be silly! It's just one number! Add to the memory? (y / n)","Last chance! Do you really want to embarrass yourself? (y / n)"]

def is_one_digit(v):
    if v == int(v):
        if v >- 10 and v < 10:
            return True
        else:
            return False

def check(v1,v2,v3):
    msg = ""
    if is_one_digit(v1) == True and is_one_digit(v2) == True:
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 =="*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    return msg

memory = 0
while True:
    print(msg_0)
    x,oper,y = input().split()
    if oper != '*' and oper != '+' and oper != '-' and oper != '/':
        print(msg_2)
    else:
        if x == 'M':
            x = memory
        if y == 'M':
            y = memory
        try:
            x1 = float(x)
            y1 = float(y)
            print(check(x1, y1, oper))
            if oper == '*':
                a = (x1 * y1)
                print(a)
            if oper == '+':
                a = (x1 + y1)
                print(a)
            if oper == '-':
                a = (x1 - y1)
                print(a)
            try:
                if oper == '/':
                    a = (x1 / y1)
                    print(a)
                v = (input(msg_4))
                if is_one_digit(a) == True:
                    if v == 'y':
                        msg_index = 10
                        while True:
                            v3 = (input(msg_[msg_index]))
                            if v3 == 'y':
                                if msg_index < 12:
                                    msg_index = msg_index + 1
                                    if msg_index == 12:
                                        memory = a
                                else:
                                    # memory = 0
                                    break
                            elif v3 == 'n':
                                # memory = 0
                                break
                else:
                    if v == 'y':
                        memory = a
                v2 = (input(msg_5))
                # print(memory)
                if v2 == 'n':
                    break
            except ZeroDivisionError:
                print(msg_3)
        except ValueError:
            print(msg_1)
