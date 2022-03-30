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
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# My Dog Ate My Twin... Study
### A Little Bit of Everything Through A Worked Example

Over the last 90 years your medical school has collected longitudinal height data
from pairs of identical twins. Each individual is assigned a random ID number when
they join the study. Data collected is linked to a subject's ID rather than their name
in order to protect the identity.

The red floppy-disk linking subject ID, name, and co-twin
was mistaken by the bosses dog--its owner has a soft spot for retro-kitsch dog toys--as 
a retro-kitsch dog toy.

Fortunately, the team has all of the ID linked records stored on an SSD,
the dog doesn't have a taste for the modern, some semi-unique identifying 
information is collected from subjects during height collection, and you 
are on the job.

**You must** (a) relink twins and (b) come up with a visualization to show off your twin
linking skills.

#### Suggested Approach

1. Take a quick look at your data. It is stored in the `raw_data/` directory off of
this `./notebooks/` directory. A `.csv` file can be viewed in any text editor.
1. After skimming the data take a moment to consider the various inroads, potenital
pitfalls, and edge-cases.
1. Write an approach out _in words_, like a logical cascade.
1. Pseudo-code your solution. This step should be about picking a 'decomposition' of
the problem that will allow you to solve the problem in easy to grok chunks of code 
(functions please).
1. Code it up. Push yourself to make a module, better yet add it to your local `ourorboros`
directory.



# Take a Look at Your Data
---
What do you notice that could come in handy when you are solving this problem.


### Notes:
- im a note
1. im a list
- [ ] im a checkbox


# Pitfalls and Edgecases
---
What are some bad assumptions that could get us into trouble?


### Notes:
- im a note
1. im a list
- [ ] im a checkbox


# Write out your approach
---
Do this first, and keep it the same. It will be fun to see if/how your approach ended up.


## My Approach
I'm gonna crush it!


# Pseudo-code
---
This is when you can start to plan. Be as specific as you like up to your familiarity with python (e.g. "list from 0 to 9" to `[val for val in range(10)]`). Think carefully about how tasks can be broken out into reusable functions.

<!-- #region -->
## Pseudo Code can be linted if you like, or just write text.
```python
def iThink(you_sure_are):
    return generate_a_huge_complement_somehow
```

def iThink(you_sure_are):

    return generate_a_huge_compliment_somehow
<!-- #endregion -->

# Code it Up!!
---
Your solution should be down in the cells here (dont forget to import the tools you need).

If you already have some python under your belt push yourself to write a module. Witha module you should
be able to `pip install -e .` the package, and `from ouroboros import <dog_ate_my_twin_tools> as dogfix`
to use your functions in the notebook.
