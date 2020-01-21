# -*- coding: UTF-8 -*-

import numpy as np
 
def get_normal_random_number(mu, sigma, num):

	# mu 期望
	# sigma 标准差
	# num 个数

	rand_data = np.random.normal(mu, sigma, num)

	return rand_data

if __name__ == "__main__":

	n = get_normal_random_number(mu=100, sigma=30, num=10)

	int_n = []

	for i in n:
		i = int(i)
		int_n.append(i)

	print(int_n)

