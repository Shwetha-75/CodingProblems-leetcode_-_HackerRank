class RecentCounter:

    def __init__(self):
        self.queue=[]
 
    def ping(self, t: int) -> int:
        self.queue.append(t)
        count=0
        min_value,max_value=t-3000,t 
        for i in self.queue:
            if i>=min_value and i<=max_value:
                count+=1 
        return count
    
        