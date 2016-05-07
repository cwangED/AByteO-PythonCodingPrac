#coding=utf-8
#!/usr/bin/python
# Filename: yield1.py

def gen_seq(num):
    while True:
        num += 1
        yield num

gen1 = gen_seq(5)
print next(gen1), next(gen1), gen1.send(1)