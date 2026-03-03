class ObiektTestowy():
    def __init__(self) -> None:
        self.liczba = 5
        
    def increase(self) -> None:
        self.liczba += 1
        return None
    
    def returner(self) -> int:
        return self.liczba