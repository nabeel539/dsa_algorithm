from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Find two numbers in a sorted 1-indexed array that add up to target.
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                # Problem uses 1-based indexing
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    nums1, target1 = [2, 7, 11, 15], 9
    assert sol.twoSum(nums1, target1) == [1, 2], f"Failed on test 1"

    # Test Case 2
    nums2, target2 = [2, 3, 4], 6
    assert sol.twoSum(nums2, target2) == [1, 3], f"Failed on test 2"

    # Test Case 3
    nums3, target3 = [-1, 0], -1
    assert sol.twoSum(nums3, target3) == [1, 2], f"Failed on test 3"

    print("All Two Sum II test cases passed successfully!")
