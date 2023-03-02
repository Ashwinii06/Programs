def find_mean(numbers):
    return sum(numbers)/len(numbers)




def find_median(numbers):
    if len(numbers)%2 == 0:
        return (numbers[(len(numbers)-1)//2] + numbers[(len(numbers)+1)//2])/2
    return numbers[len(numbers)//2]


def count_frequency(numbers, number):
    frequency = 0


    for i in range(len(numbers)):
        if numbers[i] == number:
            frequency += 1


    return frequency


def find_max_frequency(frequencies):
    return max(frequencies)


def find_modes(numbers):
    frequencies = []
    
    for number in numbers:
        frequency = count_frequency(numbers, number)
        frequencies.append(frequency)


    max_frequency = find_max_frequency(frequencies)
    modes = []
    
    for number in numbers:
        frequency = count_frequency(numbers, number)
        if frequency == max_frequency and number not in modes:
            modes.append(number)


    return modes


            


numbers = [2, 6, 3, 1, 8, 12, 2, 9, 10, 3, 4]
numbers.sort()


mean = find_mean(numbers)
median = find_median(numbers)
modes = find_modes(numbers)


print("Mean: ", round(mean,2))
print("Median: ", median)
print("Mode: ", end='')


for mode in modes:
    print(mode, end=" ")
