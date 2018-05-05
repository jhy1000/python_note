#!/usr/bin/env python
#coding=utf-8

import atexit

def clean():
    print('clean...')

def main():
    atexit.register(clean)
    exit("Failure")

if __name__ == '__main__':
    main()
