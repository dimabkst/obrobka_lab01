import os
from utils import draw_plot
import numpy as np


def second_task(T: float, delta_t: float, approximation_delta_t: float) -> list:
    try:
        x_i = []

        test_file_path = \
            f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\\test.txt'

        # read test.txt
        with open(test_file_path, 'r', encoding='utf-8') as file:
            line = file.readline()
            while line:
                for el in line.split(' '):
                    if el:
                        x_i.append(float(el))
                line = file.readline()

        N = len(x_i)
        # First and last elements when T=0 and T=1, so there would be N - 1 segmentsS
        d = T / (N - 1)
        if (d != delta_t):
            print('Provided delta_t is incorrect')
        N -= 1  # In formula N is T / delta_t and not the number of x_i

        # np.arange doesn't include stop value
        plot_t = np.arange(0, T + delta_t, delta_t)
        # plot of values from text.txt
        draw_plot(xdata=plot_t, ydata=x_i, xlabel='t', ylabel='x',
                  title="Plot of values from test.txt")

        approximated_x_t = []
        approximation_N = int(T / approximation_delta_t) + \
            1  # +1 so 0 is counted
        for i in range(approximation_N):
            temp_sum = 0
            t = i * approximation_delta_t  # equals to t in the formula
            for k in range(N + 1):
                temp_value = np.pi * N * t / T - k * np.pi
                if temp_value == 0:
                    temp_sum += x_i[k]  # because sin(0) / 0 == 1
                else:
                    # In formula we have x(k * T / N) and that is equal to x_i[k] due to T / N = delta_t
                    temp_sum += x_i[k] * np.sin(temp_value) / temp_value
            approximated_x_t.append(temp_sum)

        # plot approximated values
        approximated_plot_t = np.arange(0, T + approximation_delta_t,
                                        approximation_delta_t)  # np.arange doesn't include stop value
        draw_plot(xdata=approximated_plot_t,
                  ydata=approximated_x_t, xlabel='t', ylabel='x(t)',
                  title='Plot of approximated x(t)')

        return approximated_x_t
    except Exception as e:
        raise e
