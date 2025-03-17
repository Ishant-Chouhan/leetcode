class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        def noc(time,ranks,cars):
            car_nums=0
            for i in ranks:
                car_nums+=int((time/i)**0.5)
            return car_nums>=cars

        low=1
        min_rank=min(ranks)
        high=min_rank*cars*cars

        while low<= high:
            mid=(low+high)//2

            if noc(mid,ranks,cars):
                Time=mid
                high=mid-1
            else:
                low=mid+1

        return Time