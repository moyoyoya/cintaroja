#madre de fizz buzz codeeval

"Sample code to read in test cases:"

import sys
test_cases = open(sys.argv[1], 'r')
contador = 1
resul = ''
for test in test_cases:
	if test.strip() != '':
		val = test.split()
		while contador-1 in range(int(val[2])):
			if contador%int(val[0]) == 0 and contador%int(val[1]) == 0:
				resul += 'FB'
			elif contador%int(val[0]) == 0:
				resul += 'F'
			elif contador%int(val[1]) == 0:
				resul += "B"
			else:
				resul += str(contador)
			contador += 1

		print(resul)

    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

test_cases.close()



