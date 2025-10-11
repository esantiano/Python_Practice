class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result, soln = [],[]
        n = len(candidates)
        def backtrack(ind, total):
            if total == target:
                result.append(soln[:])
            elif total < target:
                for j in range(ind,n):
                    soln.append(candidates[j])
                    backtrack(j,total+candidates[j])
                    soln.pop()
            return result

        return backtrack(0,0)