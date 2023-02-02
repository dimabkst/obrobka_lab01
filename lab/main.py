import os
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    try:

        VARIANT = 2

        T = 5

        x_i = []

        file_path = f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\\test{VARIANT}.txt'

        with open(file_path, 'r', encoding='utf-8') as file:
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

        fig, ax = plt.subplots()
        ax.plot(t, x_i)
        ax.set_xlabel('t')
        ax.set_ylabel('x')
        plt.show()

    except Exception as e:
        print('Error occured:', e, sep='\n')
