from sympy import symbols, Eq, solve, integrate
A1, x1, A2, x2, x = symbols('A1 x1 A2 x2 x')
equations = [Eq(A1 + A2, integrate(1, (x, -1, 1))), 
            Eq(A1 * x1 + A2 * x2, integrate(x, (x, -1, 1))),
            Eq(A1 * x1 ** 2 + A2 * x2 ** 2, integrate(x ** 2, (x, -1, 1))),
            Eq(A1 * x1 ** 3 + A2 * x2 ** 3, integrate(x ** 3, (x, -1, 1)))
            ]
solve(equations, A1, x1, A2, x2, dict = True)
