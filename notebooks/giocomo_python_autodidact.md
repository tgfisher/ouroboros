---
jupyter:
  jupytext:
    formats: ipynb,py,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.7
  kernelspec:
    display_name: Python (we_sick)
    language: python
    name: we_sick
---

# IPython Extensions

```python tags=[]
# Don't forget to autoreload if you are using local src code
```

# Importing

If you have a lot of imports, splitting them up in the following way
makes it easy for someone else to skim and see what is used.

```python
# 'standard' libraries first
import os, sys

# then libraries managed by others
import numpy as np
from matplotlib import pyplot as plt

# then your custom libraries
```

```python
print(sys.executable) 
```

# Diving Right In
---
---

In this section you will gain some experience with the concepts covered in the 
`giocomo_python_tutorial.ipynb` by playing around with a data matrix.

The data matrix is actually a low-res image. An 
image is a nice training tool because changes should be obvious and simple
to recognize quickly.

### Diving Right In Homework List

- [ ] Numpy Basics: Load a .npy file
- [ ] Plotting Basics: Plot the Array as an Image
- [ ] Indexing Basics: Select Array By Index 
- [ ] Numpy Basics: Understanding `dtype`
- [ ] Numpy Basics: Manipulate Array By Index (Find Values in an Array)



### HW: Load The `bw_arr_pm.npy` From the `raw_data` Directory
---
In order to complete the rest of the homework you will need the data from `bw_arr_pm.npy`. It
is stored in `.npy` format in the `ouroboros/raw_data/` directory (folder).

```python
#HOMEWORK CAN GO IN AS MANY BLOCKS AS YOU LIKE
```

### HW: Plot the Array as An Image
---
Have fun with this exercise. It is intended to encourage you to explore basic `matplotlib.pyplot`.

