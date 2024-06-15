class Solution(object):
    def combinationSum(self, candidates, target):
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                path.append(candidates[i])
                # Note: We can reuse the same element, so start remains the same
                backtrack(i, target - candidates[i], path)
                path.pop()

        result = []
        candidates.sort()  # Sort the candidates to handle duplicates and improve efficiency
        backtrack(0, target, [])
        return result

