class NutritionInfo:
    def __init__(self, proteins, carbs, fats):
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats

    def __add__(self, other):
        return NutritionInfo(self.proteins + other.proteins, self.carbs + other.carbs, self.fats + other.fats)

    def __mul__(self, other):
            return NutritionInfo(self.proteins * other, self.carbs * other, self.fats * other)

    def __str__(self):
        return f"Nutrition p {self.proteins}, c {self.carbs}, f {self.fats}"

    def energy(self):
        return int(self.fats * 9 + (self.carbs + self.proteins) * 4.2)


apple = NutritionInfo(0, 25, 0)
pastila = NutritionInfo(1, 2, 3)
tvorog_9 = NutritionInfo(18, 3, 9)
breakfast_summ = apple + tvorog_9 + pastila
breakfast_three_apple = apple * 3
print('Сложение разных ингредиентов:', breakfast_summ.energy(), 'calories')
print('Apple * 3:', breakfast_three_apple.energy(), 'calories')