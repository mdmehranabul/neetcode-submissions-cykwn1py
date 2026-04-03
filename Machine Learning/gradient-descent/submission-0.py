class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:

        for i in range(iterations):
            init-=2*init*learning_rate
        return round(init,5)    