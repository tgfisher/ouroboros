# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py,md
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Python and IPython Introductory Reference
#
# # Table of Contents
# 1. [IPython Extensions](#Ipython-Extensions) - tools to enhance your Jupyter/IPython experience.
# 1. [Importing](#Importing) - don't write all your code yourself, usually someone else has a faster more robust tool (e.g. numpy).
# 1. [Native Python Concepts](#Basic-Python-Types-and-Concepts)
#     1. [Numeric Types](#Numeric-Types-(int,-scalars-of-various-types-non-exhaustive))
#     1. [Null Type](#Null-Type-(None)) - nothing is its own thing.
#     1. [Text Type](#Text-Type-(Strings))
#         1. [Strings Can Do Things To Themselves...what is an 'object' anyway?](#Strings-also-have-a-bunch-of-things-that-they-can-"do"-to-themselves...What-is-an-'object'-anyway?)
#     1. [Logical Types](#Logical-Types-(True,-False,-bool))
#         1. [Equality vs. Identity](#Equality-vs.-Identity) - when are things the same?
#         1. [Using Logicals with'if' and 'while'](#Using-Logicals-with-if-and-while) - Simple [control flow][ln_control_flow_docs].
#     1. [Sequence (list, tuple, range)](#Sequence-(list,-tuple,-range)) - useful for holding multiples of types from above.
#         1. [Not all sequences can be altered](#Not-all-sequences-can-be-altered) - mutable? immutable?
#         1. ['if' and 'while' with sequences](#if-and-while-with-sequences) - more control flow.
#         1. ['for' Looping with sequences](#Looping-with-sequences) - do a thing multiple times.
#     1. [Defining new functions in python](#Defining-new-functions-in-python)
# 1. [Numpy](#Numpy)
#     1. [Defining new data arrays](#Defining-New-Data-Arrays)
#     1. [Basic 'np.ndarray()' properties](#Basic-'ndarray'-properties)
#     1. [ndarray Methods](#ndarray-methods)
#         1. ['axis' parameter](#'axis'-parameter)
#     1. [Array multiplication](#Array-multiplication)
#         1. [Matrix 'powers', beware!](#Matrix-'powers',-beware!) -- what does it mean to take a matrix to a power?
#     1. [Element-wise Multiplication](#Element-wise-Multiplication)
#     1. [Broadcasting](#Broadcasting) - simple operations between mismatched dimensions (e.g. `vector * scalar`).
#     1. [Indexing](#indexing)
#         1. [Masking](#Masking)
#     1. [Reshape arrays](#Reshape-np.arrays)
# 1. [Plotting with matplotlib.pyplot](#Plotting-with-matplotlib.pyplot)
# ---
# ---
#
# [ln_control_flow_docs]: https://docs.python.org/3/tutorial/controlflow.html

# # Ipython Extensions
#
# Primarily, **ipython** is a command line tool `$ ipython # rather than
# python` that has many nice default features. IPython also encompasses the
# **jupyter** project (this notebook is running in `jupyter notebook`). As a
# result many of the very nice [**ipython extensions**][ln_ipe] are helpful in jupyter.
#
# ```python
# # %load_ext <extension_name> # makes the extension available
# ```
#
#
# ---
#
# `autoreload` is one of the most useful extensions for working local packages.
# The `autoreload 2` mode means that your imported packages will be
# refreshed from source whenever a cell is run. If your notebook references
# modules that are changing (e.g. you are developing a function) you need to
# use this extension for jupyter to utilize the most recent save point. 
# Without this extension you would have to define all custom code
# inside the notebook, or restart the kernel and import (again and again) every time you
# alter the imported code.
#
# [ln_ipe]: https://ipython.readthedocs.io/en/stable/config/extensions/index.html

# %load_ext autoreload
# %autoreload 2

