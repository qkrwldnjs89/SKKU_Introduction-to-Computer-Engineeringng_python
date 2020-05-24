import time
from a1_2020314315 import largest_prime_factor, odd_occurred_number


time_results = [[] for _ in range(2)]

print("#1")
with open("sample_input_1.txt", "r") as f:
    data = f.readlines()
    for d in data:
        start_time = time.time()
        print(largest_prime_factor(int(d)))
        time_results[0].append(f"{time.time() - start_time:.4f} sec")  # f-string format

print("#2")
with open("sample_input_2.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        li = list(map(int, line.split(" ")))
        start_time = time.time()
        print(odd_occurred_number(li))
        time_results[1].append(f"{time.time() - start_time:.4f} sec")  # f-string format

print("Time result")
for i in range(2):
    print(f"#{i+1}: {time_results[i]}")  # f-string format
