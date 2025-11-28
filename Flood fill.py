class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def dfs(sr,sc,image,color,n,m):
            for r,c in[[1,0],[-1,0],[0,-1],[0,1]]:#to travel top bottom right left (refer notes)
                nr=r+sr#new row
                nc=c+sc#new colummn
                if (nr>=0 and nr<n and nc>=0 and nc<m and image[nr][nc]==ele):
                    image[nr][nc]=color
                    dfs(nr,nc,image,color,n,m)
        if(color==image[sr][sc]):
            return image
        n=len(image)#rows
        m=len(image[0])#columns
        ele=image[sr][sc]
        image[sr][sc]=color
        dfs(sr,sc,image,color,n,m)
        return image

