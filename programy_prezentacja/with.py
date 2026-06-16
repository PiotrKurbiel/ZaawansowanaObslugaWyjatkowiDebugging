



class ContextManager:
    def __init__(self):
        pass
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):


        pass


with open('test.txt', 'w') as plik:
    data = plik.read()

with ContextManager() as funckja_sprzatajaca:
    pass


from contextlib import contextmanager
@contextmanager
def ContextManager():
 #Manager z dekoratorem

 pass


