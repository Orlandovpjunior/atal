import sys

def solve():
    n_str = sys.stdin.readline().strip()
    n = int(n_str)
    
    min_super_lucky = float('inf')

    def generate_super_lucky(current_num, count_4, count_7):
        nonlocal min_super_lucky
        
        if current_num > min_super_lucky:
            return
        
        if count_4 == count_7 and count_4 > 0:
            if current_num >= n:
                min_super_lucky = min(min_super_lucky, current_num)

        if count_4 + count_7 >= 10:
            return

        generate_super_lucky(current_num * 10 + 4, count_4 + 1, count_7)
        
        generate_super_lucky(current_num * 10 + 7, count_4, count_7 + 1)

    generate_super_lucky(0, 0, 0)

    print(min_super_lucky)

if __name__ == "__main__":
    solve()