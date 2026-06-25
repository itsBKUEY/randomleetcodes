class Solution:
#
# 
#
#For ever numb in
#

#return arry
    import heapq

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = dict()
        array = []
        for i in range(len(nums)+1):
            array.append([])

        result = []
  

        for num in nums:
            if num in freqmap:
                freqmap[num] += 1
            else:
                freqmap[num] = 1
        
        for key, val in freqmap.items():
            array[val].append(key)
         
        
        i = len(array)-1
        while(k >0 or i < 0):
            for n in array[i]:
                if(array[i]):
                    result.append(n)
                    k -= 1
            i -= 1
            
        
        
           

        return result
            

        