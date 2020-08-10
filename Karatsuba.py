x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

def karatsuba(x,y):

	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		half = n // 2
		
		a = x // 10 ** half
		b = x % 10 ** half
		c = y // 10 ** half
		d = y % 10 ** half
		
		ac = karatsuba(a,c)
		bd = karatsuba(b,d)
		adbc = karatsuba(a+b,c+d) - ac - bd
        

		prod = ac * 10**(2*half) + (adbc * 10 ** half) + bd

		return prod

print(karatsuba(x,y))