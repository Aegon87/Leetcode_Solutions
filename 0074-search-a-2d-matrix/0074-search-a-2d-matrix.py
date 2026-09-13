class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Find the ROW with the element
        l1, r1 = 0, len(matrix)-1
        while l1 <= r1:
            row = (l1+r1)//2
            if target > matrix[row][-1]:
                l1 = row+1
            elif target < matrix[row][0]:
                r1 = row-1
            else:
                break
        
        if not (l1 <= r1):
            return False

        #find the element in the row-with-element
        row = (l1+r1)//2
        l2 , r2 = 0, len(matrix[0])-1
        while l2 <= r2:
            mid = (l2+r2)//2
            if target > matrix[row][mid]:
                l2 = mid+1
            elif target < matrix[row][mid]:
                r2 = mid - 1
            else:
                return True
        return False