class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * (len(temp))
        st = []

        for i in range(len(temp)):
            while st and temp[i] > temp[st[-1]]:
                res[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        
        return res
        