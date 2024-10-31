class maths:    
    """Mathematical operations class, including functions for minimum, maximum, mean, mode, median,
    length, and sorting of iterables."""

    def minimum(*numbers):
        """
        Find the minimum value in an iterable.

        Parameters:
            *numbers (iterable): An iterable such as a list, tuple, or set containing numeric values.

        Returns:
            smallest (numeric): The smallest value in the iterable.
        """
        numbers = list(numbers[0])  # Convert the input (list, tuple, set) to a list
        smallest = numbers[0]
        for num in numbers:
            if smallest > num:
                smallest = num
        return smallest

    def maximum(*numbers):
        """
        Find the maximum value in an iterable.

        Parameters:
            *numbers (iterable): An iterable such as a list, tuple, or set containing numeric values.

        Returns:
            largest (numeric): The largest value in the iterable.
        """
        numbers = list(numbers[0])
        largest = numbers[0]
        for num in numbers:
            if largest < num:
                largest = num
        return largest

    def mean(*numbers):
        """
        Calculate the mean (average) of an iterable.

        Parameters:
            *numbers (iterable): An iterable containing numeric values.

        Returns:
            float: The mean value of the iterable.
        """
        numbers = list(numbers[0])
        sum = 0
        for num in numbers:
            sum += num
        return sum / maths.length(numbers)

    def mode(*numbers):
        """
        Find the mode(s) of an iterable, which is the most frequently occurring value(s).

        Parameters:
            *numbers (iterable): An iterable containing numeric values.

        Returns:
            modes (numeric or list): The mode value(s) of the iterable. Returns a list if multiple modes exist.
        """
        numbers = list(numbers[0])
        curr_num = {}
        for num in numbers:
            if num not in curr_num:
                curr_num[num] = 0
            curr_num[num] += 1
        max_freq = maths.maximum(curr_num.values())
        modes = []
        for key, value in curr_num.items():
            if value == max_freq:
                modes.append(key)
        return modes if len(modes) > 1 else modes[0]

    def median(*numbers):
        """
        Find the median (middle value) of an iterable.

        Parameters:
            *numbers (iterable): An iterable containing numeric values.

        Returns:
            float: The median value of the iterable.
        """
        numbers = list(numbers[0])
        sorted_list = maths.sort(numbers)
        length = maths.length(numbers)
        mid = length // 2
        return sorted_list[mid] if length % 2 == 1 else (sorted_list[mid] + sorted_list[mid - 1]) / 2

    def length(numbers):
        """
        Calculate the length (number of elements) of an iterable.

        Parameters:
            numbers (iterable): An iterable containing numeric values.

        Returns:
            int: The length of the iterable.
        """
        count = 0
        for i in numbers:
            count += 1
        return count

    def sort(numbers):
        """
        Sort an iterable in ascending order using a simple sorting algorithm.

        Parameters:
            numbers (iterable): An iterable containing numeric values.

        Returns:
            list: A sorted list in ascending order.
        """
        num = list(numbers)
        for i in range(maths.length(numbers) - 1):
            for j in range(i, maths.length(numbers)):
                if num[i] > num[j]:
                    num[i], num[j] = num[j], num[i]
        return num


class others:
    """Utility functions unrelated to mathematics, such as OTP generation."""

    def OTP(ndigits):
        """
        Generate a One-Time Password (OTP) with the specified number of digits.

        Parameters:
            ndigits (int): The number of digits for the OTP.

        Returns:
            str: The generated OTP as a string of digits.
        """
        OTP = ""  # Initialize OTP as an empty string
        for i in range(ndigits):  # Loop through the number of digits
            random_digit = math.floor(random.random() * 10)  # Generate a random digit
            OTP += str(random_digit)  # Append the random digit to the OTP
        return OTP  # Return the generated OTP
