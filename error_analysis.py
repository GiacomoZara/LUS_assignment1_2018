import os
import operator

os.system("[ -e 09_all_together ] && rm errors.txt")

result_file = open('final_output.txt', 'r')

errors = {}

for line in result_file:
	split_line = line.split()
	if len(split_line) > 0:
		real = split_line[1]
		predicted = split_line[2]
		if not (real == predicted):
			if errors.get((real, predicted)):
				errors[(real, predicted)] += 1
			else:
				errors[(real, predicted)] = 1

result_file.close()

error_file = open('errors.txt', 'w')

sorted_errors = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)

for item in sorted_errors:
	error_file.write(str(item[0]) + ": " + str(item[1]) + "\n")

error_file.close()