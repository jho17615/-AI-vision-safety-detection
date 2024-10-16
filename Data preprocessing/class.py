import os
import shutil
import time

def extract_and_move_class_files(txt_dir, dest_dir, target_class="2"):
    """
    특정 클래스 ID를 포함하는 레이블 파일을 추출하여 다른 폴더로 이동하는 함수

    :param txt_dir: 레이블 텍스트 파일이 있는 원본 폴더 경로
    :param dest_dir: 파일을 이동할 대상 폴더 경로
    :param target_class: 추출할 클래스 ID (기본값은 "2")
    """
    # 대상 폴더가 존재하지 않으면 생성
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # 클래스 ID가 포함된 파일 이동
    moved_files_count = 0
    for txt_file in os.listdir(txt_dir):
        if txt_file.lower().endswith('.txt'):
            file_path = os.path.join(txt_dir, txt_file)
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    class_id = line.split()[0]
                    if class_id == target_class:
                        try:
                            # 파일 복사 후 원본 파일 삭제
                            shutil.copy2(file_path, os.path.join(dest_dir, txt_file))
                            os.remove(file_path)
                            print(f"Moved file: {txt_file} containing class ID {target_class}")
                            moved_files_count += 1
                        except PermissionError:
                            print(f"PermissionError: File {file_path} is being used by another process.")
                            time.sleep(0)  # 잠시 대기 후 재시도
                        break  # 파일이 이미 이동되었으므로 더 이상 검사하지 않음

    # 이동된 파일 수 출력
    print(f"Total number of files moved: {moved_files_count}")

# 레이블 파일이 있는 원본 폴더 경로 설정
text_directory = r'C:\Users\AI Software\Desktop\BAC_HIEN_CONSTRUCTION_SAFETY_2024.v8i.yolov8\train\labels'

# 파일을 이동할 대상 폴더 경로 설정
destination_directory = r'C:\Users\AI Software\Desktop\BAC_HIEN_CONSTRUCTION_SAFETY_2024.v8i.yolov8\train\x'

# 클래스 ID 2가 포함된 파일만 추출 및 이동
extract_and_move_class_files(text_directory, destination_directory, target_class="2")