# # Importing
#
# With **pip** we decide
# which tools we'd like in our "workshop", but it is `import`-ing that spins
# the tools up in the current working environment.
#
# When you import you reference **packages** and **modules**. 
# In python **packages** contain **modules** (files with the `.py` extension).
# Modules are composed of **functions** and **classes**.
#
# ```python
# # example imports
# import package # simple import
# import long_package_name as cute_name # import and rename for convenience
# from another_package.supermodule import submodule as sm # a module, not the whole package
# from final_example_package import module1, module2 # grab a few modules at once
# ```
# ---
# Please be reasonable and consistent when you customize and abbreviate in import
# statements... 
#
# <div align="center">
# <img src="./media/import_alignment_theo_oneill.jpeg" width="300" height="300" title="Found on twitter by Theo ONeill"/>
# </div>

# + id="wuc2lmzEZzoW"
import os
import sys

import numpy as np 
import numpy.random as npr
import matplotlib.pyplot as plt

from ouroboros.utilitarian_module_name import twoDvectors as tdvec_plot # <-- single 'function' import example
# -

print(sys.executable, "<-- The python associated with this kernel.")

# # Basic Python Types and Concepts
# ---
# ---
#
# We can't cover all python types, but this section provides a tour of the key
# players. If all this is new to you and you'd like pointers for learning coding
# basics, please let us know. We are happy to help. 
#
# Numeric, Logic, Null, Text, Sequence are all families of default types in
# python. As we learn about these types we will also show how they interact with
# common control flow operators like `if`, `for`, and `while`.
#
# Run the cells below each titled-block to experience them.
#
#
# ## Numeric Types (int, scalars of various types _non-exhaustive_)
#
# **print()** is a common way to expose variables to the user.
#

integer_var = 12
float_var = 12.0
complex_var = 3+2j
print(integer_var)
print(float_var)
print(complex_var)

# ## Null Type (None)

simple_none_val = None
print_none_val = print("print is a function that doesn't return a value?")
print(simple_none_val)
print(print_none_val, "<-- yep, I guess so. Any function w/o a `return` will 'return' None.")

# ## Text Type (Strings)
# The **"f" string** can be used to evaluate little bits of code inside "\{ \}"
# withing the string. 
#
# ```python
# print(f"<some string>{<some_code_to_evaluate>}<more string>")`
# ```

# +
numbers_string_var = f"my integer: {integer_var}\nmy float: {float_var}\nmy complex: {complex_var}"

getting_a_bit_extra = (
    numbers_string_var +
    f"\nDon't know why you'd want this, but here is a sum: {integer_var + float_var + complex_var}"
) # using () to split things across lines is nice for readability

print(numbers_string_var)
print("\n\t-----Getting Extra Below-----\n")
print(getting_a_bit_extra)
print("\t\t\t\t\t\t\t^ Interesting to see what type was inherited (complex).")

# + [markdown] tags=[]
# ### Strings also have a bunch of things that they can "do" to themselves...What is an 'object' anyway?
# ---
# _This is a good time for a small aside..._ in the cell below we will show you
# examples where a string is utilized as an 'object'.
#
# _What is an object?_ You may have heard that Python is an "object oriented"
# language. You might even hear people bashing Matlab because it isn't. What does
# it mean to be object oriented?
#
# Briefly, an object can "do" things and keep track of things related to itself.
# For example, we can model a bouncing ball in (1) a 'functional' way or (2) an
# 'object oriented' way:
#
# 1. We can have a variable holding the height of a ball, and a function taking
#    in the bounciness of the ball and "bouncing physics" in order to model a
#    bounce.
#
# ```python
# start_height = 10 # feet
# start_velocity = 0 # meters/sec
# bouncyness = .9 # rebound efficiency (out of 1)
# height_over_time = bounce_physics(start_height, start_velocity, bouncyness)
# ```
#
# 1. We can write a ball 'object' that holds all of its own information.
#
# ```python
# start_height = 10
# ball.set_bouncyness(.9)
# ball.drop_from_ft(10)
# height_over_time = ball.bounce_from(start_height)
# ```
#
# The key is that each thing in python is an 'object' and can have built in
# 'methods' to alter itself or hold functions to alter other things.
#
# _A note on the Matlab-Python debate: object oriented code can be written in
# Matlab, and many people write 'functional' mega-scripts/notebooks in python 
# anyway, so... you decide._
# -

