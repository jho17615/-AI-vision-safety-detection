import os
import shutil

def move_class_1_files(label_dir, dest_dir, target_class=1):
    """
    클래스 1이 포함된 라벨 파일을 지정된 디렉토리로 이동하는 함수

    :param label_dir: 라벨 파일이 있는 디렉토리 경로
    :param dest_dir: 파일을 이동할 대상 디렉토리 경로
    :param target_class: 이동할 클래스 ID (기본값은 1)
    :return: 이동된 파일 리스트
    """
    # 대상 디렉토리가 존재하지 않으면 생성
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    moved_files = []

    # 라벨 파일 디렉토리의 모든 파일을 반복
    for filename in os.listdir(label_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(label_dir, filename)

            with open(file_path, 'r') as file:
                lines = file.readlines()

            # 클래스 ID가 1인 라인이 있는지 확인
            if any(int(line.split()[0]) == target_class for line in lines):
                # 파일을 대상 디렉토리로 이동
                shutil.move(file_path, os.path.join(dest_dir, filename))
                moved_files.append(filename)
                print(f"Moved: {filename}")

    return moved_files

# 라벨 파일이 있는 디렉토리 경로 설정
label_directory = r'C:\Users\AI Software\Desktop\BAC_HIEN_CONSTRUCTION_SAFETY_2024.v8i.yolov8\train\jx'
# 파일을 이동할 대상 디렉토리 경로 설정
destination_directory = r'C:\Users\AI Software\Desktop\BAC_HIEN_CONSTRUCTION_SAFETY_2024.v8i.yolov8\train\1x'

# 클래스 1이 포함된 파일 이동 실행
moved_files = move_class_1_files(label_directory, destination_directory, target_class=1)

# 이동된 파일 리스트 출력
print("Moved files:")
print(moved_files)
