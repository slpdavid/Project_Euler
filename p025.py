import numpy as np

fb_matrix = np.array([[1,1],[1,0]])
fb_sequence = np.array([[1,1],[1,0]])
digit = 1
index = 2
while True:
    fb_sequence = np.matmul(fb_sequence, fb_matrix)
    index += 1
    if fb_sequence[0][0] >= 10:
        fb_sequence = fb_sequence / 10
        digit += 1
    if digit % 50 == 0:
        print('Current digit:', digit)
        print('Current index:', index)
        print('Current Fibonacci number:', fb_sequence[0][0])
        print('')
    if digit >= 1000:
        break

print('Result Fibonacci number =', fb_sequence[0][0])
print('Total digit:', digit)
print('Index:', index)