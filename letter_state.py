class LetterState:
    def __init__(self, Character: str):
        self.Character: str = Character
        self.in_word: bool = False
        self.in_position: bool = False
    
    def __repr__(self):
        return f"[{self.Character} in_word: {self.in_word} in_position: {self.in_position}]"
