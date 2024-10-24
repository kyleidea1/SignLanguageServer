import random

def generate_random_korean_word():
    korean_words = [
        '택시', '기사님', '요금', '미터기', '카드', '현금', '영수증',
        '목적지', '주소', '길', '교통', '혼잡', '우회', '빠르게',
        '천천히', '안전', '정체', '신호등', '건널목', '사거리',
        '좌회전', '우회전', '직진', '유턴', '정류장', '공항',
        '역', '터미널', '호텔', '식당', '병원', '학교', '회사',
        '아파트', '주차', '내리다', '타다', '멈추다', '출발',
        '도착', '거리', '시간', '분', '기다리다', '서두르다',
        '늦다', '빠르다', '가깝다', '멀다', '앞', '뒤', '옆'
    ]
    return random.choice(korean_words)

def process_frames(input_folder, output_file):
    # 입력 폴더의 jpg 파일 수 확인 (실제로는 파일을 세지 않고 임의의 수를 사용)
    word_count = random.randint(3, 7)
    
    # 무작위로 한글 단어 선택하여 문장 생성
    words = [generate_random_korean_word() for _ in range(word_count)]
    sentence = " ".join(words)
    
    # 결과를 파일에 쓰기
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(sentence)
    
    return sentence

# 테스트용 코드
if __name__ == "__main__":
    test_input_folder = "./test_frames"
    test_output_file = "./test_output.txt"
    result = process_frames(test_input_folder, test_output_file)
    print(f"생성된 문장: {result}")