class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_customers = len(customers)
        running_sum = 0
        running_prep_time = 0
        for i in range(total_customers):
            print(f"arr:{customers[i][0]}, prep_time:{customers[i][1]}")
            arrival_time = customers[i][0]
            prep_time = customers[i][1]
            if arrival_time > running_prep_time:
                running_prep_time = arrival_time + prep_time
            else:
                running_prep_time += prep_time
            val = running_prep_time - arrival_time
            running_sum += val
            print(val, running_sum)
            print(running_prep_time)

        return running_sum / total_customers
