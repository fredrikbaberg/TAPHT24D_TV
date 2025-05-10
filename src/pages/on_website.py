import playwright


class Website:
    def __init__(self):
        self.page = playwright.goto(
            "https://tap-ht24-testverktyg.github.io/exam-template/"
        )
