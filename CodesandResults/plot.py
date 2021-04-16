import matplotlib.pyplot as plt
plt.clf()
x = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
l1 = [1.11, 1.61, 2.16, 2.67, 2.77, 3.89, 3.56, 3.83, 3.94]
l2 = [4.41, 4.39, 4.41, 4.29, 4.24, 4.21, 4.29, 4.24, 4.29]

plt.plot(x, l1, '-o', label='Dataset1')
plt.plot(x, l2, '-o', label='Dataset2')
# plt.plot(x, l1, '-s', label='Dataset1', color='r')
# plt.plot(x, l2, '-s', label='Dataset2', color='b')
plt.xlabel('k', fontsize=18)
plt.ylabel('Average Index', fontsize=18)
plt.title('Average Index', fontsize=18)
plt.legend()
plt.show()