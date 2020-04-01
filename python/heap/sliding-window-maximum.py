# leetcode [239]
class Solution:
    @staticmethod
    def max_sliding_window(nums: [int], k: int) -> [int]:
        pass

    @staticmethod
    def max_sliding_window_with_queue(nums: [int], k: int) -> [int]:
        if not len(nums) or len(nums) < k:
            return []
        window, res = [], []
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i - k:
                window.pop(0)
            while len(window) and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res


if __name__ == '__main__':
    # test_nums = [1, 3, -1, -3, 5, 3, 6, 7]
    test_nums = [9, 8, 7, 6, 5, 4]
    k = 3

    print(Solution.max_sliding_window_with_queue(test_nums, k))
