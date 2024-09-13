from groq import Groq
client = Groq(api_key="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")


rules={
    1:"llama3-8b-8192",
    2:"llama-3.1-8b-instant",
    3:"llama3-70b-8192",
    4:"llama-3.1-70b-versatile",
    5:"mixtral-8x7b-32768",
    6:"llava-v1.5-7b-4096-preview",
    7:"gemma-7b-it",
    8:"gemma2-9b-it"
}
def get_response(messages,n):
    completion = client.chat.completions.create(
        model=rules[n],
        messages=messages,
        temperature=0,
        max_tokens=4096,
        top_p=1,
        stream=False,
        stop=None,
    )

    content = completion.choices[0].message.content

    return content