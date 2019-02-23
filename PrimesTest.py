import time
import sys

class PrimeNumbers:
    N = 0
    nums = list(range(2, N))

    def __init__(self, n = 100):
        self.N = n
        self.nums = list(range(2, n))

    #Медленный метод
    #@staticmethod
    def SlowMethod(self):
        _nums = self.nums.copy()
        start_time= time.time()
        for n in _nums:
            for m in _nums[1:]:
                if n!=m and m % n == 0:
                    _nums.remove(m)
        #print(nums)
        print('Slow Time: '+str(round(time.time()-start_time, 5)))

    #Решето
    #@staticmethod
    def SieveMethod(self):
        _nums = self.nums.copy()
        start_time= time.time()
        for n in range(0, self.N-2):
            if _nums[n]<0:
                continue
            for m in range(n+_nums[n], self.N-2, _nums[n]):
                    _nums[m]=-1
        #print(_nums)
        print('Sieve Time: '+str(round(time.time()-start_time, 5)))

    #Мой метод
    def FastMethod(self):   
        print('FastMethod')


    def ExecuteAllMethods(self):
        print('\n*********************')
        print('N = '+str(self.N))
        self.SlowMethod()
        self.SieveMethod()
        print('********************\n')


PrimeNumbers(2500).ExecuteAllMethods()
