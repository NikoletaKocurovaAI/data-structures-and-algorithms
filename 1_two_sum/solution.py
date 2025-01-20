class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """
        :param nums: list[int]: Numbers to search through for pairs that sum to the target
        :param target: int: The target sum to find in nums
        :return: list[int] A list of two indices whose values add up to the target
        :example:
            two_sum([2, 7, 11, 15], 9) -> [0, 1]
        """
        return self._find_two_sum_indices(target, nums)

    @staticmethod
    def _find_two_sum_indices(target: int, elements: list[int]) -> list[int]:
        """
        Hash-map-based approach

        The single-pass solution where indices of seen numbers are stored using a hash map,
        while traversing once through the list.
        """
        if len(elements) < 2:
            return []

        num_to_index: dict[int, int] = {}

        for idx, element in enumerate(elements):
            complement: int = target - element

            if complement in num_to_index:
                return [num_to_index[complement], idx]

            num_to_index[element] = idx
        return []
