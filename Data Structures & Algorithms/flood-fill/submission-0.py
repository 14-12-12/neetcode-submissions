class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        Rows, Cols = len(image), len(image[0])
        og_color = image[sr][sc]
        visit = set()
        def dfs(self, image:List[List[int]],sr: int, sc: int, color: int )-> List[List[int]]:
            if (min(sr,sc)<0 or sr == Rows or sc == Cols or image[sr][sc]!=og_color or (sr,sc) in visit):
                return 
            image[sr][sc] = color
            visit.add((sr,sc))
            dfs(self,image, sr+1,sc,color)
            dfs(self,image, sr-1,sc,color)
            dfs(self,image, sr,sc+1,color)
            dfs(self,image, sr,sc-1,color)
            return image
        image = dfs(self,image,sr,sc,color)
        return image


        