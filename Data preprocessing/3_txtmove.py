import os
import shutil


def move_empty_txt_files(src_dir, dest_dir):
    """
    원본 폴더에서 내용이 없는 .txt 파일을 다른 폴더로 이동하는 함수

    :param src_dir: 원본 폴더 경로
    :param dest_dir: 빈 .txt 파일을 이동할 폴더 경로
    """
    # 원본 폴더와 대상 폴더가 존재하는지 확인
    if not os.path.exists(src_dir):
        print(f"Source directory '{src_dir}' does not exist.")
        return
    if not os.path.exists(dest_dir):
        print(f"Destination directory '{dest_dir}' does not exist. Creating it.")
        os.makedirs(dest_dir)

    # 원본 폴더의 모든 파일을 반복
    for filename in os.listdir(src_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(src_dir, filename)

            # 파일이 비어 있는지 확인
            if os.path.getsize(file_path) == 0:
                dest_file_path = os.path.join(dest_dir, filename)

                # 파일 이동
                shutil.move(file_path, dest_file_path)
                print(f"Moved empty file: {filename}")


# 원본 폴더와 대상 폴더 경로 설정
source_directory = r'C:\Users\AI Software\Desktop\yolov5dataset\valid\labels'
destination_directory = r'C:\Users\AI Software\Desktop\yolov5dataset\valid\x'

# 빈 .txt 파일 이동 수행
move_empty_txt_files(source_directory, destination_directory)
