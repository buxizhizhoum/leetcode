#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""


class Solution(object):
    calc_tokens = ("+", "-", "*", "/")

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        return self.ans_refer_from_web(tokens)
        # return self.ans_1(tokens)

    def ans_refer_from_web(self, tokens):
        stack = []
        for token in tokens:
            if token not in self.calc_tokens:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    res = first + second
                    stack.append(res)
                elif token == "-":
                    res = first - second
                    stack.append(res)
                elif token == "*":
                    res = first * second
                    stack.append(res)
                elif token == "/":
                    if first * second < 0 and first % second != 0:
                        res = first // second + 1
                    else:
                        res = first // second
                    stack.append(res)
                else:
                    raise ValueError

        return stack[0]

    def ans_1(self, tokens):
        """
        inter from end of tokens, if pushed two digit to the stack, calculate
        res in stack until there are no continue digit at the top of stack,
        then continue to push token in tokens to stack
        :param tokens:
        :return:
        """
        stack = []
        i = len(tokens) - 1
        two_digit = False
        one_digit = False
        while i >= 0:
            token = tokens[i]
            # push to stack
            if token in self.calc_tokens:
                stack.append(token)
                one_digit = False
                i -= 1
                continue
            else:
                if len(stack) == 0:
                    stack.append(token)
                    i -= 1
                    one_digit = True
                    continue

                if one_digit is False:
                    stack.append(token)
                    i -= 1
                    one_digit = True
                    continue

                if one_digit is True:
                    stack.append(token)
                    i -= 1
                    two_digit = True

                if two_digit is True:
                    stack_flag = self.stack_calc(stack)
                    while stack_flag:
                        stack_flag = self.stack_calc(stack)
                    one_digit = True
                    two_digit = False

        while len(stack) > 1:
            self.stack_calc(stack)

        return int(stack[0])

    def stack_calc(self, stack):
        if len(stack) == 1:
            return False
        first = stack.pop()
        second = stack.pop()
        if second not in self.calc_tokens:
            calc = stack.pop()
            res = self.calculate(first, second, calc)
            # push res to stack
            stack.append(res)
            return True
        else:
            stack.append(second)
            stack.append(first)
            return False

    def calculate(self, first, second, calc):
        if ((first.startswith("-") and not second.startswith("-"))
                or (not first.startswith("-") and second.startswith("-"))) \
                and calc == "/":
            # res = str(-(abs(int(first)) / abs(int(second))))
            res = str(int(float(first)/float(second)))
            return res

        else:
            return str(eval(first + calc + second))


if __name__ == "__main__":
    test_input = ["2", "1", "+", "3", "*"]
    # test_input = ["4", "13", "5", "/", "+"]
    test_input = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

    # test_input = ["4", "-2", "/", "2", "-3", "-", "-"]
    print(Solution().evalRPN(test_input))





