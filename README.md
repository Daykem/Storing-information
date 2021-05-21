# Storing Informations


[Create by Daykem](https://tomrouvier.eu)

[![Build Status](https://travis-ci.org/quii/learn-go-with-tests.svg?branch=main)]()

### 
Storing Information is a software component for storing information about student grades. Each topic that a student is graded on has a Rubric. A Rubric is made up of multiple Criteria (up to a maximum of 10). When a student is graded they are awarded a score for each Criterion in the Rubric, which is an integer value between 1 and 5.

![GitHub Logo](/images/example.png)

## Why

* Explore the Python language by writing tests
* **Get a grounding with TDD**. Go is a good language for learning TDD because it is a simple language to learn and testing is built-in
* Be confident that you'll be able to start writing robust, well-tested systems in Python

## Python fundamentals

### Install python
On MacOS
> brew install python

On window/Linux
> sudo apt install python3.8
> sudo yum|dnf install python3.8

### Run project
> python3 someproject.py

### **When the project are running you have 4 possibility:**

Add a new student with their grades
> a
When you add new student you need: fistname lastname, design grade, implementation grade, testing grade, documentation grade

Look the statistics of the students
> s

Create a CSV file
> csv

Quit
> q

## Background

I have some experience in introducing Python in development teams but I had never done unit tests with it, so this was an opportunity to try.