# def get_average():
#     with open('files/data.txt', 'r') as file:
#         data = [x.strip('\n') for x in file.readlines()][1:]
#         values = [float(x) for x in data]
#         avg = sum(values)/len(values)
#     return avg
#
#
# average = get_average()
# print(average)

def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum


celsius_1 = get_maximum()
print(celsius_1)
fahrenheit = celsius_1 * 1.8 + 32.0

print(fahrenheit)
