class Solution:
    def getSmallestString(self, s: str) -> str:
        parity = ""
        for char in s:
            if int(char) % 2:
                parity += "o"
            else:
                parity += "e"
        list_of_possible_strings = [s]
        s_list = list(s)
        print(parity)
        for i in range(len(parity) - 1):
            if (parity[i] == "o" and parity[i + 1] == "o") or (
                parity[i] == "e" and parity[i + 1] == "e"
            ):
                copy_s_list = s_list[:]
                copy_s_list[i], copy_s_list[i + 1] = copy_s_list[i + 1], copy_s_list[i]
                copy_s = "".join(copy_s_list)
                list_of_possible_strings.append(copy_s)
        print(list_of_possible_strings)
        list_of_possible_strings.sort()
        return list_of_possible_strings[0]
