# Decorator classes
class Multiplier:
    def __init__(self, multiplier) -> None:
        self._multiplier = multiplier

    def __call__(self, func):
        def internal (*args, **kwargs):
            result = func(*args, **kwargs)
            return result * self._multiplier
        return internal
    
@Multiplier(2)
def sum(x, y):
    return x * y

two_plus_two = sum(2,2)
print(two_plus_two)