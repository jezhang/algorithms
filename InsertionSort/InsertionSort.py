
def insertion_sort(a):
	# for j in range(len(a)):
	# 	print j
	j = 1
	while(j < len(a)):
		key = a[j]
		i = j - 1
		while(i >= 0 and a[i] > key):
			a[i+1] = a[i]
			i = i - 1
		a[i+1] = key
		j = j + 1
	return a

def read_file():
    f = open('numbers.txt','r')
    a = [int(x) for x in f.read().split(',')]
    f.close()
    return a

def gen_int_numbers(1000):
	




def main():
	gen_int_numbers(1000)
    a = read_file()
    print(insertion_sort(a))

if __name__ == '__main__':
	main()
	# raw_input('Please enter any key to exit.')