Your plot should contain:
1. the `bw_arr_pw.npy` plotted
1. a title
1. x- and y-axis labels
1. a colorbar (if this were neural data we'd need to know how to interpret pixel color) 

**BONUS:** After successfully completing the tasks above you will notice that
axes have the (0,0) pixel in the top right. This is handy for matrices, but 
what if you'd like to plot binned spike counts from trial zero to trial n, bottom to top?
**Add subplot where the image is plotted with (0,0) at the bottom.**

```python
#HOMEWORK CAN GO IN AS MANY BLOCKS AS YOU LIKE
```

### HW: Select Array By Index
---
In addition to manipulating an array by index, we will play around with the the "dtype" of an array and discuss
the significance of a "dtype".

1. Imagine a 'cropped' view of the image that you like better. Use 'slicing' to realize 
this imagined crop in a plot below.
1. Use `plt.subplots(ncols=2)` to plot the old and new
images side by side with their originals.


```python
#HOMEWORK CAN GO IN AS MANY BLOCKS AS YOU LIKE
```

### HW: Understanding `dtype`
---
The datatype is the "kind" of thing that the computer must store. Floats, strings, integers, positive real numbers
are all examples of "types" of data. The numpy datatype gets more specific than that, it also asks
how you would like to store a thing: 8 bit positive integer(?) or 64 bit positive integer(?). We care about this
because just like each "type" defines what kind of thing can be stored the "dtype" gets more specific,
it also defines "how much" you can store.

**A concrete explanation of "uint8"** -- 'u' for unsigned (can't sign -/+) and 'int8' for storing 
    an integer with 8 bits (1 byte, _similar to how 12 is a dozen_). We know a bit can take 2 states 
    (0 or 1) and we have 8. With a little math we know we can make 256 unique combinations, 2^8=256,
    to store 256 things with 1 byte. Since we want to be able to store zero this means uint8
    can go from 0-255, wow!

1. Make a histogram of pixel brightnesses that shows both the distribution of brightnesses for your
crop and the original image.
1. Adjust pixel brightnesses of the original image.
    1. Note that the image histograms don't spread out completely between 0 and 255. Look at where 
    the tails of the histogram basically go to zero, this should leave you with 
    a pseudo minimum greater than zero and pseudo maximum less than 255.
    1. Set values below your pseudo min to the pseudo min value (e.g. for a pseudo min of 6, all pixels 
    5 and below should be set to 6).
    1. Set values higher than your pseudo max to the pseudo max value (e.g. for a pseudo max of 250, all pixels
    251 and above should be set to 250).
    1. Normalize the pixels so that your pseudo max pixels are 255 and your pseudo min pixels are 0.
1. Make a new variable saving save the exposure adjusted array as "uint8" `uint_version = <ndarray>.astype("uint8")` \

`uint_version.nbytes` should be quite a bit smaller than `norm_version.nbytes`. This means it 
takes up less space on your computer.

```python
#HOMEWORK CAN GO IN AS MANY BLOCKS AS YOU LIKE
```

### HW: Manipulate the Array By Index (Find Values in an Array)
---
1. Find the brightest pixel
1. Make a new image, using index assignment put a _black_ horizontal 
and vertical line (4px wide) over the brightest pixel.
1. Plot the array with the cross-hairs from (2) on it. 
1. Find the darkest pixel
1. Make another new image off the original, using index assignment put _white_ cross-hairs 
(4px wide) over the darkest pixel. 
1. Plot the array with the cross-hairs from (5) on it. _Tired of writing out the plotting 
details? Might be time to make a plotting function._
1. Place a 30px wide "frame" around the photograph by changing existing pixel values.
1. Once you've plotted the cross-hairs you will notice that the brightest
pixel isn't where you might expect (at the lighthouse). Describe in pseudo-code
an algorithm that you could use to reliably find the lighthouse lamp. Feel free
to "use" any packages that you would try if you were solving the problem. _HINT: Use
a markdown cell for this part_

**Bonus** Implement (8), find the lighthouse lamp and plot another set of _black_ cross-hairs.

```python
#HOMEWORK CAN GO IN AS MANY BLOCKS AS YOU LIKE
```

#### This is a markdown cell

<!-- #region tags=[] -->
# Variables and Shared Memory
---
---

In this section we begin to explore how python stores variables.

- Are identical things stored in the same place, or does python store multiple copies for
the same thing?
- Where is a variable stored?
- Importantly, in which situations does python's memory usage have consequences on your code?

_If python is your first--or only--programming language it is important to note 
that the 'rules' we discuss in this section represent design decisions. Handling 
variables and how they are stored is done differently in other 
languages._

### Variables and Shared Memory Homework List

- [ ] Make a custom deep copy function.
<!-- #endregion -->

```python
"""
This block may seem strange, we are just defining a variables and values that are 
easy for us to remember. This section is all about how variables can change when 
you aren't expecting it, colors should be easy to remember.
"""
red = "red"
my_colors = ["purple", red]
my_list = [number for number in range(10)] # (you've just learned a new thing) this is "list comprehension"
my_list[0] = my_colors
```

```python
print("red: \t\t", red)
print("my_colors:\t", my_colors)
print("my_list:\t", my_list)
```

#### Making a new variable from an old one.

What happens if we make a new variable from a new one?

_Spoiler: It depends on what kind of variable._

```python
a_color = red
new_list = my_list
```

```python
a_color = "dark red"
print("red: ", red, "\n\t^- the string stored in `red` hasn't changed,")
print("\t  this makes might make some kind of sense.")
```

```python
new_list[1] = "change"
print("new list: ", new_list)
print("my list: ", my_list, "\n\t\t\t\t   ^- `my_list` changes after changing new_list,")
print("\t\t\t\t\t unlike the `string` example above, beware...")
```

#### (solution) `.copy` a list to really make a copy

What we just observed can cause pretty nasty "bugs"
in your code. Lets review:

**Variables pointing to the "same" immutable object won't impact one another.**

Luckily, many `types` in python are "immutable", they can't be changed. Practically
this means that if you have two variables pointing to the same immutable `a = (11,12); b = a`
changing `a` will just overwrite it, `a = (15,16)`, `a` is now `(15,16)`, but `b` is still
`(11,12)`. Variables storing integers, floating-point numbers, 
booleans, strings, and tuples will all have the same "reassignment"
behavior. 

**Variables pointing to the "same" mutable object will impact one another**

As we saw above, `new_variable` and `my_variable` hold the same "mutable" (a `list`) 
located at the same location in memory. They are just two names for the 
same "address".

--- 

`<mutable>.copy()` method makes a copy of something to a new location in memory,
a new memory address.

```python
# this might look a little complicated, it is written
# this way to prevent any funny business caused by
# potentially asynchronous cell runs in jupyter.
living_variables = %who_ls
if not any(var == "my_list_copy" for var in living_variables):
    print("make a copy")
    my_list_copy = my_list.copy() # <-- in this block, this line is what you should understand.
```

```python
new_list[4] = "another change"
print("Another change to `new_list` changes `my_list`, but doesn't alter `my_list_copy`!\n")
print("  new_list:\n\t", new_list, "\n\t\tmemory location: ", id(new_list))
a_thing = "somthing"
print("  my_list:\n\t", my_list, "\n\t\tmemory location: ", id(my_list))
print("  my_list_copy:\n\t", my_list_copy, "\n\t\tmemory location: ", id(my_list_copy))
```

#### `.copy`s aren't always deep enough.

What we have above looks like it works!

We have verified that `my_list` and `my_list_copy` are stored in different locations.
We have even made a 'change' to `new_list` (`my_list` changed again, too) and saw that
this didn't alter `my_list_copy`. 

The astute reader might wonder about the "inner list". The copy we made doesn't also `.copy()` the list
at index 0, `['purple', 'red']`. This remains a pointer to a place in memory, meaning if the item at that
memory location is changed the copied list can have a changed component. 

```python
def all_integers_match(*integers):
    if not any((item - integers[0] for item in integers[1:])):
        return "All Matching"
    else:
        return "At Least One Doesn't Match"

def memory_locations_of_list_elements(*args):
    for stuff in zip(*args):
        ids = (id(value) for value in stuff)
        print(*ids, "<--", all_integers_match(ids))
```

```python
memory_locations_of_list_elements(my_list, new_list, my_list_copy)
```

```python
my_list_copy[0]+=["O_o 'Oh, no...'"]
print("Changing the list within my_list_copy (shared with my_list) alters the list wherever it shows up:")
print("  zeroth element of my_list:\t\t", my_list[0])
print("  zeroth element of my_list_copy:\t", my_list_copy[0])
```

### HW: Make a custom deep copy function
---

Make a function called `deep_copy` that is capable of copying a list that has other
lists in it.

1. For full credit this function should deep copy down to the first level.
**Bonus** credit write a function that is depth agnostic.

```python
def deep_copy(thing):
    pass
```

# Variable Scope
---
---

In this section we will explore how to know which variables are in currently in use. Often
variables are penned into a particular context. For example, unless a variable 
is an output, a variable created inside a function typically doesn't exist
outside the function.

### Variables and Shared Memory Homework List

- [ ] Functions for exposing the current workspace.
- [ ] Fix a variable scope related bug.

#### Notebook Workspace (and getting '`help()`)

For those coming from Matlab or a python IDE, you may
be familiar with tools that allow you inspect variables in your current workspace. 
IPython has a nice set of magics (`%who`, `%whos`, `%who_ls`) that list variables
out for you.

In this section you will write your own workspace tools and learn a bit about how 
the python variable space is organized using your choice of `dir`, `global`,
`local`, and `vars`. 

---

`help()` -- is a fantastic tool to give you information on a python object.

```python
"""
In the next few cells we are going to show you the output of `%who`, `%whos`, and
`%who_ls`. You will notice that all the variables you've created in the sections
above are listed out. This means--what you already know--that any variable
is available in any cell.
"""
def underline(my_str):
    """
    Just a cute function to underline in a print 
    statement b/c I got tired of formatting by hand.
    """
    str_len = len(my_str.strip("\n\t"))
    return my_str + "\n" + ("=" * str_len)
    
print(underline("who output"))
%who
```

```python
print(underline("\nwhos output"))
%whos
```

```python
print(underline("\nwho_ls output (items listed as a column)"))
whos_list = %who_ls
for item in whos_list:
    print(item)
```

```python
help(locals)
```

```python
def custom_functions_can_have_help(an_input, keyword_argument="Your input was: "):
    """
    This is a help string... for a function about how to add `help strings`
    to custom functions.
    
    -- params --
    input_var: int
        This input should be an integer for some reason that doesn't matter
        because this function doesn't really do anything.
    ** default params **
    keyword_argument: str
        This input has a default value, so the user doesnt "need" to set it.
    >> return <<
        A string with these function inputs combined.
    """
    assert isinstance(an_input, int), "Your input must be an integer."
    
    return keyword_argument + str(an_input)
```

```python

```

```python
help(custom_functions_can_have_help)
```

<!-- #region -->
## HW: Custom Workspace Listing
--- 

Write a few functions to 
1. list functions
1. list modules
1. list variables.
1. a function that wraps the first three and returns an output you personally find handy.

#### A few tools you will find useful

`isinstance` takes a variable or instance of an object and tells you if it
is of a certain type. You will use it like this: 
```python
isinstance(<variable_or_instance>, <class>)
```

`locals` returns a dictionary, `dict` type, of the local variables. 

Be careful, when you use `locals`, `locals()` output will change if you assign `locals()` 
to a new variable (because you will have just have added a new variable to the workspace). 
Luckily, the `.copy()` method exists for `dict` objects just like it does for `list` objects 
(from [variables and shared memory](#Variables-and-Shared-Memory)).

_Hint: you can import `ModuleType` and `FunctionType` from the `types` module._
<!-- #endregion -->

```python
def workspace_modules_list():
    pass
def workspace_functions_list():
    pass
def workspace_variables_list():
    pass
def my_who_list():
    pass
from types import ModuleType, FunctionType
```

<!-- #region -->
## Variable Scope and Functions

Often while coding in an IDE or jupyter there are many variables floating around. In the previous 
section on [workspace](#Workspace) we played with tools that expose functions, 
variables, methods &c. In this section we will highlight the potential for "bugs" 
in any python situation where there are variables floating 
around before a function definition.

**Situation A: Function Uses a Variable From Outside the `def`**

Pythonic "assumption": This is a global variable.

```python
variable_from_outside = "I will raise the siege of Orelans."
def situation_a():
    return variable_from_outside
``` 

**Situation B: Function Assigns to a Variable From Outside the `def`**

Pythonic "assumption": Assigning a value to a variable that already exits? 
This is a new variable in the "local" scope.

```python
def situation_b():
    variable_from_outside = "The mountains are calling and I must go."
    return variable_from_outside
```

**Situation C: Breaking the "local" assumption**
```python
outKast = "I'm sorry Ms. Jackson"
def situation_c():
    global outKast
    outKast = "I am for real."
    return outKast
```
    
<!-- #endregion -->

### Situation A: 

```python
variable_from_outside = "I will raise the siege of Oreleans."
def situation_a():
    return variable_from_outside
```

```python
print(variable_from_outside)
print(situation_a())
print(variable_from_outside)
```

### Situation B:

```python
def situation_b():
    variable_from_outside = "The mountains are calling and I must go."
    return variable_from_outside
```

```python
print(variable_from_outside)
print(situation_b())
print(variable_from_outside) # the global variable `variable_from_outside` isn't changed
```

### Situation C:

```python
outKast = "I'm Sorry Ms. Jackson."
def situation_c():
    global outKast
    outKast = "I am for real."
    return outKast
```

```python
print(outKast)
print(situation_c())
print(outKast)
```

### HW: Fix a variable scope related bug
---
The function `fix me` isn't working. It is taking valid paths and saying they don't exist.

**goal** -- Debug the `fix_me` function to "free" the keyword argument.

```python
# nothing in this block needs to be changed
valid_path = os.path.expanduser("~")
```

```python
# something in this block is broken
def path_is_valid(path):
    path = path + a_thing
    return os.path.isdir(path)

def fix_me(path, keyword_argument = "I want to be free"):
        if path_is_valid(path):
            print(keyword_argument, "(the path does exist, btw.)")
        else:
            print(f"{path} does not exist")
```

```python
# this is just an evaluation block, change the function definition above
fix_me(valid_path)
```

```python

```

