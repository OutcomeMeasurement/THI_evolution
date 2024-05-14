# Genetic Algorithm for the abbreviation of the THI Questionnaire


## Introduction

This repository holds the code that is used for the abbreviation the THI questionnaire using a Genetic Algorithm (GA). With the algorithm, the THI is split up in two or three stages.

## How to use the code

The `Evolution` class is the starting point for the GA for the abbreviation of the THI questionnaire. This takes as input:

- `answers`, a NumPy array in the shape of NxM numbers, where N is the amount of responded questionnaires, and M is the amount of items in a questionnaire.
- `results`, a Numpy array with length N, where N is the amount of questionnaires.
- `n_questions_1`, an integer which specifies the amount of questions in the first stage.
- `n_questions_2`, an integer which specifies the amount of questions in the second stage. The remaining questions will go to stage 3. For models that should only have 2 stages, this should be set to 0.
- `n_switches`, an integer which specifies how many questions should be switched during a mutation.
- `pool_size`, an integer which specifies the size of the population of the GA.
- `fitness_func`, a reference to a function that can calculate the performance of a certain questionnaire. Example fitness functions can be found in [fitness_functions.py](fitness_functions.py). The fitness function 

Use the `Evolution.step()` function to do 1 evolution step. Use the `Evolution.best()` function to find the current best performing question selection.

An example of a 3-stage model can be found in [example.py](example.py).

The THI questionnaire data used in the research can be found in [thi_data.csv](thi_data.csv).

## How to read the result

The result that follows from the GA will be in the form of a NumPy array. In this section, it will be explained how to read this NumPy array.

For clarity, let's assume that the full questionnaire consists of only 5 questions. If you are looking for a 2-stage model that consists of 3 questions, the best solution found can look as follows:

    array([1, 0, 1, 1, 0])

This means that the best found solution consists of question 1, 3 and 4 in stage 1 and questions  and 5 in stage 2.

If you are looking for a 3-stage model, the best solution can look as follows:

    array([2, 1, 1, 0, 2])

This means that question 2 and 3 should be asked in the first stage, question 1 and 5 in the second stage, and question 4 in the third stage.

## The fitness function

The fitness functions are crucial in determining if some question selection is better than another. It should act as a distance function. Therefore, a better question selection should get a lower value out of the fitness function that worse question selections. Keep this in mind when creating a custom fitness function.
