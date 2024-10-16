import os

# 폴더 경로를 입력하세요
folder_path = R'C:\Users\AI Software\Desktop\test\xl'

# 클래스 카운트를 위한 변수 초기화
count_0 = 0
count_1 = 0
count_2 = 0
# 폴더 내 모든 파일을 처리합니다
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as file:
            for line in file:
                # 줄에서 클래스 정보를 추출합니다
                parts = line.strip().split()  # 공백으로 분리
                if parts:  # 줄이 비어 있지 않다면
                    label = parts[0]  # 첫 번째 항목이 클래스 라벨이라고 가정
                    if label == '0':
                        count_0 += 1
                    if label == '1':
                        count_1 += 1
                    elif label == '2':
                        count_2 += 1

print(f'클래스 0의 개수: {count_0}')
print(f'클래스 1의 개수: {count_1}')
print(f'클래스 2의 개수: {count_2}')