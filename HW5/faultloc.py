#!/usr/bin/env python3
# -*- coding: utf8 -*-
import sys
import subprocess
import os
import ast
import random
import astor
import math

def calculation(failcount,failline,passline):

    temp = math.pow(failcount*(failline + passline),0.5)
    if temp != 0:
        return failline / temp
    else:
        return 0

def calculate2():
    global failfilecontent, passfilecontent,failcount
    ret = []
    conbinekeys = {**failfilecontent, **failfilecontent}
    for key in failfilecontent:
        if passfilecontent.get(key) is not None:
            res = (key, calculation(failcount, failfilecontent[key], passfilecontent[key]))
        else:
            res = (key, calculation(failcount, failfilecontent[key], 0))
        ret.append(res)
    for key in passfilecontent:
        if failfilecontent.get(key) is None:
            res = (key,0.0)
            ret.append(res)
    return ret


def main():
    global passfilecontent, failfilecontent,failcount
    filelist = [] #file
    raw_filecontent = []
    passfilecontent = {}
    failfilecontent = {}
    passfilelist = []
    failfilelist = []
    passcount = 0
    failcount = 0
    finallist = []
    if len(sys.argv) < 1:
        print("You must enter enough param")
        return 0
    filename = str(sys.argv[1])
    for param in sys.argv:
        filelist.append(param)
    filelist.remove(filelist[0])
    for item in filelist:
        if "pass" in item:
            passcount = passcount+1
            passfilelist.append(item)
        if "fail" in item:
            failcount = failcount+1
            failfilelist.append(item)

    for file in passfilelist:
        f = open(file, 'r')
        raw_filecontent = f.readlines()
        for line in raw_filecontent:
            temp = line.split(":")
            firstnum = temp[0].strip()
            secondnum = temp[1].strip() #line number
            if firstnum.isdigit() == False:
                continue
            if firstnum.isdigit() == True:
                secondnum1 = int(secondnum)
                if secondnum1 not in passfilecontent:

                    passfilecontent[secondnum1] = 1
                else:
                    passfilecontent[secondnum1]+=1
    for file in failfilelist:
        f = open(file, 'r')
        raw_filecontent = f.readlines()
        for line in raw_filecontent:
            temp = line.split(":")
            firstnum = temp[0].strip()
            secondnum = temp[1].strip() #line number
            if firstnum.isdigit() == False:
                continue
            if firstnum.isdigit() == True:
                secondnum1 = int(secondnum)
                if secondnum1 not in failfilecontent:
                    failfilecontent[secondnum1] = 1
                else:
                    failfilecontent[secondnum1] = failfilecontent[secondnum1]+1

    finallist = calculate2()
    finallist.sort(key = lambda x: x[1]*10000000-x[0],reverse= True)
    finallist2 = finallist[:100]
    print(finallist2)
    
if __name__ == '__main__':
    main()