class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        k=len(arr)
        for i in range(k):
            for j in range(k):
                if i!=j and arr[i] == 2 * arr[j] :
                    return True
        return False            
        