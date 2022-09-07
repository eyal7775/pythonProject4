# ax^3 + bx^2 +cx + d = 0
# ax^3 + bx^2 +cx + d = a(x - x1)(x - x2)(x - x3)
# connections:
# x1 + x2 + x3 = -b/a
# x1x2 + x1x3 + x2x3 = c/a
# x1x2x3 = -d/a
import math

def solve_cubic_equation(a,b,c,d):
    q = (3*a*c - b*b)/(9*a*a)
    r = (9*a*b*c - 27*a*a*d - 2*b*b*b)/(54*a*a*a)
    s = math.pow(r + math.sqrt(q*q*q + r*r),1/3)
    t = math.pow(r - math.sqrt(q*q*q + r*r),1/3)
    x1 = s + t - b/(3*a)
    print("x1 = " + str(x1))
    x2 = complex(- 0.5 * (s + t) - b/(3*a), math.sqrt(3)/2 * (s - t))
    print("x2 = " + str(x2))
    x3 = complex(- 0.5 * (s + t) - b/(3*a), - math.sqrt(3) / 2 * (s - t))
    print("x3 = " + str(x3))

print(solve_cubic_equation(1,-2,-3,-20))
print(solve_cubic_equation(1,-6,11,-6))