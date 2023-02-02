import os
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    try:
        # Laboratory specifications
        VARIANT = 2
        T = 5

        x_i = []

        f0 = 1 / T

        testk_file_path = f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\\test{VARIANT}.txt'

        # read testk.txt
        with open(testk_file_path, 'r', encoding='utf-8') as file:
            line = file.readline()
            while line:
                for el in line.split(' '):
                    if el:
                        x_i.append(float(el))
                line = file.readline()

        N = len(x_i)
        # First and last elements when T=0 and T=5, so there would be N - 1 segmentsS
        d = T / (N - 1)

        t = np.arange(0, T + d, d)  # np.arange doesn't include stop value

        # plot values from textk.txt
        # fig, ax = plt.subplots()
        # ax.plot(t, x_i)
        # ax.set_xlabel('t')
        # ax.set_ylabel('x')
        # plt.show()

        cx_k = []
        for k in range(N):
            real_sum = 0
            imaginary_sum = 0
            for m in range(N):
                real_sum += x_i[m] * np.cos(-2 * np.pi * k * m / N)
                imaginary_sum += x_i[m] * np.sin(-2 * np.pi * k * m / N)

            cx_k.append((real_sum + imaginary_sum * 1j) / N)
        cx_k_abs = [abs(cx) for cx in cx_k]

        # plot values of cx_k_abs with coresponding N
        # fig, ax = plt.subplots()
        # ax.plot(np.arange(0, N, 1), cx_k_abs)
        # ax.set_xlabel('N')
        # ax.set_ylabel('cx_k_abs')
        # plt.show()

        # plot first half of values of cx_k_abs with coresponding frequency
        fig, ax = plt.subplots()
        ax.plot(np.arange(0,  (N // 2 + 1) * f0, f0), cx_k_abs[:N // 2 + 1])
        ax.set_xlabel('N')
        ax.set_ylabel('cx_k_abs')
        plt.show()

    except Exception as e:
        print('Error occured:', e, sep='\n')
