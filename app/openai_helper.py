import os
from openai import OpenAI

# api_key = os.getenv("OPENAI_API_KEY")
# if not api_key:
#     raise ValueError("API key is missing! Make sure to set it in the environment variables.")
# client = OpenAI(api_key=api_key)

def read_words_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().split()

client = OpenAI(api_key="sk-proj-7v7ONn0vYJnTvXstEt2obqhEwKKVPcprORCBybsdxMjBLzKmEDey2BseBTUVlO3Ww5RdFTQpeeT3BlbkFJtyWoS9eI1gDtbdaKm1Fm0snbUX9YUI74XP0wGZxKTbW-ln_2tAAGKMB4917OzjhFRP3YpwuuI
A")

def ask_chatgpt(words):
    try:
        # words가 리스트인 경우 문자열로 변환
        if isinstance(words, list):
            gloss_text = " ".join(words)
        else:
            gloss_text = words
            
        # 파인튜닝된 모델 ID (실제 모델 ID로 교체 필요)
        fine_tuned_model_id = "ft:gpt-3.5-turbo-0125:personal::AL0CbsDQ"  # 여기에 실제 파인튜닝된 모델 ID를 입력
        
        response = client.chat.completions.create(
            model=fine_tuned_model_id,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert in translating Korean sign language glosses into natural Korean sentences."
                },
                {
                    "role": "user",
                    "content": gloss_text
                }
            ]
        )
        
        natural_sentence = response.choices[0].message.content
        print(f"Gloss input: {gloss_text}")
        print(f"Generated sentence: {natural_sentence}")
        
        return natural_sentence
        
    except Exception as e:
        print(f"Error in ask_chatgpt: {str(e)}")
        return "자연스러운 문장을 생성하는 중 오류가 발생했습니다."

def main():
    filename = input("단어가 포함된 텍스트 파일의 이름을 입력하세요: ")
    words = read_words_from_file(filename)
    sentence = ask_chatgpt(words)
    print(f"\n생성된 택시 상황 문장: {sentence}")

if __name__ == "__main__":
    main()
