#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    a1,b1,c1,a2,b2,c2 = map(int, input().split())
    d = b2*a1 - a2*b1
    dx = b2 * c1 - c2 * b1
    dy = c2 * a1 - a2 * c1

    if d != 0:
        x = dx / d
        y = dy / d
        print(x,y)
    elif dx!=0 or dy != 0:
        print("ПРямые параллельны")
    else:
        print("Прямые совпадают")
