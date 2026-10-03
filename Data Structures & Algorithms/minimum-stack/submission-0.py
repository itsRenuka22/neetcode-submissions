class MinStack:

    def __init__(self):
        self.st = []
        self.mini = []
        

    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self.mini) == 0:
            self.mini.append(val)
        else:
            self.mini.append(min(val, self.mini[-1]))       

    def pop(self) -> None:
        self.st.pop()
        self.mini.pop()
        
    def top(self) -> int:
        return self.st[-1]
        
    def getMin(self) -> int:
        return self.mini[-1]


        
