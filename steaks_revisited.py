# by Kami Bigdely
# Extract class
WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05


def is_well_done(time, temperature, pressure, desired_state):
    return desired_state == 'well-done' and  \
        get_cooking_progress(time, temperature, pressure) >= WELL_DONE


def is_medium(time, temperature, pressure, desired_state):
    return desired_state == 'medium' and  \
        get_cooking_progress(time, temperature, pressure) >= MEDIUM


def get_cooking_progress(time, temperature, pressure):
    return time * temperature * pressure * COOKED_CONSTANT


def is_cookeding_criteria_satisfied(time, temperature,
                                    pressure, desired_state):
    if is_cookeding_criteria_satisfied(time, temp, pressure, desired_state):
        print('cooking is done.')
        return is_well_done(time, temperature, pressure, desired_state) or \
            is_medium(time, temperature, pressure, desired_state)
    print('not cooked')


time = 30  # [min]
temp = 103  # [celcius]
pressure = 20  # [psi]
desired_state = 'well-done'
