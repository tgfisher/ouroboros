"""
This block was written to illustrate that code run from withing an REPL or Jupyter
differs from running code from within a script. Please use `==` when
you wish to evaluate equality. Reserve `is` for comparing identity.
"""

tucker_says = "hi there!"
compiler_says = "hi" + " there!"
tucker_responds = "bye."

print_returns_none = print("strings can be tricky")
print("\t", tucker_says == compiler_says, "\t(tucker_says == compiler_says)")
print("\t", tucker_says is compiler_says, "\t(tucker_says is compiler_says)")

print("\t", tucker_responds == "bye.", '\t(tucker_responds == "bye.")')
print("\t", tucker_responds is "bye.", '\t(tucker_responds is "bye.")') # <-- python might warn you

another_none_return = print("there is only one `None`")

print("\t", print_returns_none is another_none_return, "(print_returns_none is another_none_return)")
print("\t", print_returns_none == another_none_return, "(print_returns_none == another_none_return)")

print("lists are tricky")
print("\t", [1] == [1], "\t([1] == [1])")
print("\t", [1] is [1], "\t([1] is [1])")

my_list = [1]
new_name_same_list = my_list
print("\t", my_list is new_name_same_list, "\t(my_list is new_name_same_list)")
print("\t", my_list is my_list.copy(), "\t(my_list is my_list.copy())")
