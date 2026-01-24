# MinStack

from typing import List
import random 

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            current_min = min(val, self.min_stack[-1])
            self.min_stack.append(current_min)

    def pop(self) -> None:
        # 뺄 때는 양쪽 다 같이 빼야 그 층에 대한 기록이 유지된다.
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        # 맨 위 마지막 값 보여주기
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]


        
if __name__ == "__main__":
    obj = MinStack()
