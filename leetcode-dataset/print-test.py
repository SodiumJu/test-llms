import json
from bs4 import BeautifulSoup

# Specify the line number you want to fetch (0-based index)
j = 3  # For example, to fetch the 4th line (index starts at 0)

# Open the JSONL file and read the j-th line
with open('LeetCode-dataset/leetcode_questions.jsonl', 'r', encoding='utf-8') as jsonl_file:
    lines = jsonl_file.readlines()  # Read all lines from the file

    if j < len(lines):
        # Parse the j-th line into a dictionary
        question_data = json.loads(lines[j].strip())
        
        # Print the content (e.g., the question content and title)
        print(f"Question Title: {question_data['questionTitle']}")
        print(f"Content: {question_data['content']}")
        # soup = BeautifulSoup(question_data['content'], "html.parser")
        # # Get the plain text without HTML tags
        # plain_text = soup.get_text(separator="\n", strip=True)
        # # Print the plain text
        # print(plain_text)

        print(f"Similar Questions: {question_data['similarQuestions']}")
    else:
        print(f"Line {j} does not exist in the file. The file has {len(lines)} lines.")
