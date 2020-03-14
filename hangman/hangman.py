# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.masked = "_" * len(word)
        self.word = word

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("game is finished")
        elif char in self.masked:
            self.remaining_guesses -= 1
            return
        i = 0
        did = False
        if char in self.word:
            for ch in self.word:
                if ch == char:
                    self.masked = self.masked[0:i] + char + self.masked[i + 1:]
                    did = True
                i += 1
        if not did:
            self.remaining_guesses -= 1

    def get_masked_word(self):
        return self.masked

    def get_status(self):
        if "_" not in self.masked:
            self.status = STATUS_WIN
        elif "_" in self.masked and self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        return self.status
