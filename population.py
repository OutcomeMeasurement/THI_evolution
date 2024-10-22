import numpy as np
from typing import Callable

from questionset import Questionset


class Population:
    def __init__(
        self,
        answers: np.ndarray,
        fitness_func: Callable,
        n_questions_1: int,
        n_questions_2: int,
        pool_size: int,
        results: np.ndarray,
    ):
        self.answers = answers
        self.fitness = fitness_func
        self.pool_size = pool_size
        self.results = results

        self.individuals = [
            Questionset(
                n_questions_1=n_questions_1,
                n_questions_2=n_questions_2,
                n_questions_total=len(answers[0]),
            )
            for _ in range(pool_size)
        ]
        self.sort_individuals()

    def sort_individuals(self) -> None:
        """Sort individuals based on the fitness function"""
        fitness_scores = []
        for qs in self.individuals:
            if not qs.fitness_score:
                fitness_score = self.fitness(qs, self.answers, self.results)
                qs.fitness_score = fitness_score
            fitness_scores.append(qs.fitness_score)

        self.individuals = [
            x for _, x in sorted(zip(fitness_scores, self.individuals))
        ]
        return

    def remove_individuals(self) -> None:
        """Only keep the pool_size best performing individuals"""
        self.individuals = self.individuals[: self.pool_size]
        return
