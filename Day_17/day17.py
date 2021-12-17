import re
from aoc_utils import timed

def main():
    with open('day17_input.txt') as f:
        input = f.readline()
    print("Part 1:", timed(part1, input))
    print("Part 2:", timed(part2, input))

def get_potential_velocities(minimum, maximum, is_x):
    potential_vx = []
    for vx in range(-1000, 1000):
        x = 0
        i = 0
        step_region = []
        for vxd in range(vx, -1 if is_x else -1000, -1):
            i += 1
            x += vxd
            if minimum <= x <= maximum:
                step_region.append(i)
            if (x > maximum and is_x) or (x < minimum and not is_x):
                if step_region:
                    step_region.append(i - 1)
                    potential_vx.append((vx, step_region))
                break
        if minimum <= x <= maximum:
            if step_region:
                step_region.append(-1)
                potential_vx.append((vx, step_region))
    return potential_vx

def get_potential_velocity_pairs(target_x0, target_x1, target_y0, target_y1):
    potential_vx = get_potential_velocities(target_x0, target_x1, True)
    potential_vy = get_potential_velocities(target_y0, target_y1, False)
    potential_pairs = []
    for vx, step_region_x in potential_vx:
        for vy, step_region_y in potential_vy:
            if any(a in step_region_y for a in step_region_x) or (step_region_x[-1] == -1 and any(a >= step_region_x[-2] for a in step_region_y)):
                potential_pairs.append((vx, vy))
    return potential_pairs

def part1(input):
    target_x0, target_x1, target_y0, target_y1 = [int(x) for x in re.findall(r'-?\d+', input)]
    potential_pairs = get_potential_velocity_pairs(target_x0, target_x1, target_y0, target_y1)
    max_y = 0
    for vx, vy in potential_pairs:
        max_height = sum(range(vy+1))
        max_y = max(max_height, max_y)
    return max_y

def part2(input):
    target_x0, target_x1, target_y0, target_y1 = [int(x) for x in re.findall(r'-?\d+', input)]
    potential_pairs = get_potential_velocity_pairs(target_x0, target_x1, target_y0, target_y1)
    return len(potential_pairs)

if __name__ == '__main__':
    main()
