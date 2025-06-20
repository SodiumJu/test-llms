import requests
import json

# 設定 GraphQL 端點
url = "https://leetcode.com/graphql"

# 設定 GraphQL 查詢語句
# 查詢題目列表和相關信息


graphql_query = {
    "query": """
    query {
        allQuestions {
            questionId
            questionTitle
            questionType
            difficulty
            content
            similarQuestions
        }
    }
    """
}

# 設定 headers，如果需要認證，請在這裡加入 cookies 或 token
headers = {
    "Content-Type": "application/json",
    "Cookie": "LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfcGFzc3dvcmRfcmVzZXRfa2V5IjoiY28wYnZ0LTkyZWFjZTY2NmVkMGRmODU5ZWI5ZjAzMTU5ODg4OTJhIiwiX2F1dGhfdXNlcl9pZCI6IjMyMTk2NzQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJhbGxhdXRoLmFjY291bnQuYXV0aF9iYWNrZW5kcy5BdXRoZW50aWNhdGlvbkJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiMTEyYWE0N2U1YjEzYTZhOTU3NzNkNGQzNzVkMzZmYWVmOGU2OGE4YTRlYTYyNDIwMTBhOWQ3YjYzYjdmMWNkIiwic2Vzc2lvbl91dWlkIjoiYjYwNjhhMzQiLCJpZCI6MzIxOTY3NCwiZW1haWwiOiJ5ajVqdTBiakBnbWFpbC5jb20iLCJ1c2VybmFtZSI6Illhbi1SdV9KdSIsInVzZXJfc2x1ZyI6Illhbi1SdV9KdSIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9kZWZhdWx0X2F2YXRhci5qcGciLCJyZWZyZXNoZWRfYXQiOjE3NDQ1OTk4NDIsImlwIjoiMTQwLjEwOS4yMS41NSIsImlkZW50aXR5IjoiMzNkMGYyNTdhODE3ZDFjYTRjNDM4MWI4N2Y4YWQ4M2YiLCJkZXZpY2Vfd2l0aF9pcCI6WyJlYTE2MWUwMzEyM2Q4OTcxYWJkZmM0Mjc4NjJmM2Y4ZCIsIjE0MC4xMDkuMjEuNTUiXSwiX3Nlc3Npb25fZXhwaXJ5IjoxMjA5NjAwfQ.f938lN7NQuwrZdyEj9wBuhVxXNNVrmBxcPjQ2h7Cicc",  # 如果需要提供 cookies 或 token
}

# 發送 POST 請求
response = requests.post(url, json=graphql_query, headers=headers)

# 檢查回應
if response.status_code == 200:
    data = response.json()
    questions = data.get('data', {}).get('allQuestions', [])
    print(f"共找到 {len(questions)} 題目")
    with open('leetcode_questions.jsonl', 'w', encoding='utf-8') as jsonl_file:
        for question in questions:
            # question_id = question['questionId']
            # question_title = question['questionTitle']
            # question_type = question['questionType']
            # question_difficulty = question['questionDifficulty']
            # question_content = question['content']
            # similar_questions = question['similarQuestions']
            
            # print(f"題目 ID: {question_id}")
            # print(f"題目標題: {question_title}")
            # print(f"題目類型: {question_type}")
            # print(f"題目難度: {question_difficulty}")
            # print(f"題目內容: {question_content}")
            # print(f"相似題目: {similar_questions}")
            # print("-" * 50)
            question_data = {
                "questionId": question['questionId'],
                "questionTitle": question['questionTitle'],
                "questionType": question['questionType'],
                "difficulty": question['difficulty'],
                "content": question.get('content', 'No content'),  # Handle missing content
                "similarQuestions": question.get('similarQuestions', []),
            }

            jsonl_file.write(json.dumps(question_data, ensure_ascii=False) + "\n")
else:
    print("請求失敗:", response.status_code)
    print(f"錯誤信息: {response.text}")
