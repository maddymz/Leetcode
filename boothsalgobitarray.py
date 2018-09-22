from bitarray import bitarray

'''
   Returns m * r using Booth's algorithm.
   x = len(m) and y = len(r). Note that this is the length in base 2.
   See http://en.wikipedia.org/wiki/Booth%27s_algorithm
'''
def booth(m, r, x, y):
	# Initialize
	totalLength = x + y + 1
	mA = bitarray(int = m, length = totalLength)
	rA = bitarray(int = r, length = totalLength)
	A = mA << (y+1)
	S = bitarray(int = -m, length = totalLength)  << (y+1)
	P = bitarray(int = r, length = y)
	P.prepend(bitarray(int = 0, length = x))
	P = P << 1
	print ("Initial values")
	print ("A", A.bin)
	print ("S", S.bin)
	print ("P", P.bin)
	print ("Starting calculation")
	for i in range(1,y+1):
		if P[-2:] == '0b01':
			P = bitarray(int = P.int + A.int, length = totalLength)
			print ("P +  A:", P.bin)
		elif P[-2:] == '0b10':
			P = bitarray(int = P.int +S.int, length = totalLength)
			print ("P +  S:", P.bin)
		P = arith_shift_right(P, 1)
		print ("P >> 1:", P.bin)
	P = arith_shift_right(P, 1)
	print ("P >> 1:", P.bin)
	return P.int

def arith_shift_right(x, amt):
	l = x.len
	x = bitarray(int = (x.int >> amt), length = l)
	return x

# Sample usage: find 86 * 41
b = booth(86, 41, 8, 8)
print (b)