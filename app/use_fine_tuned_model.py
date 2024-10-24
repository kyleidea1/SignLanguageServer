from openai import OpenAI

# OpenAI 클라이언트 초기화
client = OpenAI(api_key="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")

def translate_gloss(fine_tuned_model_id, gloss_text):
    try:
        response = client.chat.completions.create(
            model=fine_tuned_model_id,  # 여기에 파인튜닝된 모델 ID를 입력
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
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# 사용 예시
fine_tuned_model_id = "ft:gpt-3.5-turbo-0125:personal::AL0CbsDQ"  # 여기에 실제 모델 ID를 입력하세요
test_glosses = [
    "지하철 다음 내리다"
]

print("수어 글로스 번역 결과:")
print("-" * 50)
for gloss in test_glosses:
    translation = translate_gloss(fine_tuned_model_id, gloss)
    print(f"글로스: {gloss}")
    print(f"번역: {translation}")
    print("-" * 50)