class Solution:
#
# 
#
#count with Frequency map
# for (v, key) in freqap
# add (v,key) to heap sorted on v
# 
# for k 
# add top of heap  to aray
# pop top of heap
#
#return arry
    import heapq

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = dict()
        heap = []
        array = []
        
        for each in nums:
            if each in freqmap:
                freqmap[each] +=1
            else:
                freqmap[each] = 1
        

        for numb, count in freqmap.items():
            heapq.heappush(heap, (-count, numb))

        for i in range(k): 
            count, numb = (heapq.heappop(heap))
            array.append(numb)
           

        return array
            

        