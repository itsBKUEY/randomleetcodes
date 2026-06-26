class Solution:


    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arrayset = dict()
        nestarr = []
        extra = []
        final = []

        for i in range(len(arr1)):
            nestarr.append([ ])


        for i in range(len(arr2)):

            arrayset[arr2[i]] = i


        for num in arr1:
            if num in arrayset:
                nestarr[arrayset[num]].append(num) 
            else:
                extra.append(num)
            
        for arrs in nestarr:
            for items in arrs:
                final.append(items)
        
        extra.sort()

        final.extend(extra)


        return final 
