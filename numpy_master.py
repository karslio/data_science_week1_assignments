import numpy as np
import time

i = 0
start = time.time()
while True:
    a = np.random.rand(10, 10)
    b = np.random.rand(10, 10)
    c = a - b
    diagonal = np.diagonal(c)
    if np.all(diagonal > -0.1) & np.all(diagonal < 0.1):
        break
    i += 1

end = time.time()
time = end - start
with open("print.txt", "w", encoding="utf-8") as file:
    file.write("""
import numpy as np
import time

i = 0
start = time.time()
while True:
    a = np.random.rand(10, 10)
    b = np.random.rand(10, 10)
    c = a - b
    diagonal = np.diagonal(c)
    if np.all(diagonal > -0.1) & np.all(diagonal < 0.1):
        break
    i += 1

end = time.time()
time = end - start
######################################################################
""")
    file.write('subtract_matrix :' + '\n' + str(c) + '\n')
    file.write('diagonal :' + str(diagonal) + '\n')
    file.write('number_of_loops :' + str(i) + '\n')
    file.write('total_time :' + str(time / 60) + ' minutes')
