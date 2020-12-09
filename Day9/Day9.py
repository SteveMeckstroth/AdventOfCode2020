class XMAS:

    def __init__(self):
        with open("Day9Input.txt", "r") as f:
            self.input = [int(i) for i in f.readlines()]

    def find_invalid_number(self, preamble_length):
        for i in range(preamble_length, len(self.input)):
            res = self.input[i]

            pyramid = self.input[i - preamble_length: i]
            if res not in self.get_sums_from_pyramid(pyramid):
                return res

        return 0

    def get_sums_from_pyramid(self, pyramid):
        sums = []
        for i in range(0, len(pyramid)):
            for n in range(i + 1, len(pyramid)):
                sums.append(pyramid[i] + pyramid[n])

        return sums

    def get_numbers_that_sum_to(self, number):
        for i in range(0, len(self.input)):
            total = 0
            numbers = []
            for n in range(i, len(self.input)):
                total += self.input[n]
                numbers.append(self.input[n])

                if total == number:
                    return numbers

        return []

    def get_min_and_max_from_list(self, numbers):
        pass


if __name__ == "__main__":
    x = XMAS()
    print("Part 1.")
    print(f"{x.find_invalid_number(25)} does not satisfy the algorithm!")
    print("Part 2.")
    numbers = x.get_numbers_that_sum_to(x.find_invalid_number(25))
    print(f"Sum of minimum and maximum numbers: {min(numbers) + max(numbers)}")

