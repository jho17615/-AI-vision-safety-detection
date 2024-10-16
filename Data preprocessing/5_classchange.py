import os
import shutil


def process_labels(label_dir, move_dir, class_to_move, new_class):
    """
    라벨 파일을 읽어 특정 클래스 레이블을 다른 폴더로 이동시키고, 해당 레이블을 새로운 값으로 변경하는 함수

    :param label_dir: 원본 라벨 파일이 있는 폴더 경로
    :param move_dir: 이동할 폴더 경로
    :param class_to_move: 이동할 클래스 레이블
    :param new_class: 변경할 클래스 레이블
    """
    # 원본 폴더와 이동할 폴더가 존재하는지 확인
    if not os.path.exists(label_dir):
        print(f"Source directory '{label_dir}' does not exist.")
        return
    if not os.path.exists(move_dir):
        print(f"Move directory '{move_dir}' does not exist. Creating it.")
        os.makedirs(move_dir)

    # 이동된 파일 수를 추적하기 위한 변수
    moved_files_count = 0

    # 원본 폴더의 모든 파일을 반복
    for filename in os.listdir(label_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(label_dir, filename)

            # 라벨 파일을 읽기
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # 수정된 라벨을 저장할 리스트
            new_lines = []
            move_file = False

            # 라벨 파일의 각 라인 처리
            for line in lines:
                parts = line.strip().split()
                if len(parts) > 0:
                    label = int(parts[0])
                    if label == class_to_move:
                        move_file = True
                        # 새 레이블로 변경
                        parts[0] = str(new_class)

                # 수정된 라인을 리스트에 추가
                new_lines.append(' '.join(parts) + '\n')

            # 파일 이동 및 수정된 내용 저장
            if move_file:
                # 이동할 폴더로 파일 이동
                shutil.move(file_path, os.path.join(move_dir, filename))
                # 수정된 라벨 파일을 원본 폴더에 저장
                with open(file_path, 'w') as file:
                    file.writelines(new_lines)
                print(f"Moved and updated file: {filename}")
                moved_files_count += 1

    # 이동된 파일 수 출력
    print(f"Total number of files processed: {moved_files_count}")


# 원본 폴더와 이동할 폴더 경로 설정
label_directory = r'C:\Users\AI Software\Desktop\test\xl'
move_directory = r'C:\Users\AI Software\Desktop\test\xl'

# 클래스 레이블을 이동시키고 변경할 값 설정
class_to_move = 0
new_class = 2

# 라벨 파일 처리 수행
process_labels(label_directory, move_directory, class_to_move, new_class)
