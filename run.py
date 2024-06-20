import requests

def ask_question(model, api_key, question):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    
    data = {
        'prompt': question,
        'max_tokens': 50
    }
    
    if model == 'chatgpt4':
        url = 'https://api.openai.com/v1/chat/completions'
    elif model == 'chatglm':
        url = 'https://api.openai.com/v1/engines/glm-13b/completions'
    else:
        raise ValueError("Unsupported model. Choose 'chatgpt4' or 'chatglm'.")

    response = requests.post(url, headers=headers, json=data)
    return response.json()

# 使用示例
api_key = 'your_api_key_here'
question = "What is the capital of France?"

# 调用 ChatGPT-4
response_gpt4 = ask_question('chatgpt4', api_key, question)
print("ChatGPT-4 response:", response_gpt4)

# 调用 ChatGLM
response_glm = ask_question('chatglm', api_key, question)
print("ChatGLM response:", response_glm)