ugly_sentence = "U.g.L.y._YoU_ainT_gOT_nO_AliBy!"
print(ugly_sentence.split("_"))

print(ugly_sentence)
print(" ".join(ugly_sentence.split("_")))

pretty_sentence = " ".join(ugly_sentence.split("_")).capitalize()
print(pretty_sentence)

# ## Logical Types (True, False, bool)
#
# Logical types are about "yes"/"no", "true"/"false", or "hide"/"show". 

true_var = True
false_var = False
print(true_var)
print(false_var)

# +
two = 2
too = 2.0

print("----Equality----")
print(two == too)
print(two != too)
print("----Identity----")
print(two is too)
print(two is not too)
print("\nO_o ... wut?")
# -

# ### Equality vs. Identity 
# --- 
# When we are asking if something "is the same as
# something else" what do we mean?
#
# Variables are stored in memory on your computer. The `is` operator tells us if
# two variables reference the same place in memory, a.k.a. they are just two
# names for the 'same thing'. The `==` operator asks if the two things are
# equivalent. One apple might look the same, taste the same, and have the same
# effect, but they don't share the same space.
#
# Equality has a few subtleties:
# 1. Numeric variables (as shown above).
# 1. Strings.
# 2. There is only one "None".
# 3. Two identical lists don't necessarily share the same space.

# +
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
# -

print("-------Run File-------")
# %run ../bin/wish_you_knew.py

scary_file = "../bin/wish_you_knew.py"
print("-------Show File Contents-------")
with open(scary_file, "r") as omg:
    file_by_line = omg.read()
print(file_by_line)


# ### Using Logicals with `if` and `while`
# ---
# `if/elif/else` and `while` are two 'control flow' tools in python. 
#
# 1. `if/elif/else` in action:
# ```python
# if <something_not_False_and_not_None>:
#     ...this happens
# elif <something_else_False_and_not_None>:
#     ...this happens, the above was skipped
# else:
#     ...a different thing happens, both above were skipped
# ```
#
# 2. `while` in action:
# ```python
# while <something_not_False_and_not_None>:
#     ...this continues to happen repeatedly
# ```
#
# Most simply `if/elif/else` and `while` are switches that will allow, or
# disallow, the code within to run.
#
# Logical types (`True`, `False`, 0, 1) are most often responsible for controlling the flow of `if` and
# `while` statements..._however, other types can also control flow. We will see more later in another section._

a_nothing = None
if a_nothing:
    print("This wont go if a_nothing is None.")
else:
    print("This printed because a_nothing is None.")

zero = 0
if zero:
    print("This won't go if zero is 0")
elif zero == 0:
    print("This goes off if zero == 0")
else:
    print("Try and make this go off by altering 'zero' variable.")

a_num = 10
if a_num:
    print("This goes off if 'not None', 'not 0', and 'not False'")
else:
    print("a_num is iterpreted as a 'False'.")

# ## Sequence (list, tuple, range)
#
# Sequences are very useful for holding a bunch of things in a particular
# order. Each kind of sequence has its uses, strengths and weaknesses.

# +
this_is_a_list = numbers_string_var.split("\n")

print(this_is_a_list, end="") # the typical end of a print is "\n", but it doesn't have to be
print(f"\t{type(this_is_a_list)}")

# +
another_list = [integer_var, float_var, complex_var, 14.7]

print(another_list, end="\t")
print(f"{type(another_list)}")

# +
this_is_a_tuple = (1,2,3,"4")
another_tuple = 1,2,3,4; # <-- sneaky ; makes a tuple also

print(this_is_a_tuple, end="\t")
print(f"{type(this_is_a_tuple)}")

print(another_tuple, end="")
print(f"\t{type(another_tuple)}")

# +
start = 1
stop = 4
step_size = 3

this_is_a_range = range(stop)
start_range = range(start, stop)
startstep_range =range(start,stop,step_size) # this function has an optional keyword argument

print(this_is_a_range, end="")
print(f"\t{type(this_is_a_range)}")

print(start_range, end="")
print(f"\t{type(startstep_range)}")

print(startstep_range, end="")
print(f"\t{type(startstep_range)}")
# -

