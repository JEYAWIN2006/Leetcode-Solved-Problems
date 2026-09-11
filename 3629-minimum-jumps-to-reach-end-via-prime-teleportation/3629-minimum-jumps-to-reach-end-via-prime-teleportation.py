class Solution(object):
    def minJumps(self, nums):
        l=len(nums)
        max_nums=max(nums)
        is_prime=[True]*(max_nums+1)
        is_prime[0]=is_prime[1]=False
        for i in range(2,int(sqrt(max_nums))+1):
            if is_prime[i]==True:
                for j in range(i*i,max_nums+1,i):
                    is_prime[j]=False
        mp_nums = defaultdict(list)
        for i,n in enumerate(nums):
            mp_nums[n].append(i)
        
        
        prime_seen=set()
        q=deque()
        q.append(0)
        dis=[-1]*l
        dis[0]=0
        while q:
            cur = q.popleft()
            if cur==l-1: return dis[cur]
            if cur-1>=0 and dis[cur-1]==-1:
                q.append(cur-1)
                dis[cur-1]= dis[cur]+1
            if cur+1<l and dis[cur+1]==-1:
                q.append(cur+1)
                dis[cur+1]= dis[cur]+1
            num = nums[cur]
            if is_prime[num] and num not in prime_seen:
                prime_seen.add(num)
                for multi in range(num,max_nums+1,num):
                    if multi in mp_nums:
                        for idx in mp_nums[multi]:
                            if dis[idx]==-1:
                                q.append(idx)
                                dis[idx]= dis[cur]+1
        return dis[-1]
