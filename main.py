#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
class Stack(list):
    def push(self, x):
        return self.append(x)
#
print('НАЧАЛО ПЕРВОЙ УТИЛИТЫ:')
ob = input('Текст берется из файла?\n')
if ob == 'да':
    file = input('Название файла:\n')
    one = open(file, 'r', encoding='utf-8')
    print('\nТекст, находящийся в файле:')
    print(one.read())
    one.close()
    two = open(file, 'r', encoding='utf-8')
    string = ""
    while 1:
        line = two.readline()
        if not line: break
        string += line
    two.close()
if ob == 'нет':
    lok = input('Введите текст:')
    string=lok
    print(string)
#
import re
pattern = re.compile(r'([А-ЯA-Z]((т.п.|т.д.|пр.|г.)|[^!.\(]|\([^\)]*\))*[.!])')
#
def check(data,pat):
    stack = Stack()
    print('Текст,поделенный на строки:')
    for i, sent in enumerate(pat.findall(data)):
        print('[{}]{}'.format(i + 1, sent[0]))
        for c in sent[0]:
            if c == '{':
                stack.push(c)
            if c == '}':
                if not stack:
                    a = i+1
                    print('Ошибка! Номер строки с непарными скобками:')
                    return a
                stack.pop()
            for d in sent[0]:
                if d == '[':
                    stack.push(d)
                if d == ']':
                    if not stack:
                        a = i + 1
                        print('Ошибка! Номер строки с непарными скобками:')
                        return a
                    stack.pop()
                for k in sent[0]:
                    if k == '(':
                        stack.push(k)
                    if k == ')':
                        if not stack:
                            a = i + 1
                            print('Ошибка! Номер строки с непарными скобками:')
                            return a
                        stack.pop()
    return not stack
#
print(check(string,pattern))
print('КОНЕЦ ПЕРВОЙ УТИЛИТЫ')
#
print('НАЧАЛО ВТОРОЙ УТИЛИТЫ\n')
file = input('Название файла:\n')
three = open(file, 'r', encoding='utf-8')
print('\nТекст, находящийся в файле:')
print(three.read())
three.close()
four = open(file, 'r', encoding='utf-8')
string = ""
while 1:
    line = four.readline()
    if not line: break
    string += line
four.close()
#
import json
print('\nJSON-текст:')
print(json.dumps(string))
print('\nЗначение заданного ключа в строках:')
import re
pattern=re.compile(r'(([^{\(]|\([^\)]*\))*[}])')
for i,sent in enumerate(pattern.findall(string)):
    d = re.split(',|:|\n',sent[0])
    print(d[3])
print('КОНЕЦ ВТОРОЙ УТИЛИТЫ')

