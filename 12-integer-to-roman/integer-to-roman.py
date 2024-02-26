class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Converts an integer to a Roman numeral.

        Parameters:
        - num (int): The integer to be converted to a Roman numeral.

        Returns:
        - str: The Roman numeral representation of the input integer.
        """
        # Mapping between integer values and their corresponding Roman numeral symbols
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

        # Initialize an empty string to store the Roman numeral representation
        result = ""
        while num>0:
        # Iterate through the mapping in descending order of values
            for value in sorted(roman_mapping.keys(), reverse=True):
                if num >= value:
                    result += roman_mapping[value]
                    num -= value
                    break


        return result
