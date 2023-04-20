# Robotic Gripper: Block Stacking and Unstacking

## Description
This project aims to create a robotic gripper capable of stacking and unstacking three colored blocks (red, blue, and green) on a table. The project 

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation
To set up the development environment for this project, follow these steps:

1. Clone the repository:
```
git clone https://github.com/kiranajith/Stacking-blocks-on-table
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```
## Usage

Open the terminal and navigate to the project directory.
Run the following command to start the program:
```
python main.py
```
Here is a sample output
```
$ python main.py
Provide three blocks to stack :
b g r
---- initial Configuration ----

red block is on the table
blue is on the red block
green is on the blue block

---- unstacking blocks ----

unstacked green from blue
put green on table
unstacked blue from red
put blue on table

---- stacking blocks ----

picked up green
stacked green on top of blue
picked up red
stacked red on top of green

---- final configuration ----

blue block is on the table
green is on the blue block
red is on the green block
```
