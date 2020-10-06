from heapq import heapify, heappush, heappop


class RaceParticipants:
    def __init__(self, arr, name, kondratiy, index, points):
        self.arr = arr
        self.name = name
        self.kondratiy = kondratiy
        self.index = index
        self.points = points

    def __lt__(self, other):
        if self.kondratiy and other.kondratiy:
            return self.index > other.index
        if self.kondratiy or other.kondratiy:
            return self.kondratiy > other.kondratiy
        if not (self.kondratiy and other.kondratiy):
            if self.points == other.points:
                if self.name == other.name:
                    return self.index > other.index
                return self.name < other.name
            return self.points > other.points
        # if self.kondratiy:
        #     return self.kondratiy and self.index > other.index
        # if other.kondratiy:
        #     return other.kondratiy and self.index < other.index
        # if self.points > other.points:
        #     return True
        # if self.points == other.points:
        #     if self.name < other.name:
        #         return True
        #     if self.name == other.name:
        #         if self.index > other.index:
        #             return True

    @classmethod
    def creating_racers(cls, index, arr):
        name = arr[0]
        kondratiy = set('kondratiy').issubset(set(name))
        points = sum(
            int(arr[i]) for i in range(1, len(arr)) if int(arr[i]) > 0)
        participants = cls(arr, name, kondratiy, index, points)
        return participants

    def __str__(self):
        return ' '.join(self.arr)


class Race:
    def __init__(self, heap_list=[]):
        self.heap_list = heap_list

    @classmethod
    def insert_data(cls, arr):
        heap_list = list()
        for i, item in enumerate(arr):
            heappush(heap_list, RaceParticipants.creating_racers(i, item))
        return cls(heap_list)

    def get_data(self):
        riders1 = list()
        while len(self.heap_list) > 0:
            riders1.append(heappop(self.heap_list))
        return riders1


if __name__ == '__main__':
    with open('input.txt') as f:
        input_file = f.read().rstrip().split('\n')
    len_list, input_list = int(input_file[0]), input_file[1:]
    input_list = [i.split() for i in input_list]
    heap_obj = Race.insert_data(input_list)
    for i in heap_obj.get_data():
        print(i)
    # print(*heap_obj.get_data())
