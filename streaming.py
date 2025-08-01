from litellm import completion

def completion_llm(prompt):
    response = completion(
        model="ollama/llama3.2:1b", 
        messages=[
            {"content": "respond in 20 words. who are you?", "role": "system"},
            {"content": prompt, "role": "user"}
        ], 
        api_base="http://localhost:11434",
        stream=True
    )
    for chunk in response:
        if hasattr(chunk.choices[0].delta, "content") and chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="", flush=True)