# ### Not all sequences can be altered
# ---
# When something can't be altered we call it "immutable". Tuples are an example
# of an immutable object.
#
# _Below is an example of a **try, catch** statement. These are great ways to manage
# expected errors. The more specific you are with the exception you are excepting
# the better._

try: # changing the first item in a list
    this_is_a_list[0] = "I'm a change"
    print(this_is_a_list)
except TypeError as e:
    print("Whoa, it won't let me do that because {e}")

try: # changing the last item of a tuple
    this_is_a_tuple[-1] = "I'm a change"
    print(this_is_a_tuple)
except TypeError as e:
    save_the_error_for_later = e
    print(f"Whoa, it won't let me do that because the {e}.")

# +
#raise save_the_error_for_later # if you want, take a look at the error we produced.
# -

# ### `if` and `while` with sequences
# ---
# Lists, Tuples and Ranges also can impact drive control flow with `if` and `while`.

empty_sequence = range(0)
if empty_sequence:
    print("This shouldn't print with an empty sequence.")
else:
    print("An 'empty' sequence is like a False to the `if` operator.")


# + [markdown] tags=[]
# ### Looping with sequences
# ---
# We can loop over many of the types of variables we've explored above. The `for`
# loop is another type of 'control flow'. It can be applied when we wish to loop
# through various things in a sequence or only loop for a limited number of repeats.
#
# _The function `clean_looper()` is defined using `def <function_name>:` syntax
# so that the next cell looks cleaner (and you see a function definition in
# action)._
#
# ## Defining new functions in python
#
# Functions are defined using the `def` operator.
#
# ```python
# def <my_function_name>(<inputs_to_your_function>): # functions don't need to take inputs
#     ...body of function
#     return <something> # not all functions return values
# ```
#
# Functions can be defined using the `lambda` operator.
#
# ```python
# <some_function_handle> = lambda <inputs>: ...something
# ```

# +
def clean_looper(iterable):
    last_thing = iterable[-1]
    for thing in iterable[:-1]:
        print(thing, end = ", ")
    print(last_thing)
    
# show a lambda function
make_list = lambda stop_at: [val for val in range(stop_at)]
clean_looper(make_list(10))

# loop over our sequences above
clean_looper(start_range)
clean_looper(another_tuple)
clean_looper(pretty_sentence)
# -

# # Numpy
# ---
# ---
#
# Numpy is arguably the most fundamental package for a neuroscientist
# interested in writing custom analysis code. Datasets are often 'arrays'
# with various dimensions: neurons, time, features, experimental conditions. The
# numpy package is the tool for storing, manipulating, and performing fast-ish and
# efficient operations on arrays of data.
#
# ## Defining New Data Arrays
#
# The **numpy.ndarray** is another object like the 'tuple' or 'list' except
# it is an object defined in the numpy package. The ndarray is likely the best
# object to hold your data when you intend to do matrix and vector operations.
#
# **np.zeros** and **np.ones** can help initialize an array with repeated values.

# + colab={"base_uri": "https://localhost:8080/"} id="ZMKEyomVNYEB" outputId="22951a3c-622e-4d46-dada-2ad326cb18db"
taylor = np.array([1.,1.]) # 1-D array, vector
print("taylor:\n", taylor, type(taylor))

swift = np.ones((1,2)) # 2-D array, row vector
print("swift:\n", swift, type(swift))

fearless = np.ones((2))
print("fearless:\n",fearless, type(fearless))

idk_taylor = np.ones((2,1)) * 3
print("idk taylor:\n",idk_taylor, type(idk_taylor))
# -

# ## Basic 'ndarray' properties

# + colab={"base_uri": "https://localhost:8080/"} id="5Iop5Ts5W4ay" outputId="86db0da5-33b6-4bd4-cb85-b8c380b7a9e7"
print("shape:",taylor.shape)
print("size:",taylor.size)
print("number of dim:",taylor.ndim)
print("data type:",taylor.dtype) # unlike in lists and tuples, elements share a type

# + colab={"base_uri": "https://localhost:8080/"} id="5Iop5Ts5W4ay" outputId="86db0da5-33b6-4bd4-cb85-b8c380b7a9e7"
print("shape:",swift.shape)
print("size:",swift.size)
print("number of dim:",swift.ndim)
print("data type:",swift.dtype)

