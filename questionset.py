import numpy as np
from typing import Optional


class Questionset:
    def __init__(
        self,
        n_questions_1: int,
        n_questions_2: int,
        question_selection: Optional[np.ndarray] = None,
    ):
        self.n_questions_1 = n_questions_1
        self.n_questions_2 = n_questions_2
        self.fitness_score = None

        if question_selection is not None:
            self.question_selection = question_selection
        else:
            self.random_init(n_questions_1, n_questions_2)

    def random_init(self, n_questions_1: int, n_questions_2: int) -> None:
        """
        Fill self.question_selection with a random question selection
        based on n_questions_1 and n_questions_2
        """
        arr = np.array(
            [0] * (25 - n_questions_1 - n_questions_2)
            + [1] * n_questions_1
            + [2] * n_questions_2
        )
        np.random.shuffle(arr)
        self.question_selection = arr
        return

    def mutate(self, n_switches):
        """
        Returns a copy of this Questionset with n_switches questions switched.
        """
        new_question_selection = self.question_selection.copy()
        for _ in range(n_switches):
            i1 = np.random.randint(25)
            i2 = np.random.randint(25)
            new_question_selection[[i1, i2]] = new_question_selection[[i2, i1]]
        return Questionset(
            question_selection=new_question_selection,
            n_questions_1=self.n_questions_1,
            n_questions_2=self.n_questions_2,
        )

    def __lt__(self, other) -> bool:
        """
        This function is necessary to compare Questionset objects when the
        fitness function of both Questionsets is the same value
        """
        return self.question_selection[0] < other.question_selection[0]
