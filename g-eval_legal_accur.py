# -*- coding: utf-8 -*-
from openai import OpenAI

#key.txt 파일을 읽어서 api_key를 가져옴
with open('key.txt', 'r') as f:
    api_key = f.readline().strip()
client = OpenAI(
    api_key=api_key
)

userInput = "매매의 목적물이 화재로 소실됨으로써 매도인의 매매 목적물 인도 의무가 이행 불능일 경우 매수인이 화재사고로 매도인이 지급받게 되는 화재보험금 화재공제금 전부에 대하여 대상청구권을 행사할 수 있나요?"
systemOutput = "유사 판례에 따르면, 매매의 목적물이 화재로 소실됨으로써 매도인의 매매 목적물 인도 의무가 이행 불능일 경우, 매수인은 화재사고로 매도인이 지급받게 되는 화재보험금 및 화재공제금에 대하여 대상청구권을 행사할 수 있습니다. 이는 매수인이 특별한 사정이 없는 한 목적물에 대하여 지급되는 화재보험금 및 화재공제금 전부에 대하여 대상청구권을 행사할 수 있다는 원칙을 강조하고 있습니다.따라서, 매매의 목적물이 화재로 소실되어 매도인의 인도 의무가 이행 불능이 되었을 때, 매수인은 화재사고로 매도인이 받게 되는 화재보험금 및 화재공제금에 대한 청구를 할 수 있습니다. 이러한 권리는 특별한 사정이 없는 한 해당 보험금 전부에 대하여 행사할 수 있음을 의미합니다.이러한 판례에 근거하여, 매수인이 화재사고로 매도인이 받게 되는 화재보험금 및 화재공제금 전부에 대하여 대상청구권을 행사할 수 있습니다. 이러한 원칙은 민법 제390조, 상법 제664조, 제665조, 제676조 제1항, 제683조 등의 관련 법조규정에 근거하고 있습니다."

chat_completion = client.chat.completions.create(
    
    messages=[
                {
            "role": "system",
            "content": "You will be presented with one legal question and the system's answer to it. Your task is to evaluate the answers according to certain metrics. Your task is to rate the summary on two metrics: legal accuracy and relevance. Please make sure you read and understand these instructions carefully. Please keep this document open while reviewing, and refer to it as needed.\n\n"
                    "Evaluation Criteria:\n"
                    "1. Legal accuracy (1-5) - The extent to which the answer is consistent with the legal basis. Answers should accurately reflect relevant law and case law. Answers that are uncertain about the legal basis or contain incorrect information should be penalized.\n"
                    "2. Relevance (1-5) - The degree to which the answer directly addresses the user's question. The answer should be comprehensive and directly respond to the legal question posed. Answers that are off-topic, incomplete, or fail to address the main points of the question should be penalized.\n\n"
                    "Evaluation Steps:\n"
                    "1. Read the questions and answers: Carefully read the legal question provided and the system's answer.\n"
                    "2. Compare legal basis: Evaluate how well the answer responds to the question and how accurately it uses relevant laws and case law.\n"
                    "3. Rate legal accuracy: Evaluate how legally accurate the answer is and whether it contains false or unnecessary information.\n"
                    "4. Assess relevance: Determine how well the answer addresses the user's question and whether it provides a comprehensive response.\n"
                    "5. Assign scores: Score the answer for both legal accuracy and relevance on a scale of 1 to 5. Where 1 is highly inaccurate/irrelevant and 5 is perfectly accurate/relevant.\n"
                    "6. Provide rationales: Provide a rationale for your calculated scores for both legal accuracy and relevance.\n\n"
                    "Example:\n"
                    "User question:\n"
                    f"{userInput}\n"
                    "System's answer:\n"
                    f"{systemOutput}\n\n"
                    # "# Evaluation Form (scores, rationales):\n" 
                    "- Legal accuracy: \n"
                    "- Rationale for legal accuracy:\n"
                    "- Relevance: \n"
                    "- Rationale for relevance:\n"
        },

    ],
    model="gpt-4o",
    temperature=1
)

print(chat_completion.choices[0].message.content)