# + colab={"base_uri": "https://localhost:8080/"} id="ojTg_9nQNqAa" outputId="f0fc7a53-b610-4d09-aeb8-a8db139e0f5c"
print("fearless:\n", fearless)
print("shape:", fearless.shape)

fearless1 = fearless[:,np.newaxis]
print("fearless1:\n",fearless1)
print("shape:", fearless1.shape)

fearless2 = fearless[np.newaxis,:]
print("fearless2:\n", fearless2)
print("shape",fearless2.shape)
# -

type(np.random.rand(1))

# ## ndarray methods
# yup... instances of numpy.ndarray are objects with methods. These are a few pretty convenient ones.

guitar = np.array([[1,2],[3,4]])
print(guitar)
print(guitar.sum())
print(guitar.cumsum()) # cumulative sum
print(guitar.max())
print(guitar.argmax())
print(guitar.min())
print(guitar.argmin())
print(guitar.mean())
print(guitar.std()) # standard deviation
print(guitar.reshape((4,1)))
print(guitar)

# + [markdown] tags=[]
# ### 'axis' parameter
# ---
#
# Many numpy operations allow the user to specify which axis to operate between.
# Once the operation has been applied between a certain axis (or dimension) it
# has effectively been collapsed into a singleton dimension. Numpy will by default
# disappear singleton dimensions to simplify the array.
#
# ```python
# # keeping dims is possible
# np.sum(<your_array>, axis=<dim>, keepdims=True)
#
# # also possible with array methods
# <your_array>.sum(axis=<dim>, keepdims=True)
# ```
#
# Consider if you had a matrix and you wanted to 'sum the columns' vs. 'sum the
# rows'. `np.sum(ur_mat, axis=<dim>)` can take care of either situation with the
# **axis parameter**.

# + colab={"base_uri": "https://localhost:8080/"} id="-E3-Fe2EWtNh" outputId="c35b0d5d-ea08-4892-b100-a28e5ef4acaf"
print("guitar has shape", guitar.shape, "\n",guitar)
wonderland = guitar[:,np.newaxis]
print("wonderland has shape", wonderland.shape, "\n",wonderland)
print("\n\t-----summing axis parameter examples------\n")
print("summing guitar with axis = 0: (sum between rows)\n",np.sum(guitar,axis=0))
print(
    "summing guitar with axis = 0: (sum between rows, keeping dims **not common**)\n",
    np.sum(guitar,axis=0, keepdims=True)
)
print("summing guitar with axis = 1: (sum between columns)\n",guitar.sum(axis=1))
print(
    "summing guitar with axis = 1: (sum between columns, keeping dims **not common**)\n",
    np.sum(guitar,axis=1, keepdims=True)
)
print("")
print("summing wonderland with axis = 0:\n",np.sum(wonderland,axis=0))
print("summing wonderland with axis = 1:\n",np.sum(wonderland,axis=1))
# -

# ## Array multiplication

# + colab={"base_uri": "https://localhost:8080/"} id="-qT6aH1RPe_8" outputId="54b604a0-86bd-4289-9bbb-5e6bcf96481b"
speak = np.array([[2,3],[4,5]])
red = np.matmul(speak,fearless1) # equivalent to np.dot but don't use this
print("speak:\n",speak)
print("fearless1:\n",fearless1)
print("red:\n",red)
# -

print(fearless1)

# +
# Applying new names so that the Linear algebra shines through in the plotted example
A = speak
x = fearless1

axis_lim = (-2,9)
vector_fig, vector_axes = plt.subplots(ncols=3, figsize=(10,4), constrained_layout=True)
fearless_fig = tdvec_plot(fearless1, axis_lim, axes_handle=vector_axes[0])
vector_axes[0].set_title("x (fearless1)")
vector_axes[0].set_aspect("equal")

speak_fig = tdvec_plot(speak, axis_lim, tip_to_tail=True, axes_handle=vector_axes[1])
vector_axes[1].set_title("Columns of A (speak) tip to tail")
vector_axes[1].set_aspect("equal")

