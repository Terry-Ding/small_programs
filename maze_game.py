import random

def is_valid(li: list[list[int]]) -> bool:
    """
    This is a helper function.
    This function can check if the maze is 
    vaild or not.
    """
    for i in range(1, len(li) - 1):
        valid = False
        for j in range(1, len(li[i]) - 1):
            if li[i][j] == 0:
                valid = True
        if not valid:
            return False
    return True

def generate_maze(length: int, width: int) -> list[list[int]]:
    """
    This function generate the maze pattern
    randomly.
    """
    stop = False
    while not stop:
        ans = []
        first_line = []
        last_line = []

        for index in range(length + 2):
            first_line.append(1)
            last_line.append(1)
        
        ans.append(first_line)
        for row in range(width):
            temp = [1]
            for col in range(length):
                temp.append(random.randint(0, 1))
            temp.append(1)
            ans.append(temp)
        ans.append(last_line)

        if is_valid(ans):
            stop = True

    return ans

def start_point(maze_li: list[list[int]]) -> list[tuple[int, int]]:
    """
    This function can get the start point.
    """
    point_li = []
    x = 1
    for y in range(1, len(maze_li[x]) - 1):
        if maze_li[x][y] == 0:
            point_li.append((x, y))
    return point_li
            
def play(maze_li: list[list[int]], length: int, width: int) -> dict[tuple[int, int]]:
    """
    This function plays the maze and the result is within a 
    dictionary, which shows all the steps.
    """
    point_li = start_point(maze_li)
    again = True
    for point in point_li:
        x, y = point
        ans = {}
        count = 1
        stop = False
        repeat = []
        repeat.append((x, y))
        ans[count] = (x, y)

        while not stop:
            if x == len(maze_li) - 2 and maze_li[x][y] == 0:
                stop = True
                again = False
                return ans
            else:
                moved = False
                if x - 1 > 0 and maze_li[x - 1][y] == 0 and (x - 1, y) not in repeat:
                    # is able to move upward
                    x -= 1
                    moved = True
                elif x + 1 < len(maze_li) and maze_li[x + 1][y] == 0 and (x + 1, y) not in repeat:
                    # is able to move downward
                    x += 1
                    moved = True
                elif y - 1 > 0 and maze_li[x][y - 1] == 0 and (x, y - 1) not in repeat:
                    # is able to move left
                    y -= 1
                    moved = True
                elif y + 1 < len(maze_li[x]) and maze_li[x][y + 1] == 0 and (x, y + 1) not in repeat:
                    # is able to move right
                    y += 1
                    moved = True

                if moved:
                    count += 1
                    ans[count] = (x, y)
                    repeat.append((x, y))
                else:
                    stop = True
    if again:
        print(f"无解，重新生成")
        maze_li = generate_maze(length, width)
        for a in maze_li:
            for b in a:
                print(b, end = ' ')
            print()
        print('-------------------------------------')
        new_ans = play(maze_li, length, width)
        return new_ans

def main():
    """
    This is the main function, it shows the maze pattern and the solution.
    """
    length = int(input("enter length: "))
    width = int(input("enter width: "))
    maze_li = generate_maze(length, width)
    for index1 in maze_li:
        for index2 in index1:
            print(index2, end = ' ')
        print()
    solution = play(maze_li, length, width)
    print(f"答案是: {solution}")

if __name__ == "__main__":
    main()
