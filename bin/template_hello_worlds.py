#!/usr/bin/env python

from ouroboros.utilitarian_module_name import hello_world as simple_hello
from ouroboros.sub_package.utilitarian_module_name import hello_world as meta_hello

def blow_my_mind():
    print("---------------------")
    print("running simple_hello")
    print("---------------------")
    simple_hello()
    print("\n---------------------")
    print("running meta_hello")
    print("---------------------")
    meta_hello()

if __name__ == "__main__":
    blow_my_mind()
