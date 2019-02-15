import time

class PrimeNumbers:
    N = 10000
    nums = [i+1 for i in range(1, N)]
    boolNums = [True for i in range(1, N)]

    #Медленный метод
    def SlowMethod(N=N):
        start_time= time.time()
        nums = [i+1 for i in range(1, N)]
        for n in nums:
            for m in nums[1:]:
                if n!=m and m % n == 0:
                    nums.remove(m)
        #print(nums)
        print('Slow Time: '+str(round(time.time()-start_time, 6)))

    #Решето
    def Sieve(_nums = nums, _N=N):
        start_time= time.time()
        for n in range(2, _N):
            for m in range(n*n, _N, n):
                    _nums[m]=-1
                    #_nums.remove(m)
        print(_nums)
        print('Sieve Time: '+str(round(time.time()-start_time, 6)))

#PrimeNumbers.SlowMethod()
PrimeNumbers.Sieve()
