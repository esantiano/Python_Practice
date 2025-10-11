import copy
import random

#region my solution:
class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            for i in range(count):
                self.contents.append(color)
        self.removed = []

    def __str__(self):
        return str(self.contents)

    def replace_contents(self):
        self.contents += self.removed
        self.removed.clear()

    def draw(self,num):  
        results = []
        draw = 0
        total = len(self.contents)
        while draw < num:
            count = len(self.contents)
            if count == 0:
                self.replace_contents()
                results.clear()
            rand = random.random()
            ind = int(rand*count)-1
            result = self.contents.pop(ind)
            results.append(result)
            self.removed.append(result)
            draw += 1
        return results

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    contents_copy = copy.copy(hat.contents)
    for _ in range(num_experiments):
        results = hat.draw(num_balls_drawn)
        _key = {}
        expected = copy.copy(expected_balls)
        for color in results:
            if color in _key:
                _key[color] += 1
            else:
                _key[color] = 1
            if color in expected and _key[color] == expected[color]:
                del expected[color]
        if not expected:
            M +=1
    return M/num_experiments
#endregion 

# region chatgpt solution:
import copy
import random

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            for i in range(count):
                self.contents.append(color)

    def __str__(self):
        return str(self.contents)

    def draw(self,num):
        count = len(self.contents)
        if count == 0:
            return self.contents
        if count <= num:
            drawn = self.contents.copy()
            self.contents.clear()
            return drawn
        
        results = []
        for draw in range(num):
            ind = random.randrange(count)
            result = self.contents.pop(ind)
            results.append(result)
            count -=1
        return results


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)
        draw_counts = {}
        for color in drawn:
            draw_counts[color] = draw_counts.get(color, 0) + 1
    
        success = True
        for color, count in expected_balls.items():
            if draw_counts.get(color,0) < count:
                success = False
                break
                
        if success:
            M += 1

    return M/num_experiments

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)


# endregion



# region test cases:
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)
# endregion