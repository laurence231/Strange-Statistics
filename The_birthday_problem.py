import numpy as np
from matplotlib import pyplot as plt


def birthday_dictionary(num_people):
    '''
    initialise a dictionary of randomly allocated birthdays associated a number of people determined by num_people
    :param num_people:
    :return: dictionary of birthdays
    '''
    birthdays = {}
    for person in range(num_people):
        birthdays[person+1] = np.random.randint(1,365)
    return birthdays


def number_of_birthday_pairs(birthdays, multiple_occurences, single_occurences):
    '''
    this function tests if, in a given dictionary of people (with values of their birthdays),
    :param birthdays:
    :param multiple_occurences:
    :param single_occurences:
    :return:the appended values of only SINGLE occurences of birthdays, or if an instance of MULTIPLE occurences of 1 birthday happened
    '''
    birthday_dates = list(birthdays.values())
    for date in birthday_dates:
        N_occurences = birthday_dates.count(date)
        if N_occurences > 1:
            multiple_occurences += 1
            return multiple_occurences, single_occurences

    single_occurences += 1
    return multiple_occurences, single_occurences


results_dict = {}

for i in range(2,365,1):
    multiple_occurences = 0
    single_occurences = 0
    for _ in range(100):
        num_people = i
        birthdays = birthday_dictionary(num_people)
        (multiple_occurences, single_occurences) = number_of_birthday_pairs(birthdays, multiple_occurences, single_occurences)
    results_dict[i] = multiple_occurences


plt.plot(range(1,364,1), list(results_dict.values()))
plt.title('The Birthday Problem')
plt.ylabel('Percentage of tests with matching birthday pair ')
plt.xlabel('No. of People in sample')
plt.axis([0, 365, 0, 110])
plt.show()
