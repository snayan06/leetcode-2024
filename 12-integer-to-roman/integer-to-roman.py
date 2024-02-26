class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Converts an integer to a Roman numeral.

        Parameters:
        - num (int): The integer to be converted to a Roman numeral.

        Returns:
        - str: The Roman numeral representation of the input integer.
        """
        roman_mapping = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        result_components = []

        for value in sorted(roman_mapping.keys(), reverse=True):
            quotient, num = divmod(num, value)
            result_components.append(roman_mapping[value] * quotient)

        return ''.join(result_components)
