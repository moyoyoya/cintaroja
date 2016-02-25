#Sample code to read in test cases:

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test.strip() != '':
    	vals = test.split(',')
    	otra = [int(x.strip()) for x in vals]
    	while otra[0]>= otra[1]:
    		otra[0] -= otra[1]
    	print(otra[0])

    # ignore test if it is an empty line
    # 'test' represents the test case, do something with it
    # ...
    # ...

test_cases.close()
