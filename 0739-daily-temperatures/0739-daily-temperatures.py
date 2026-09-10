class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # ==== Brute Force: ====
        # answer = []
        # for i in range(len(temperatures)):
        #     cnt = 1
        #     j = i+1
        #     while j < len(temperatures):
        #         if temperatures[i] < temperatures[j]:
        #             break
        #         j+=1
        #         cnt+=1
        #     cnt = 0 if j == len(temperatures) else cnt
        #     answer.append(cnt)
        # return answer

        # ==== Better Solution ====
        n = len(temperatures)
        output = [0]*n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                output[prev] = i - prev
            
            stack.append(i)
        return output