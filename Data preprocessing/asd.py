import os

def extract_classes_from_labels(txt_dir):
    """
    레이블 텍스트 파일에서 클래스 ID를 추출하는 함수

    :param txt_dir: 레이블 텍스트 파일이 있는 폴더 경로
    :return: 파일명과 클래스 ID 정보를 담은 딕셔너리
    """
    classes = {}

    # 텍스트 파일을 하나씩 읽기
    for txt_file in os.listdir(txt_dir):
        if txt_file.lower().endswith('.txt'):
            file_path = os.path.join(txt_dir, txt_file)
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    # 클래스 ID 추출 (라인의 첫 번째 값)
                    class_id = line.split()[0]
                    if txt_file not in classes:
                        classes[txt_file] = []
                    classes[txt_file].append(class_id)

    return classes

# 텍스트 파일이 있는 폴더 경로 설정
text_directory = r'C:\Users\AI Software\Desktop\yolo8dataset\hardhat_Person\train\labels'

# 클래스 정보 추출
classes_info = extract_classes_from_labels(text_directory)

# 추출된 클래스 정보 출력
for txt_file, class_ids in classes_info.items():
    print(f"File: {txt_file}, Classes: {', '.join(class_ids)}")
