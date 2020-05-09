#!/usr/bin/env python3

import argparse
import sys
from beautifultable import BeautifulTable

parser = argparse.ArgumentParser()

#### Normal Syscall Operations ####
parser.add_argument("syscall", type=str,
help="syscall you want calling convention for, use 'cheat' for generic calling convention")
parser.add_argument("-x32",
help="32 bit syscall calling convention", action="store_true")
parser.add_argument("-x64",
help="64 bit syscall calling convention", action="store_true")

args = parser.parse_args()
syscall = args.syscall

registers32 = ["eax", "ebx", "ecx", "edx", "esi", "edi", "ebp"]
registers64 = ["rax", "rdi", "rsi", "rdx", "r10", "r8", "r9"]

def cheatsheet32():
    print("\nx86 Calling Convention:\n")
    t = BeautifulTable()
    t.append_row(['eax', 'syscall/return'])
    t.append_row(['ebx', 'arg0'])
    t.append_row(['ecx', 'arg1'])
    t.append_row(['edx', 'arg2'])
    t.append_row(['esi', 'arg3'])
    t.append_row(['edi', 'arg4'])
    t.append_row(['ebp', 'arg5'])
    print(t)
    print("\n")
    return

def cheatsheet64():
    print("\nx86_64 Calling Convention:\n")
    t = BeautifulTable()
    t.append_row(['rax', 'syscall/return'])
    t.append_row(['rdi', 'arg0'])
    t.append_row(['rsi', 'arg1'])
    t.append_row(['rdx', 'arg2'])
    t.append_row(['r10', 'arg3'])
    t.append_row(['r8', 'arg4'])
    t.append_row(['r9', 'arg5'])
    print(t)
    print("\n")
    return

def parse64():
    try:
        with open("64.txt", "r") as f:
            lines = f.readlines()
    except:
        print("Unable to open 64.txt, is the file in this directory?")
        sys.exit(1)

    for x in lines:
        x = x.split("\t")
        if x[1] == syscall:
            t = BeautifulTable()
            t.append_row(['rax', x[0] + "/" + x[3]])
            counter = 4
            while counter < len(x):
                if "-" not in x[counter] and x[counter] != syscall:
                    t.append_row([registers64[counter - 3], x[counter]])
                    counter += 1
                else:
                    counter += 1
            print("\n'" + syscall + "' calling convention for x86_64 (64-bit):\n")
            print(t)
            print("\n")
            return
    
    print("'" + syscall + "' not found.\n")
    sys.exit(1)

def parse32():
    try:
        with open("32.txt", "r") as f:
            lines = f.readlines()
    except:
        print("Unable to open 32.txt, is the file in this directory?")
        sys.exit(1)

    for x in lines:
        x = x.split("\t")
        if x[1] == syscall:
            t = BeautifulTable()
            t.append_row(['eax', x[0] + "/" + x[3]])
            counter = 4
            while counter < len(x):
                if "-" not in x[counter] and x[counter] != syscall:
                    t.append_row([registers32[counter - 3], x[counter]])
                    counter += 1
                else:
                    counter += 1
            print("\n'" + syscall + "' calling convention for x86 (32-bit):\n")
            print(t)
            print("\n")
            return
    
    print("'" + syscall + "' not found.\n")
    sys.exit(1)

def main():
    if syscall.lower() == "cheat":
        if args.x64 and args.x32:
            cheatsheet32()
            cheatsheet64()
        elif args.x64:
            cheatsheet64()
        elif args.x32:
            cheatsheet32()
        else:
            print("usage: <syscall/cheat> -x32/-x64\n")
            sys.exit(1)
    else:
        if args.x64 and args.x32:
            parse32()
            parse64()
        elif args.x64:
            parse64()
        elif args.x32:
            parse32()
        else:
            print("usage: <syscall/cheat> -x32/-x64\n")
            sys.exit(1)

main()
