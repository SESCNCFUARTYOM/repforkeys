#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    c = int(input())
    if a+b>c and a+c>b and b+c>a:
        if a==b==c:
            print("Треугольник равносторонний")
        elif a==b or b==c or a==c:
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")
    else:
        print("Такой треугольник не существует!!!")