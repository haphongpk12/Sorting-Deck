# Sorting-Deck

## Core project

### Notions: sorting algorithms and algorithm complexity

## Introduction

This subject is an algorithm project.

It will initiate you to a fundamental category of algorithms -sorting algorithms-, as well as theoretical notions revolving around algorithm analysis, such as the big O notation. In this project, your understanding of the theoretical notions is as important as your code, so spend enough time doing your research and synthesizing it.


## Your mission

Your mission is to implement different sorting algorithms and to visualise those algorithms. 

When given a series of numbers as input, your program will sort them using the algorithm specified on the command line. It will output the different steps of the sorting operation on stdout, or display them in the GUI if the GUI option is specified.

In the core part of the project, you will implement the following algorithms:
    - bubble sort
    - insertion sort
    - quick-sort
    - merge sort

Because understanding algorithms and their complexity is essential to become a well-rounded engineer (... you will also need it to pass technical interviews!), you also need to research the complexity of those algorithms. During the code review, you must be able to describe the worst/average/best cases of those algorithms.

__Note__: Obviously you won't get any skill points if you don't understand perfectly what you have implemented.


## Directions
Your program must be called sorting_deck.py and be present at the root of your git repository.

The arguments to the --algo option are bubble, insert, quick and merge. If the option --algo is not specified, the default algorithm will be bubble sort.

A --gui option will display a graphical representation of the sort with the pyglet library that you know already. You must be able to display inputs of up to 15 integers in the core part of the project (you can handle larger inputs as a bonus). This limit is only for the GUI mode, the default mode should of course handle inputs of all sizes.

In non-GUI mode, the outputs on stdout will be as follow:
```diff
- red
```
