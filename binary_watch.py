#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
A binary watch has 4 LEDs on the top which represent the hours (0-11),
and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are
currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero,
for example "10:2" is not valid, it should be "10:02".
"""


class Solution(object):
    hours = [8, 4, 2, 1]
    minutes = [32, 16, 8, 4, 2, 1]

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        # answer_hour = []
        # answer_min = []
        answer = {"hour": [], "min": []}
        # self.find_display(res, answer, num)
        # self.find_display_2(res, answer, num)
        # self.find_display_3(res, answer, num, 0, 0)
        self.find_display_4(res, answer, num, self.hours, self.minutes)
        return res

    def find_display(self, res, answer, nums):
        if nums == 0:
            # res.append(answer[:])  # answer is dict, [:] not usable
            answer_str = self.convert_format(answer)
            if answer_str not in res:
                res.append(answer_str)
            return

        for i in range(nums):
            # when the number stands for hour
            for hour_num in self.hours:
                current_digit = hour_num

                # ensure digit not be used 2 times.
                if sum(answer["hour"]) + current_digit <= 11 \
                        and current_digit not in answer["hour"]:
                # if sum(answer["hour"]) + current_digit <= 11:
                    answer["hour"].append(current_digit)
                    # answer["min"].append(0)
                    self.find_display(res, answer, nums - 1)
                    # answer["min"].pop()
                    answer["hour"].pop()

            # when the num stands for minute
            for min_num in self.minutes:
                current_digit = min_num

                if sum(answer["min"]) + current_digit <= 59 \
                        and current_digit not in answer["min"]:
                # if sum(answer["min"]) + current_digit <= 59:
                #     answer["hour"].append(0)
                    answer["min"].append(current_digit)
                    self.find_display(res, answer, nums - 1)
                    answer["min"].pop()
                    # answer["hour"].pop()

    def find_display_2(self, res, answer, nums):
        if nums == 0:
            answer_str = self.convert_format(answer)
            if answer_str not in res:
                res.append(answer_str)
            return

        for i in range(nums):
            # when the number stands for hour
            for hour_num in self.hours:
                current_digit = hour_num

                # ensure digit not be used 2 times.
                if sum(answer["hour"]) + current_digit <= 11 \
                        and current_digit not in answer["hour"]:
                    answer["hour"].append(current_digit)
                    self.find_display_2(res, answer, nums - 1)
                    answer["hour"].pop()

            # when the num stands for minute
            for min_num in self.minutes:
                current_digit = min_num

                if sum(answer["min"]) + current_digit <= 59 \
                        and current_digit not in answer["min"]:
                    answer["min"].append(current_digit)
                    self.find_display_2(res, answer, nums - 1)
                    answer["min"].pop()

    def find_display_3(self, res, answer, nums, hour_index, min_index):
        if nums == 0:
            answer_str = self.convert_format(answer)
            if answer_str not in res:
                res.append(answer_str)
            return

        for _ in range(nums):
            # when the number stands for hour
            for i in range(hour_index, len(self.hours)):
                current_digit = self.hours[i]

                # ensure digit not be used 2 times.
                if sum(answer["hour"]) + current_digit <= 11 \
                        and current_digit not in answer["hour"]:
                    answer["hour"].append(current_digit)
                    self.find_display_3(res, answer, nums - 1, hour_index+1, min_index)
                    answer["hour"].pop()

            # when the num stands for minute
            for j in range(min_index, len(self.minutes)):
                current_digit = self.minutes[j]

                if sum(answer["min"]) + current_digit <= 59 \
                        and current_digit not in answer["min"]:
                    answer["min"].append(current_digit)
                    self.find_display_3(res, answer, nums - 1, hour_index, min_index+1)
                    answer["min"].pop()

    def find_display_4(self, res, answer, nums, hours, minutes):
        if nums == 0:
            answer_str = self.convert_format(answer)
            if answer_str not in res:
                res.append(answer_str)
            return

        for num_count in range(nums):
            # when the number stands for hour
            for i in range(0, len(hours)):
                # there are at most 4 led in hour
                if num_count > 3:
                    break
                current_digit = hours[i]
                # current_digit not in answer["hour"]:
                # remove dup is done by hours[i+1:], used element not pass.
                if sum(answer["hour"]) + current_digit <= 11:
                    answer["hour"].append(current_digit)
                    self.find_display_4(res, answer, nums - 1, hours[i+1:], minutes)
                    answer["hour"].pop()

            # when the num stands for minute
            for j in range(0, len(minutes)):
                if num_count > 6:
                    break
                current_digit = minutes[j]

                if sum(answer["min"]) + current_digit <= 59:
                    answer["min"].append(current_digit)
                    self.find_display_4(res, answer, nums - 1, hours, minutes[j+1:])
                    answer["min"].pop()

    @staticmethod
    def convert_format(answer):
        answer_hour = answer["hour"]
        answer_min = answer["min"]
        hour = str(sum(answer["hour"])) if answer_hour else "0"
        minute = str(sum(answer["min"])) if answer_min else "0"

        if len(minute) == 1:
            minute = "0" + minute
        return "%s:%s" % (hour, minute)


if __name__ == "__main__":
    test_num = 5
    print(Solution().readBinaryWatch(test_num))

    # todo: time limit exceeded.

    # ["0:03", "0:05", "0:06", "0:09", "0:10", "0:12", "0:17", "0:18", "0:20",
    #  "0:24", "0:33", "0:34", "0:36", "0:40", "0:48", "1:01", "1:02", "1:04",
    #  "1:08", "1:16", "1:32", "2:01", "2:02", "2:04", "2:08", "2:16", "2:32",
    #  "3:00", "4:01", "4:02", "4:04", "4:08", "4:16", "4:32", "5:00", "6:00",
    #  "8:01", "8:02", "8:04", "8:08", "8:16", "8:32", "9:00", "10:00"]
















