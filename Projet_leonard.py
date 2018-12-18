import sympy as sym
x = sym.symbols('x')

def func(x1, y1, x2, y2, p, N0) :
    a = (x1+y1) / y1
    b = 1 - a * (1 - x1)
    c = (x2 + y2) / y2
    d = 1 - c * (1 + x2)
    f = sym.Piecewise((p*x,x<(1-x1-y1)*N0), (a*p*x + b*p*N0,x<(1-x1)*N0), (p*N0,x<(1+x2)*N0), (c*p*x + d*p*N0,x<(1+x2+y2)*N0), (p*x,x<True))
    print(a,b,c,d)
    return f
    
test = func(0.1,0.1,0.1,0.1,5,10)

#sym.plotting.plot(test)
test.evalf(2)