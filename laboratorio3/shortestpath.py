start_pos = input()
target_pos = input()

start_x = ord(start_pos[0]) - ord('a')
target_x = ord(target_pos[0]) - ord('a')
start_y = int(start_pos[1]) - 1
target_y = int(target_pos[1]) - 1
dx = target_x - start_x
dy = target_y - start_y
num_moves = max(abs(dx), abs(dy))
print(num_moves)
current_x = start_x
current_y = start_y

while current_x != target_x or current_y != target_y:
    
    move = ""
    if current_x < target_x:
        move += "R"
        current_x += 1
    elif current_x > target_x:
        move += "L"
        current_x -= 1
    if current_y < target_y:
        move += "U"
        current_y += 1
    elif current_y > target_y:
        move += "D"
        current_y -= 1
    print(move)