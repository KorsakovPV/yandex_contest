n = int(input('Введите количество уроков: '))
lessons_time = []
for i in range(n):
    s = input()
    lessons_time.append([float(s.split()[0]), float(s.split()[1]), s])
sorted_lessons_time = sorted(lessons_time, key=lambda x: (x[1], x[0]))
timetable = [sorted_lessons_time[0]]
end_time = timetable[0][1]
for time in sorted_lessons_time[1:]:
    if time[0] >= end_time:
        timetable.append(time)
        end_time = timetable[-1][1]
print(len(timetable))
for time in timetable:
    print(time[2])

