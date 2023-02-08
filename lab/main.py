from first_task import first_task
from second_task import second_task


if __name__ == "__main__":
    try:
        # Task №1
        VARIANT = 2
        T = 5
        frequencies = first_task(VARIANT, T)
        print(*[f'Frequence: {frequency}, Coefficient absolute value: {coefficient_abs}' for
                frequency, coefficient_abs in frequencies.items()], sep='\n')

        # Task №2
        T = 1
        delta_t = 0.05
        approximation_delta_t = 0.001
        approximated_x_t = second_task(T, delta_t, approximation_delta_t)

    except Exception as e:
        print('Error occured:', e, sep='\n')
