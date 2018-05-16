#!/usr/bin/python
#-*- coding: utf-8 -*-

import unicodedata

def no_tilde(palabra):
    s = ''.join((c for c in unicodedata.normalize('NFD', palabra) if unicodedata.category(c) != 'Mn'))
    return s
acentos = input('')
sin = no_tilde(acentos)
print(sin)