red_fig = tdvec_plot(red, axis_lim, axes_handle=vector_axes[2])
vector_axes[2].set_title("red = Ax")
vector_axes[2].set_aspect("equal")

st_handle = red_fig.suptitle(
    """
    Note: In this case x (fearless1) is a special vector [1,1] so mutiplying it to any matrix 
        just gives us a new vector that is tip to tial of the matrix columns.
    """
)
# -

vector_fig.tight_layout() # an alternative to constrained layout can be set using the figure handle
vector_fig # the warning comes because we requested constrained layout at first (you don't need to do that).

# + colab={"base_uri": "https://localhost:8080/"} id="pJCEDqNGPueQ" outputId="d15ad21f-5228-4aed-a3d6-850c6052571d"
red_prime = speak @ fearless1 # equivalent to np.matmul
print("speak:\n",speak)
print("fearless:\n",fearless1)
print("red':\n",red_prime)

# + colab={"base_uri": "https://localhost:8080/"} id="BvoRsD3yVbTG" outputId="ad4fd637-5171-4e40-f7c7-ec9621ebff4e"
print("speak:\n",speak)
red1_prime = np.einsum('ij,jk->ik',speak,fearless2) #specify indices for matrix operation
print("fearless2:\n",fearless2)
print("red1':\n",red1_prime)
# -

# ### Matrix 'powers', beware!
# ---
# It is important to know exactly how the computer will interpret particular
# operations.
#
# `**` operator is the python version of "to the power of": `2**x` is $2^x$.
#
# However, this operator doesn't operate on like it does in common mathematics
# syntax.
#
# $A^3$ isn't achieved via `A**3` in python. In fact, `A**3` is element-wise and
# is an extension of the Hadamard product ($A\odot A\odot A$).

# + colab={"base_uri": "https://localhost:8080/"} id="8zEtGBexXeDV" outputId="3433a2d3-359b-4c19-8945-246e53f241cb" tags=[]
sing = speak ** 3 
print("sing has shape", sing.shape, "\n",speak)

print(
    (sing == (speak * speak * speak)).all() # equiv. to the Hadamard product of 3 identical matrices
)

print(
    (sing == (speak @ speak @ speak)).all()
)
# -

# ## Element-wise Multiplication

# + colab={"base_uri": "https://localhost:8080/"} id="JNzYM-2aQS0x" outputId="651c68ae-f2b4-42cc-84c6-bed4dc9865bc"
fearless3 = np.array([[1,1],[1,1]])
red3 = np.multiply(speak,fearless3)
print("speak:\n",speak)
print("fearless3:\n",fearless3)
print("red3:\n",red3)

# + colab={"base_uri": "https://localhost:8080/"} id="0hZMgsVySVjx" outputId="8a23f7a7-dbbc-4a9f-8ca7-954c83f074e8"
red3_prime = speak * fearless3 # mostly equivalent but be careful
print("speak:\n",speak)
print("fearless3:\n",fearless3)
print("red3:\n",red3_prime)

# + colab={"base_uri": "https://localhost:8080/"} id="gWvvxvq6Sf84" outputId="95547d72-7590-4f45-efe3-8fd2e5e027ff"
2 * np.array([1,2])

# + colab={"base_uri": "https://localhost:8080/"} id="wsUXOwO_SlNp" outputId="9062d699-899c-4efc-ef6a-47a417020b39"
np.multiply(2,[1,2])
# -

# ## Broadcasting 
#
# With broadcasting, numpy follows a set of rules (_think_ assumptions) for how "element-wise"
# operations between size-mismatched arrays are handled. 
#
# With broadcasting, the user is not responsible for replicating the smaller array 
# to match. In certain situations this can make your job easier, for example if 
# you would like to add a vector to every column of a matrix. 

# + colab={"base_uri": "https://localhost:8080/"} id="YBvp8TldSn3A" outputId="84baf6ce-e8f9-4d3b-a99c-e1cffd0e4721"
fearless_shrink = np.array([[0.5],[0.25]])
print("fearless_shrink has shape", fearless_shrink.shape, "\n",fearless1)
red1 = np.multiply(speak,fearless_shrink) # NOT matrix-vector multiplication, this is "element-wise"
print("speak has shape", speak.shape, "\n", speak)
print("red1 comes from replicating fearless1 and multiplying\n", red1)

