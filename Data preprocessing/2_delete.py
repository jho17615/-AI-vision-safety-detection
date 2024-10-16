import os

def clean_labels(label_dir, valid_classes):
    """
    라벨 파일에서 유효하지 않은 클래스 레이블을 삭제하는 함수

    :param label_dir: 라벨 파일이 있는 디렉토리 경로
    :param valid_classes: 유효한 클래스 목록
    :return: 변환된 파일 리스트, 변환되지 않은 파일 리스트
    """
    updated_files = []
    unchanged_files = []

    # 라벨 파일 디렉토리의 모든 파일을 반복
    for filename in os.listdir(label_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(label_dir, filename)

            with open(file_path, 'r') as file:
                lines = file.readlines()

            # 유효한 클래스 레이블만 남기기
            new_lines = [line for line in lines if int(line.split()[0]) in valid_classes]

            # 변경된 내용이 있는 경우에만 파일 업데이트
            if len(new_lines) != len(lines):
                with open(file_path, 'w') as file:
                    file.writelines(new_lines)
                updated_files.append(filename)
                print(f"Updated: {filename}")
            else:
                unchanged_files.append(filename)
                print(f"No changes: {filename}")

    return updated_files, unchanged_files

# 라벨 파일이 있는 디렉토리 경로 설정
label_directory = r'C:\Users\AI Software\Desktop\valid\al'
# 유효한 클래스 설정
valid_classes = [0,2]

# 라벨 파일 정리 실행
updated_files, unchanged_files = clean_labels(label_directory, valid_classes)

# 변환된 파일과 변환되지 않은 파일 리스트 출력
print("변환된 파일:")
print(updated_files)
print("변환되지 않은 파일:")
print(unchanged_files)
