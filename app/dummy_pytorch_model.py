def process_frames(input_folder, output_file):
   # 고정된 문장 리스트
   sentences = [
       "종로 찾다 가다 곳 방법",
       "돈 얼마 맞다 확인",
       "돈 계산 잘못하다"
   ]
   
   # 파일이 있으면 읽어서 마지막 인덱스 확인, 없으면 0부터 시작
   try:
       with open('last_index.txt', 'r') as f:
           last_index = int(f.read().strip())
   except:
       last_index = -1
   
   # 다음 인덱스 계산 (순환)
   current_index = (last_index + 1) % len(sentences)
   
   # 현재 인덱스 저장
   with open('last_index.txt', 'w') as f:
       f.write(str(current_index))
   
   # 현재 문장 선택
   sentence = sentences[current_index]
   
   # 결과를 파일에 쓰기
   with open(output_file, 'w', encoding='utf-8') as f:
       f.write(sentence)
   
   return sentence

# 테스트용 코드
if __name__ == "__main__":
   test_input_folder = "./test_frames"
   test_output_file = "./test_output.txt"
   
   # 여러 번 호출하여 순환 테스트
   for _ in range(5):
       result = process_frames(test_input_folder, test_output_file)
       print(f"생성된 문장: {result}")