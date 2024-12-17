import random
import json
import sys

# 재귀 깊이 설정
sys.setrecursionlimit(1500)

def save_students_to_file(students, filename="students.json"):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

def generate_students_and_save(num_students=30, filename="students.json"):
    students = []
    for _ in range(num_students):
        name = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
        age = random.randint(18, 22)
        score = random.randint(0, 100)
        students.append({"이름": name, "나이": age, "성적": score})
    
    save_students_to_file(students, filename)
    return students

# 선택 정렬
def selection_sort(students, key, reverse=False):
    for i in range(len(students)):
        min_index = i
        for j in range(i+1, len(students)):
            if (students[j][key] < students[min_index][key]) ^ reverse:
                min_index = j
        students[i], students[min_index] = students[min_index], students[i]
    return students

# 삽입 정렬
def insertion_sort(students, key, reverse=False):
    for i in range(1, len(students)):
        key_student = students[i]
        j = i - 1
        while j >= 0 and ((students[j][key] > key_student[key]) ^ reverse):
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = key_student
    return students

# 퀵 정렬
def quick_sort_iterative(arr, key, reverse=False):
    stack = [(0, len(arr) - 1)]
    
    while stack:
        low, high = stack.pop()
        if low < high:
            p = partition(arr, low, high, key, reverse)
            stack.append((low, p - 1))
            stack.append((p + 1, high))
            
    return arr

def partition(arr, low, high, key, reverse):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if (arr[j][key] < pivot[key]) ^ reverse:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# 기수 정렬 
def radix_sort(students):
    RADIX = 10
    max_length = False
    tmp, placement = -1, 1

    while not max_length:
        max_length = True
        buckets = [[] for _ in range(RADIX)]

        for student in students:
            tmp = student["성적"] // placement
            buckets[tmp % RADIX].append(student)
            if max_length and tmp > 0:
                max_length = False

        a = 0
        for b in range(RADIX):
            bucket = buckets[b]
            for student in bucket:
                students[a] = student
                a += 1

        placement *= RADIX
    return students

# 사용자 인터페이스
def main():
    students = generate_students_and_save()
    print("생성된 학생 정보:")
    for student in students:
        print(student)

    while True:
        try:
            print("\n정렬 기준을 선택하세요:")
            print("1. 이름을 기준으로 정렬")
            print("2. 나이를 기준으로 정렬")
            print("3. 성적을 기준으로 정렬")
            print("4. 프로그램 종료")
            
            choice = input("선택: ")
            if not choice.isdigit() or int(choice) not in [1, 2, 3, 4]:
                raise ValueError("유효한 숫자를 입력하세요.")
            choice = int(choice)

            if choice == 4:
                print("프로그램을 종료합니다.")
                break

            print("\n정렬 알고리즘을 선택하세요:")
            print("1. 선택 정렬")
            print("2. 삽입 정렬")
            print("3. 퀵 정렬")
            print("4. 기수 정렬 (성적 기준)")
            
            algorithm = input("선택: ")
            if not algorithm.isdigit() or int(algorithm) not in [1, 2, 3, 4]:
                raise ValueError("유효한 숫자를 입력하세요.")
            algorithm = int(algorithm)

            print("\n정렬 방식을 선택하세요:")
            print("1. 오름차순")
            print("2. 내림차순")
            
            order = input("선택: ")
            if not order.isdigit() or int(order) not in [1, 2]:
                raise ValueError("유효한 숫자를 입력하세요.")
            order = int(order)
            reverse = (order == 2)

            key_map = {1: "이름", 2: "나이", 3: "성적"}
            key = key_map[choice]

            if algorithm == 1:
                students = selection_sort(students, key, reverse)
            elif algorithm == 2:
                students = insertion_sort(students, key, reverse)
            elif algorithm == 3:
                students = quick_sort_iterative(students, key, reverse)
            elif algorithm == 4 and choice == 3:
                students = radix_sort(students)
            else:
                print("잘못된 선택입니다.")
                continue

            print("\n정렬된 학생 정보:")
            for student in students:
                print(student)

        except ValueError as e:
            print(f"오류: {e}")
            continue

if __name__ == "__main__":
    main()
