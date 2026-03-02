from modules.objects import ObiektTestowy
from modules import objects as objekty

liczba: int = 1
zmienno_przecinkowa: float = 1.0
tekst: str = 'text'
lista: list = [1, 'text', liczba, 1, 2, 3, 4, 5, 6]
taple: tuple = (1, 2, 3)
secik: set = set(lista)
slownik: dict = {
    'liczba': liczba,
    'tekst': tekst
}
binarne: bool = True
obiekt1 = ObiektTestowy()
obiekt2 = objekty.ObiektTestowy()
obiekt1.increase()
liczba2 = obiekt1.returner()
print(liczba2)
