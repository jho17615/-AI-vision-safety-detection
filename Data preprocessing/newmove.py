import os
import shutil

def move_matching_files(image_dir, txt_dir, dest_dir):
    """
    이미지 파일과 텍스트 파일의 이름을 비교하여 같은 이름의 파일을 다른 폴더로 이동하는 함수

    :param image_dir: 이미지 파일이 있는 원본 폴더 경로
    :param txt_dir: 텍스트 파일이 있는 원본 폴더 경로
    :param dest_dir: 이동할 폴더 경로
    """
    # 원본 폴더와 대상 폴더가 존재하는지 확인
    if not os.path.exists(image_dir):
        print(f"Image directory '{image_dir}' does not exist.")
        return
    if not os.path.exists(txt_dir):
        print(f"Text directory '{txt_dir}' does not exist.")
        return
    if not os.path.exists(dest_dir):
        print(f"Destination directory '{dest_dir}' does not exist. Creating it.")
        os.makedirs(dest_dir)

    # 이미지 파일과 텍스트 파일의 이름 목록 가져오기
    image_files = set(os.path.splitext(f)[0] for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')))
    txt_files = set(os.path.splitext(f)[0] for f in os.listdir(txt_dir) if f.lower().endswith('.txt'))

    # 이름이 같은 파일 찾기
    common_names = image_files.intersection(txt_files)

    # 이동된 파일 수를 추적하기 위한 변수
    moved_files_count = 0

    for name in common_names:
        # 이미지 파일 경로 설정
        img_file_path = None
        for ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp']:
            possible_img_path = os.path.join(image_dir, f"{name}{ext}")
            if os.path.exists(possible_img_path):
                img_file_path = possible_img_path
                break

        # 텍스트 파일 경로 설정
        txt_file_path = os.path.join(txt_dir, f"{name}.txt")

        # 대상 파일 경로 설정
        dest_img_file_path = os.path.join(dest_dir, os.path.basename(img_file_path))
        dest_txt_file_path = os.path.join(dest_dir, os.path.basename(txt_file_path))

        # 이미지 파일 이동
        if img_file_path and os.path.exists(txt_file_path):
            shutil.move(img_file_path, dest_img_file_path)
            shutil.move(txt_file_path, dest_txt_file_path)
            print(f"Moved image file: {os.path.basename(img_file_path)} and text file: {os.path.basename(txt_file_path)}")
            moved_files_count += 1

    # 이동된 파일 수 출력
    print(f"Total number of file pairs moved: {moved_files_count}")

# 원본 폴더와 대상 폴더 경로 설정
image_directory = r'C:\Users\AI Software\Desktop\yolo8dataset\hardhat_Person\test\x'
text_directory = r'C:\Users\AI Software\Desktop\yolo8dataset\hardhat_Person\test\labels'
destination_directory = r'C:\Users\AI Software\Desktop\yolo8dataset\hardhat_Person\valid\x'

# 파일 이동 수행
move_matching_files(image_directory, text_directory, destination_directory)
