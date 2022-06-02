# Number of test cases
T = int(input())

# Execute as number of test cases
for tc in range(1, T + 1):
    # N : Number of lockers
    # M : Number of students
    M, N = map(int, input().split())

    luggage_volume = sorted(list(map(int, input().split())), reverse=True)
    locker_capacity = sorted(list(map(int, input().split())), reverse=True)

    # # # if print value == Number of students
    # # Sum of volumes of placed luggage
    num_students = 0

    while True:
        # if no more luggage or no more lockers
        if not locker_capacity or not luggage_volume:
            break
        locker_selected = locker_capacity.pop(0)

        i = 0
        while True:
            if i == len(luggage_volume) or not luggage_volume:
                break

            if locker_selected == 0:
                break

            if locker_selected >= luggage_volume[i]:
                luggage_volume.pop(i)
                num_students += 1
                break
            else:
                i += 1

    print(f'#{tc} {num_students}')