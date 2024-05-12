# -*- coding: utf-8 -*-
from openai import OpenAI

client = OpenAI(
    api_key="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"
)

userInput = "매매의 목적물이 화재로 소실됨으로써 매도인의 매매 목적물 인도 의무가 이행 불능일 경우 매수인이 화재사고로 매도인이 지급받게 되는 화재보험금 화재공제금 전부에 대하여 대상청구권을 행사할 수 있나요?"
systemOutput = "유사 판례에 따르면, 매매의 목적물이 화재로 소실됨으로써 매도인의 매매 목적물 인도 의무가 이행 불능일 경우, 매수인은 화재사고로 매도인이 지급받게 되는 화재보험금 및 화재공제금에 대하여 대상청구권을 행사할 수 있습니다. 이는 매수인이 특별한 사정이 없는 한 목적물에 대하여 지급되는 화재보험금 및 화재공제금 전부에 대하여 대상청구권을 행사할 수 있다는 원칙을 강조하고 있습니다.따라서, 매매의 목적물이 화재로 소실되어 매도인의 인도 의무가 이행 불능이 되었을 때, 매수인은 화재사고로 매도인이 받게 되는 화재보험금 및 화재공제금에 대한 청구를 할 수 있습니다. 이러한 권리는 특별한 사정이 없는 한 해당 보험금 전부에 대하여 행사할 수 있음을 의미합니다.이러한 판례에 근거하여, 매수인이 화재사고로 매도인이 받게 되는 화재보험금 및 화재공제금 전부에 대하여 대상청구권을 행사할 수 있습니다. 이러한 원칙은 민법 제390조, 상법 제664조, 제665조, 제676조 제1항, 제683조 등의 관련 법조규정에 근거하고 있습니다."

chat_completion = client.chat.completions.create(
    
    messages=[
        {
            "role" : "system",
            "content" : f"You will be presented with one legal question and the system's answer to it. Your task is to evaluate the answers according to certain metrics.Your task is to rate the summary on one metric."
                            "Please make sure you read and understand these instructions carefully. Please keep this document open while reviewing, and refer to it as needed."
                            "Evaluation Criteria:"
                            "Legal accuracy (1-5) - The extent to which the answer is consistent with the legal basis. Answers should accurately reflect relevant law and case law. Answers that are uncertain about the legal basis or contain incorrect information should be penalized."
                            "Evaluation Steps:"
                            "1. Read the questions and answers: Carefully read the legal question provided and the system's answer."
                            "2. Compare legal basis: Evaluate how well the answer responds to the question and how accurately it uses relevant laws and case law."
                            "3. Rate legal accuracy: Evaluate how legally accurate the answer is and whether it contains false or unnecessary information."
                            "4. Assign a legal accuracy score: Score the answer for legal accuracy on a scale of 1 to 5. Where 1 is highly inaccurate and 5 is perfectly accurate."
                            "5. Also, provide a rationale for your calculated score"
                            "Example:"
                            "User question:"
                            f"{userInput}"
                            "system's answer:"
                            f"{systemOutput}"
                            
                            # "Evaluation Form (scores, rationale):"
                            # "- Relevance:"
        },  
    ],
    model="gpt-4",
    temperature=1
)

print(chat_completion.choices[0].message.content)