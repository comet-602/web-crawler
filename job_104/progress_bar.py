# def view_bar(num, total):
#     rate = float(num) / float(total)
#     rate_num = int(rate * 100)
#     r = '\r[%s%s]%d%%' % ("="*rate_num, " "*(100-rate_num), rate_num)
#     print(r,end='\0')
# import time
# for i in range(101):
#     time.sleep(0.1)
#     view_bar(i , 100)

import sys
def view_bar(num, total):
    x=[]
    for num in range(21):
        rate = float(num) / float(total)
        rate_num = int(rate * 20)
        r = '\r%d%%  [（ﾟДﾟ）σ''%s%s' % (5 * rate_num, "弌" * rate_num, "⊃" + " " * (20 - rate_num))
        time.sleep(0.2)

        t=sys.stdout.write(r)
        t=sys.stdout.flush()
        x.append(r)

    return print(t)
import time

if __name__ == '__main__':
    view_bar(1,20)
