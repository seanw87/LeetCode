import collections
import heapq
from typing import List


class Solution1:
    """
    Use collections.defaultdict so that no need for initialization manually
    """

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        class TrieNode:
            def __init__(self):
                self.children = collections.defaultdict(TrieNode)
                self.suggestions = []

            def add(self, product):
                if len(self.suggestions) < 3:
                    self.suggestions.append(product)

        products = sorted(products)
        root = TrieNode()
        for p in products:
            node = root
            for char in p:
                node = node.children[char]
                node.add(p)

        result = []
        node = root
        for char in searchWord:
            node = node.children[char]
            result.append(node.suggestions)
        return result


class Solution2:
    """
    Use heapq to do the sorting work
    """

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        class TrieNode:
            def __init__(self):
                self.children = collections.defaultdict(TrieNode)
                self.hres = []

            def add(self, product):
                if len(self.hres) < 3:
                    heapq.heappush(self.hres, MaxHeapStr(product))  # Use MaxHeapStr for sorting the elements in heapq
                else:
                    heapq.heappushpop(self.hres, MaxHeapStr(product))

            def get(self):
                return sorted(self.hres, reverse=True)

        class MaxHeapStr(str):
            def __init__(self, string): self.string = string

            def __lt__(self, other): return self.string > other.string

            def __eq__(self, other): return self.string == other.string

        root = TrieNode()
        for p in products:
            node = root
            for char in p:
                node = node.children[char]
                node.add(p)

        result = []
        node = root
        for char in searchWord:
            node = node.children[char]
            result.append(node.get())
        return result


class Solution3:
    """
    Use BinarySearch
    """

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        sorted_list = sorted(products)
        start, end = 0, len(sorted_list) - 1
        result = []

        for i, char in enumerate(searchWord):
            while start <= end and (i >= len(sorted_list[start]) or sorted_list[start][i] != char):
                start += 1
            while start <= end and (i >= len(sorted_list[end]) or sorted_list[end][i] != char):
                end -= 1

            result.append(sorted_list[start:min(start + 3, end + 1)])
            return result
