import cv2
import os

# 이미지와 라벨 파일이 있는 디렉토리 경로
image_dir = r'C:\Users\AI Software\Desktop\yolo8dataset\valid\images'
label_dir = r'C:\Users\AI Software\Desktop\yolo8dataset\valid\labels'

# 클래스 ID와 클래스 이름을 매핑하는 사전
class_names = {0: 'Ladder', 1: 'Person', 2: 'Helmet'}
# 클래스마다 고유한 색상을 지정
class_colors = {0: (0, 255, 0), 1: (0, 0, 255), 2: (255, 0, 0)}

# 이미지 디렉토리 내의 모든 파일을 반복 처리
for image_file_name in os.listdir(image_dir):
    if image_file_name.endswith('.jpg'):
        # 이미지 파일 경로와 YOLO 라벨 파일 경로 설정
        image_file_path = os.path.join(image_dir, image_file_name)
        yolo_label_file_path = os.path.join(label_dir, os.path.splitext(image_file_name)[0] + '.txt')

        # 이미지를 읽어옵니다.
        image = cv2.imread(image_file_path)

        # YOLO 라벨 파일을 엽니다.
        if os.path.exists(yolo_label_file_path):
            with open(yolo_label_file_path, 'r') as label_file:
                lines = label_file.readlines()

            for line in lines:
                label_data = line.strip().split(' ')
                class_id = int(label_data[0])
                x_center = float(label_data[1])
                y_center = float(label_data[2])
                normalized_width = float(label_data[3])
                normalized_height = float(label_data[4])

                # 이미지 크기에 맞게 바운딩 박스 좌표와 크기를 계산합니다.
                h, w = image.shape[:2]
                x = int((x_center - normalized_width / 2) * w)
                y = int((y_center - normalized_height / 2) * h)
                box_width = int(normalized_width * w)
                box_height = int(normalized_height * h)

                # 클래스 ID에 해당하는 색상을 가져옵니다.
                color = class_colors.get(class_id, (0, 255, 0))

                # 바운딩 박스를 이미지에 그립니다.
                cv2.rectangle(image, (x, y), (x + box_width, y + box_height), color, 2)

                # 클래스 이름을 이미지에 표시
                label = class_names.get(class_id, 'Unknown')

                # 텍스트 배경을 반투명하게 표시
                text_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
                text_x = x
                text_y = y - 10 if y - 10 > 10 else y + 10
                background_tl = (text_x, text_y - text_size[1] - 5)
                background_br = (text_x + text_size[0] + 5, text_y + 2)

                cv2.rectangle(image, background_tl, background_br, color, -1)
                cv2.putText(image, label, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            # 이미지에 라벨링된 결과를 표시합니다.
            cv2.imshow('Image with YOLO Labeling', image)
            cv2.waitKey(0)

# 창을 닫습니다.
cv2.destroyAllWindows()
