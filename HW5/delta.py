#!/usr/bin/env python3
# -*- coding: utf8 -*-
import sys
import os
import ast
import random
import astor
systag = ""

def devide1(list1,list2):
    if(len(list2) == 1):
        return list2
    mid = (len(list2))//2
    p1 = list2[0:mid]
    p2 = list2[mid:len(list2)]
    if(convert_list_to_string_and_pass(list1+p1) == 1):
        return devide1(list1,p1)
    if(convert_list_to_string_and_pass(list1+p2) == 1):
        return devide1(list1,p2)
    return devide1(list1+p2,p1) + devide1(list1+p1,p2)

def convert_list_to_string_and_pass(num):
    global systag
    temp = [str(x) for x in num]
    temp_new =' '.join(temp)
    asas = systag + " "+temp_new
    exit = os.system(asas)
    if(exit == 256):
        exit = 1;
    return exit

def main():
    global ret, systag
    ret = []
    list1 = []
    if len(sys.argv) < 3:
        print("You must enter enough param")
        return 0
    if len(sys.argv) == 4:
        systag = sys.argv[3]
    if len(sys.argv) == 3:
        systag = sys.argv[2]
    count = int(sys.argv[1])
    print(count)
    original = [0] * count
    for i in range(0,count):
        original[i] = i;
    print(original)
    print(devide1(list1,original))

if __name__ == '__main__':
    main()