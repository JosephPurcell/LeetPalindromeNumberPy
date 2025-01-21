# This is a sample Python script.
from collections import deque


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#Leet stats
#Runtime 4ms - Beats 80.68%
#Memory 17.80MB - Beats 39.19%

class Solution:
    def isPalindrome(self, x: int) -> bool:
        stack = deque()
        string_x = str(x)
        for i in string_x:
            stack.append(i)

        for i in string_x:
            if i != stack.pop():
                return False

        return True


