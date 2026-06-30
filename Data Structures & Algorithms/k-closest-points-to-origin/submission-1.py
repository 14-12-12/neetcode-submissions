import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr_distance = []
        for i in range (0, len(points)):
            distance = math.sqrt((points[i][0] - 0)**2 + (points[i][1] - 0)**2)
            arr_distance.append(distance)
        for i in range(1, len(arr_distance)):
            j = i-1
            while(j>=0 and arr_distance[j+1]<arr_distance[j]):
                temp1 = points[j]
                points[j] =points[j+1]
                points[j+1] = temp1

                temp= arr_distance[j]
                arr_distance[j] =arr_distance[j+1]
                arr_distance[j+1] = temp
                j = j-1
        for i in range(k,len(points)):
            points.pop()
        return points



                


        