def le_calcul(r, delta):
    print("\nOn a C1(x) = D*x et C2(x) = D*((((1+r)^x)-1)/r), l'une est linéaire et l'autre exponentielle.\
          \nCa fait une équation transcendante qui ne se résout pas algébriquement.")
    print("Pour trouver la valeur de x pour laquelle C2(x) = delta * C1(x), \
il faut résoudre l'équation par dichotomie (car pas de première approximation).\
          \nCa va donner un truc f(x)=0 où f(x) = (1+r)^x - delta*r*x - 1.")

    def f(x):
        return (1+r)**x - delta*r*x - 1

    left, right = 0, 80
    epsilon = 1e-3

    while right - left > epsilon:
        mid = (left + right) / 2
        value = f(mid)

        if abs(value) < epsilon:
            return mid
        elif value > 0:
            right = mid
        else:
            left = mid

    return (left + right) / 2

if __name__ == "__main__":
    r = float(input("Valeur de r : "))
    delta = float(input("Valeur de delta : "))

    x = le_calcul(r, delta)
    print(f"\nC2(x) vaudra {delta} * C1(x) en x = {x:.2f}.")