# + colab={"base_uri": "https://localhost:8080/"} id="QI-GNm9LS3PE" outputId="4bf9f5d4-3856-47ff-8953-e63e2a15772c"
fearless = np.array([6, 3])
print("fearless has shape", fearless.shape, "\n",fearless)
print("speak has shape", speak.shape, "\n",speak)
red_tilde = np.multiply(speak,fearless)
print("red_tilde comes from replicating fearless and multiplying\n",red_tilde)
# -

# **NOTE:** Broadcasting takes the shape of the array with the most dimensions

# + colab={"base_uri": "https://localhost:8080/"} id="lUE17U0LTxoz" outputId="56706bc9-13eb-4168-f505-cd81de091b4f"
fearless_newax = fearless1[:,:,np.newaxis]
print("fearless11 has shape", fearless_newax.shape, "\n",fearless_newax)
print("speak has shape", speak.shape, "\n",speak)

red_newax = np.multiply(speak,fearless_newax)

print("red_newax comes from replicating fearless and multiplying\n",red_newax)
# -

# ## Indexing
#
# Often, we would like to have access to a specific element, or set of elements
# from an array, list, or tuple. In python this is achieved with the "\[ \]"
# brackets.
#
# `:` - is a helpful operator to simplify consistent patterns of indexing
# requests. Here is a simple look, more applications explored below:
#
# ```python
# my_list[:] # all elements
#
# my_list[:4] # start to 3
#
# my_list[2:4] # 2 to 3
#
# my_list[2:11:3] # 2 to 10 in steps of 3
#
# my_list[2::3] # 2 to end in steps of 3
# ```

# + colab={"base_uri": "https://localhost:8080/"} id="W1KSBe_-YGwO" outputId="3acbe8bd-e8d4-4823-b3a4-f8afdbfdbbe1"
reputation = np.arange(1,6)
print("reputation has shape", reputation.shape, "\n", reputation,"\n")

print(reputation[0:1])
print(reputation[:1])

# + colab={"base_uri": "https://localhost:8080/"} id="tUrJ0MIdYTpb" outputId="4b2427fb-30e8-400c-a1fc-030188210b04"
print(reputation[1:])
print(reputation[1:reputation.shape[0]+1])
print(reputation[1:6])

# + colab={"base_uri": "https://localhost:8080/"} id="cX3U4eS7YkSh" outputId="a9b58def-07ec-4c2a-c6f3-956c708518cc"
print(reputation[-3:-1])

# + colab={"base_uri": "https://localhost:8080/"} id="TAuuDk7hYz0U" outputId="353cd597-bffd-42be-8013-b934bb311bbb"
lover = np.vstack((reputation,reputation+1,reputation+2,reputation+3,reputation+4))
print(lover)
print(lover[1:3,4])

# + colab={"base_uri": "https://localhost:8080/"} id="ma_Lx1zJZFqY" outputId="2a9e27b2-d752-44e0-ed75-6caf759ecf03"
print(lover[::2])

# + colab={"base_uri": "https://localhost:8080/"} id="eF8BSSqHZsL4" outputId="a858016b-5e10-49c3-90e4-43bca0792534"
print(lover[::2,::2])

# + colab={"base_uri": "https://localhost:8080/"} id="6A_CUxtCZ2_Y" outputId="f228c3fd-ee5c-4c52-bb25-567669490957"
folklore = np.arange(100) * 2
print(folklore)
betty = npr.randint(100,size=10)
print(betty)
print("folklore indexed with betty:",folklore[betty])

# + [markdown] tags=[]
# ### Masking
# ---
# Masking is a lot like indexing, but it allows the user to choose individual elements of an array by applying a
# "mask" where a `True` bool allows the element through and `False` masks the
# element away.

