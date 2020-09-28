"""
H. Разность треш-индексов

Даны 2 массива, отсортированные по неубыванию, а также число k. Нужно
Кондратий захотел выяснить k - ю минимальную разницу между значениями
треш-индексов городов Трешландии. Под разницей элементов a и b понимаем
|a - b|.

Формат ввода
В первой строке записано n - число городов, для которых известно значение
треш-индекса.
n не превосходит 10000.
В следующей строке через пробел записаны n значений треш - индекса, каждое из
которых не превосходит 1000000.
В последней строке задано число k. Оно находится в диапазоне
от 1 до n * (n - 1) / 2.

Формат вывода
Выведите k - ую минимальную разницу между парами значений треш - индексов.

https://medium.com/swlh/binary-search-find-k-th-smallest-pair-distance-91cce923c273
"""

from typing import List
import heapq, collections

def solution2(nums: List[int], k: int) -> int:
    """
    Function statement: return the pair's distance that is kth smallest
    Time complexity: O((n + k)log(n))
    Worst case: O(n^2log(n)) <- when k is large
    :param nums: all the possible pairing numbers
    :param k: target
    :return: kth smallest distance
    """
    # 1. Sort the nums array
    nums.sort()

    # 2. Get numbers' frequencies
    freq = collections.Counter(nums)
    keys = sorted(list(freq.keys()))

    # 3. Store n-1 sorted lists in a binary heap
    minHeap = [(keys[i + 1] - keys[i], i, i + 1) for i in
                range(len(keys) - 1)]
    heapq.heapify(minHeap)

    # 4. Count how many pairs' distance are 0
    cnt, rtn = 0, 0
    for key, val in freq.items():
        cnt += (val - 1) * val // 2

    # 5. Merge (len(nums) - 1) sorted lists
    while len(minHeap) > 0 and cnt < k:
        #  6. Pop the first k smallest pairs
        rtn, i, j = heapq.heappop(minHeap)
        k1, k2 = keys[i], keys[j]
        cnt += (freq[k1] * freq[k2])
        if j + 1 < len(keys):
            heapq.heappush(minHeap, (keys[j + 1] - keys[i], i, j + 1))

    # 7. Return the k-th smallest pair's distance
    return rtn

def solution(nums: List[int], k: int) -> int:
    """
    Function statement: return the pair's distance that is kth smallest (optimized solution)
    :param nums: all the pairing numbers
    :return: kth smallest distance
    """

    def findPairs(nums: List[int], d: int) -> int:
        """
        Function statement: return # of pairs with distance <= d
        :param nums: all the pairing numbers
        :param d: upper bound for pair's distance
        :return: # of pairs with distance <= d
        """
        i, j, cnt, n = 0, 0, 0, len(nums)
        for i in range(len(nums)):
            while nums[i] - nums[j] > d and j < i:
                j += 1
                cnt += (n - i)
        return n * (n - 1) // 2 - cnt

    # 1. Sort the nums array
    nums.sort()

    # 2. Initialize the left and right bounds as 0 and len(nums)-1
    l, r = min(nums[i + 1] - nums[i] for i in range(len(nums) - 1)), nums[
         -1] - nums[0]

    # 3. Binary search the distance
    while l <= r:
        mid = l + ((r - l) >> 1)
        # 4. Find # of pairs with distance <= the middle one
        if k <= findPairs(nums, mid):
            r = mid - 1
        else:
            l = mid + 1
    return l

def main(input_file):
    input_file = input_file.rstrip().split('\n')
    n = int(input_file[0])
    data = list(map(int, input_file[1].rstrip().split()))
    k = int(input_file[2])
    sol = solution(data, k)
    return str(sol)


if __name__ == '__main__':
    with open('input.txt') as f:
        input_file = f.read()
    answer = main(input_file)
    with open('output.txt', 'w') as f:
        f.write(answer)

    with open('input1.txt') as f:
        input_file = f.read()
    assert main(input_file) == '1', 'input1.txt error\n' + str(
        main(input_file))

    with open('input2.txt') as f:
        input_file = f.read()
    assert main(input_file) == '0', 'input2.txt error\n' + str(
        main(input_file))

    with open('input3.txt') as f:
        input_file = f.read()
    assert main(input_file) == '4', 'input3.txt error\n' + str(
        main(input_file))
