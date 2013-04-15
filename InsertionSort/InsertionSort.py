import random

def insertion_sort(a):
	for j in range(1,len(a)):
		key = a[j]
		i = j - 1
		while i >= 0 and a[i] > key:
			a[i+1] = a[i]
			i = i - 1
		a[i+1] = key
	return a

def read_file():
    f = open('numbers.txt','r')
    a = [int(x) for x in f.read().split(';')]
    f.close()
    return a

def gen_int_numbers(x):
	# a = [str(random.randrange(1,1000)) for i in range(x)]
	a = [str(random.randint(1,1000)) for i in range(x)]
	a = list(set(a))		# Remove duplicates
	s = ';'.join([a[i] for i in range(len(a))])
	f = open('numbers.txt','w')
	f.write(s)
	f.close()

def main():
	gen_int_numbers(100)
    	a = read_file()
    	print(insertion_sort(a))

if __name__ == '__main__':
	main()
	# raw_input('Please enter any key to exit.')