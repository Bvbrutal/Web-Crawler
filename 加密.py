# -*- coding: UTF-8 -*-
def n(t):
    e = "0123456789abcdefghijklmnopqrstuvwxyz"
    return e[t]

def r(t, e):
    return t & e

def i(t, e):
    return t | e

def o(t, e):
    return t ^ e

def a(t, e):
    return t & ~e

def s(t):
    if t == 0:
        return -1
    e = 0
    if t & 65535 == 0:
        t >>= 16
        e += 16
    if t & 255 == 0:
        t >>= 8
        e += 8
    if t & 15 == 0:
        t >>= 4
        e += 4
    if t & 3 == 0:
        t >>= 2
        e += 2
    if t & 1 == 0:
        e += 1
    return e

def c(t):
    e = 0
    while t != 0:
        t &= t - 1
        e += 1
    return e

u = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
l = "="

def f(t):
    r = ""
    for e in range(0, len(t), 3):
        n = int(t[e:e + 3], 16)
        r += u[n >> 6] + u[n & 63]
    if len(t) % 3 == 1:
        n = int(t[-1], 16)
        r += u[n << 2] + "=="
    elif len(t) % 3 == 2:
        n = int(t[-2:], 16)
        r += u[n >> 2] + u[(n & 3) << 4] + "="
    return r

def h(t):
    r = ""
    i = 0
    o = 0
    for e in t:
        a = u.find(e)
        if a < 0:
            continue
        if i == 0:
            r += n(a >> 2)
            o = 3 & a
            i = 1
        elif i == 1:
            r += n((o << 2) | (a >> 4))
            o = 15 & a
            i = 2
        elif i == 2:
            r += n(o)
            r += n(a >> 2)
            o = 3 & a
            i = 3
        else:
            r += n((o << 2) | (a >> 4))
            r += n(15 & a)
            i = 0
    if i == 1:
        r += n(o << 2)
    return r

# 示例用法
hex_string = "4C6D"
base64_encoded = f(hex_string)
print("Base64 Encoded:", base64_encoded)

base64_string = "TG1k"
hex_decoded = h(base64_string)
print("Hex Decoded:", hex_decoded)
