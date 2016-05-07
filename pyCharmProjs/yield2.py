#coding=utf-8
'''
def consumer():
    while True:
        i = yield
        print i


def producer(c):
    while True:
        c.send('product')
        yield


if __name__ == '__main__':
    c = consumer()
    c.send(None)
    p = producer(c)
    p.next()
    p.next()
    p.next()
    p.next()'''

# 定义一个生成器
def generator():
    num = 0
    while True:
        num += 1
        num = yield num      # 将 i 的值返回调用者，然后暂时冻结在这里。等到调用者发出 send 或者 next 的话，再从这里复苏并将传入的值赋给 recv

        try:
            print(">>> Generator: 我收到了 %d" % num)
        except TypeError:
            print(">>> Generator: 我收到了 None, 因为 next(m) 与 m.send(None) 效果是一样的")


# 主函数
def main():
    m = generator()
    print("得到返回值: %d" % m.send(None))
    #print("得到返回值: %d" % next(m))   # 相当于 m.send(None)，第一次调用生成器
    # print("得到返回值: %d" % next(m))   # 相当于 m.send(None)
    print("得到返回值: %d" % m.send(4))
    print("得到返回值: %d" % m.send(0))

if __name__ == '__main__':
    main()