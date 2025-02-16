class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        lst = []
        while(matrix):
            array1 = matrix.pop(0)
            for i in array1:
                lst.append(i)

            if(matrix and matrix[0]):
                for i in matrix:
                    x = i.pop()
                    lst.append(x)
                
            if(matrix):
                temp = matrix.pop()
                for i in range(len(temp)-1,-1,-1):
                    lst.append(temp[i])
            
            if(matrix and matrix[0]):
                for i in range(len(matrix)-1,-1,-1):
                    cur = matrix[i].pop(0)
                    lst.append(cur)
        
        return lst