from sys import stderr


def sum_of_list(input_list):
        summed_value = 0
        for value in input_list:
                try:
                        summed_value += int(value)
                except ValueError:
                        stderr.write(
                                "\nSkipping {} - cannot convert\n".format(value)
                        )
                        continue
        return summed_value


def day1():
        with open("input.txt", "r") as file:
                input_list = list(file)

        print(sum_of_list(input_list))


if __name__ == '__main__':
    day1()
