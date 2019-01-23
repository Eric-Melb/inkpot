

def first_reported_list_result(input_list, start_value, reached_set):
        summed_value = start_value
        reached_values = reached_set
        for value in input_list:
                summed_value += int(value)
                if summed_value in reached_values:
                        return summed_value
                else:
                        reached_values.add(summed_value)

        result = first_reported_list_result(
                input_list,
                summed_value,
                reached_values
        )

        return result


def day2():
        with open("input.txt", "r") as file:
                input_list = list(file)

        start_value = 0
        reached_set = set()

        print(
                first_reported_list_result(
                        input_list,
                        start_value,
                        reached_set
                )
        )


if __name__ == '__main__':
    day2()
