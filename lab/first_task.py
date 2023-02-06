import os
from utils import draw_plot
import numpy as np


def first_task(variant: int, T: float) -> list:
    try:
        x_i = []

        f0 = 1 / T

        testk_file_path = \
            f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\\test{variant}.txt'

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

        # plot of values from textk.txt
        draw_plot(xdata=t, ydata=x_i, xlabel='t', ylabel='x',
                  title=f'Plot of values from test{variant}.txt')

        cx_k = []
        for k in range(N):
            real_sum = 0
            imaginary_sum = 0
            for m in range(N):
                real_sum += x_i[m] * np.cos(-2 * np.pi * k * m / N)
                imaginary_sum += x_i[m] * np.sin(-2 * np.pi * k * m / N)

            cx_k.append((real_sum + imaginary_sum * 1j) / N)
        cx_k_abs = [abs(cx) for cx in cx_k]

        # plot values of cx_k_abs with corresponding k
        draw_plot(xdata=np.arange(0, N, 1), ydata=cx_k_abs, xlabel='k',
                  ylabel='cx_k_abs', title='Plot of cx_k absolute values corresponding to k')

        # plot first half of values of cx_k_abs with corresponding frequency
        draw_plot(xdata=np.arange(0,  (N // 2 + 1) * f0, f0),
                  ydata=cx_k_abs[:N // 2 + 1], xlabel='frequency', ylabel='cx_k_abs',
                  title='Plot of cx_k absolute values corresponding to frequency')

        impact_frequencies = {}
        for k in range(1, N // 2 + 2):
            if cx_k_abs[k - 1] < cx_k_abs[k] > cx_k_abs[k + 1]:
                impact_frequencies[k * f0] = cx_k_abs[k]

        return impact_frequencies
    except Exception as e:
        raise e
