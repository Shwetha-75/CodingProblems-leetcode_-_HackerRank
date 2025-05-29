class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        stack=[(0,groups[0])]
        for i in range(1,len(groups)):
            if stack[-1][-1]!=groups[i]:
                stack.append((i,groups[i]))
        return [words[i[0]] for i in stack]