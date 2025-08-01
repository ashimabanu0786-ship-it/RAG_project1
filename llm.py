from litellm import completion

def completion_prompt(prompt):
    response = completion(
        model="ollama/llama3.2:1b", 
        messages=[
            {"content": "respond in 20 words. who are you?", "role": "system"},
            {"content": prompt, "role": "user"}
        ], 
        api_base="http://localhost:11434"
    )
    return response