# + colab={"base_uri": "https://localhost:8080/"} id="GT9cSm86avdI" outputId="ddaa52c4-58ae-4858-b23e-605045027df4"
evermore = npr.randint(2,size=100).astype(bool)
love = np.arange(0,100)
story = love[evermore]
print("evermore has shape", evermore.shape, "\n", evermore, "\n")
print("love has shape", love.shape, "\n", love, "\n")
print("story has shape", story.shape, "\n", story, "\n")

print("sum of evermore:",np.sum(evermore))
print("size of story:",story.size)
# -

# ## Reshape np.arrays
#
# In some cases, often for speeding up operations, it can make sense to reshape
# arrays.

# + colab={"base_uri": "https://localhost:8080/"} id="4yWA8_U3a9T1" outputId="945f91c3-da80-4f2f-b752-36bd3e262074"
folklore1 = folklore[:,np.newaxis]
folklore1.shape

# + colab={"base_uri": "https://localhost:8080/"} id="LO1h42EpaLZe" outputId="08833ae2-9637-45b9-a307-721f6dbe58b4"
folklore1.flatten().shape #turns any num of dimensions into 1

# + colab={"base_uri": "https://localhost:8080/"} id="ZjOvs7bsat9w" outputId="9378348a-789b-45c4-eb87-60c1bc31461b"
print(folklore1.shape)
print(folklore1.reshape(10,10).shape) # another useful method
print(np.reshape(folklore1, (10,10)).shape)
print(folklore1.shape)

# + [markdown] id="HWfblV2LhZVU"
# # Plotting with matplotlib.pyplot
# ---
# ---
# An assortment of plotting tricks.
#
# Note the general plotting style...
#
# ```python
# figure_handle, axes_handle = plt.subplots()
# axes_handel.some_plotting_function()
# ```
#
# is much more flexible and provides more control than...
#
# ```python
# plt.some_plotting_function()
# ```
#
# ---
#
# This is a little joke that summarizes the good (and bad) ways to use pyplot.
# <div align="center">
# <img src="./media/plt_alignment_abhishek_sharma.jpeg" width="600" height="300" title="Found on Twitter by Abhishek Sharma" />
# </div>

# + colab={"base_uri": "https://localhost:8080/", "height": 601} id="dZZS_fIHhfud" outputId="db8f7ec2-3e99-4570-fe90-415356e40005"
# line plot
plt.rcParams.update({'font.size': 14}) # <-- this will impact all figures (go up and re-run the vector plots)
cardigan = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(10, 10), constrained_layout=True)
axs[0, 0].hist(cardigan[0], histtype="step", label="cardigan$_0$")
axs[0, 0].hist(cardigan[1], histtype="step", label="cardigan$_1$")
axs[0,0].set_title('histogram')
axs[1, 0].scatter(cardigan[0], cardigan[1])
axs[1, 0].set_xlabel("cardigan_0")
axs[1, 0].set_ylabel("cardigan_1")
axs[1,0].set_title('scatterplot')
axs[0, 1].plot(cardigan[0], cardigan[1],label="a line")
axs[0,1].set_title('line plot')
axs[1, 1].hist2d(cardigan[0], cardigan[1])
axs[1,1].set_title('2D histogram')
axs[0,0].legend()
axs[0,1].legend()
fig.suptitle('random cardigan')

fig.savefig(os.path.expanduser("~/giocomo_python_tutorial_plot_save_example.png"), dpi=100)
plt.show()

# + colab={"base_uri": "https://localhost:8080/", "height": 661} id="vVrbqlPxh6GP" outputId="d3065c01-ddea-458a-d9f3-5eca5091516d"
willow = npr.uniform(size=10000)
willow_sq = willow.reshape(100,100)
fig, ax = plt.subplots(1,2,figsize=(24,12), constrained_layout = True)
ax[0].set_title('example raster plot')
ax[0].set_xlim((0,1))
ax[0].set_ylim((0,100))
for i in range(100):
  ax[0].scatter(willow_sq[i,:],np.ones(100)*i,color='k',s=5)
  #scatter(x,y)

ax[1].set_title('example heat map')
exile = ax[1].imshow(willow_sq)
fig.colorbar(exile, ax=ax[1],shrink=0.8)
