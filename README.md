# sisy_table
Parse the Sisyphos program to a readable timetable

# About

In order to run the program the following python modules are needed:

matplotlib
numpy
ortools

# What

The program takes a text file (example in input/programm_example) as input, parses the times, runs the variables through an MIP optimizer, and draws the resulting timetable using matplotlib.

In order to run the program simply add the relative path to your input file in main.py, and run:

*python main.py