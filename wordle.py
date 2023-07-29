from letter_state import LetterState

class Wordle:
    MAX_ATTEMPTS = 6
    MAX_LENGTH = 5

    def __init__(self, secrect: str):
        self.secrect : str = secrect.upper()
        self.attempts = []
    
    def attempt(self, guess: str):
        self.attempts.append(guess.upper())

    @property
    def solved(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secrect
    @property    
    def guesses_remaining(self) -> int:
        return self.MAX_ATTEMPTS - len(self.attempts)

    @property
    def attemptable(self):
        return self.guesses_remaining > 0 and not self.solved
    
    

    def guess(self, word: str):
        result = []
        for i in range(self.MAX_LENGTH):
            char = word[i]
            letter = LetterState(char)
            letter.in_word = char in self.secrect
            letter.in_position = char ==self.secrect[i] 
            result.append(letter)

            
        return result
    
    

    
                



        
    


    

