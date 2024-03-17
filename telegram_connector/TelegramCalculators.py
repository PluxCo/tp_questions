from core.answers import PointsCalculator, OpenRecord, TestRecord


class TelegramCalculator(PointsCalculator):
    """
    Represents a calculator for scoring answers.

    This calculator extends the PointsCalculator class and implements
    specific scoring methods for open and test questions.

    """

    def __init__(self):
        """
        Initializes a TelegramCalculator object.
        """
        super().__init__()

    def score_open(self, record: OpenRecord) -> float:
        """
        Scores an open question record.

        :param record: (:class:`OpenRecord`) The open question record to score.
        :return: (:class:`float`) The score for the open question.
        """
        # TODO: add neural network
        return 0.5

    def score_test(self, record: TestRecord) -> float:
        """
        Scores a test question record.

        :param record: (:class:`TestRecord`) The test question record to score.
        :return: (:class:`float`) The score for the test question.
        """
        if record.question.answer == record.person_answer:
            return 1
        return 0
