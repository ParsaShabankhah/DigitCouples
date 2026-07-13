import random

class GameLogic:

    def __init__(self, mode):
        self.saving_points = list()
        self.mode = mode
        self.blocks = self.generate_blocks()
        self.health = (self.mode ** 2) // 4 + 1
        self.points = 0

    def generate_blocks(self):
        cells = [(row, col) for row in range(self.mode//2) for col in range(self.mode//2)]
        random.shuffle(cells)
        nums = random.sample(range(1, 101), (self.mode**2 - 4)//8 + 1)
        main_num = nums[-1]
        nums.pop()
        blocks = {items[0]:(items[1][0], items[1][1]) for items in zip(nums, zip(cells[::2], cells[1::2]))}
        blocks[main_num] = cells[-1]
        self.main_num = main_num
        return blocks

    def lose_health(self):
        if self.check_health():
            self.health -= 1
        return False

    def check_health(self):
        return self.health > 0

    def check_match(self, first_pick, first_cell, second_pick, second_cell):
        res = None
        if first_pick == second_pick:
            if first_cell != second_cell:
                if first_pick not in self.saving_points and second_pick not in self.saving_points:
                    self.saving_points.append(first_pick)
                    self.saving_points.append(second_pick)
                    res = True
                    print("They're matched!")
                    self.points += 1
            else:
                res = False
                self.lose_health()
        else:
            res = False
            self.lose_health()
        return res

    def check_main(self, pick):
        if pick == self.main_num:
            if pick not in self.saving_points:
                self.saving_points.append(pick)
                return True
            else:
                return None
        else:
            return False

    def check_victory(self):
        return self.points == ((self.mode)**2 - 4)//8