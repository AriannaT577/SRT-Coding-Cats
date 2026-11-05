import random

def create_list(size):
    random_list = []
    for _ in range(size):
        random_list.append(random.randint(1, 6))
    return random_list

def count_list(my_list, number):
    count = 0
    for item in my_list:
        if item == number:
            count += 1
    return count

def average_list(my_list):
    if not my_list:
        return 0
    total = sum(my_list)
    return total / len(my_list)

def main():
    big_list = create_list(10000)
    
    print("counts for each number (1-6(six or seven?)):")
    #1-6
    for i in range(1, 7):
        occurrence = count_list(big_list, i)
        print(f"number {i} appears {occurrence} times")

    #2-6
    #for i in range(2, 7):
    #    occurrence = count_list(big_list, i)
    #    print(f"number {i} appears {occurrence} times")
        
    avg = average_list(big_list)
    print(f"\naverage of all numbers is: {avg:.2f}")

main()