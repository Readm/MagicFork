#! /usr/bin/python
# coding:utf-8
import magicfork

a = 'a'
b = 'b'
if magicfork.magicfork():
    print a
    a = raw_input('a?')
    print 'a:', a
else:
    print b
    b = raw_input('b?')
    print 'b:', b
