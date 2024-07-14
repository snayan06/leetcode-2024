from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        counts = defaultdict(int)
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == "(":
                stack.append("(")
                i += 1
            elif formula[i] == ")":
                i += 1
                count = 0
                while i < n and formula[i].isdigit():
                    count = count * 10 + int(formula[i])
                    i += 1
                if count == 0:
                    count = 1

                temp_count = defaultdict(int)
                while stack and stack[-1] != "(":
                    elem, c = stack.pop()
                    temp_count[elem] += c * count

                stack.pop()  # Remove '('
                for elem, c in temp_count.items():
                    stack.append((elem, c))
                continue  # Skip the incrementing of i since we processed the parentheses
            elif formula[i].isalpha() and formula[i].isupper():
                element = formula[i]
                i += 1
                while i < n and formula[i].islower():
                    element += formula[i]
                    i += 1
                
                count = 0
                while i < n and formula[i].isdigit():
                    count = count * 10 + int(formula[i])
                    i += 1
                if count == 0:
                    count = 1

                stack.append((element, count))
                continue  # Skip incrementing i
            else:
                i += 1
        
        # Count occurrences
        for elem, c in stack:
            counts[elem] += c

        # Prepare result
        result = []
        for element in sorted(counts):
            result.append(element)
            if counts[element] > 1:
                result.append(str(counts[element]))

        return ''.join(result)

