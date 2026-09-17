print("===== AI Prompt Analyzer =====")
prompt=input("Enter your prompt:")
words=prompt.split()
print("\n your prompt:")
print(prompt)
print("\nnumber of words:")
print(len(words))
if len(words)<5:
    print("\n suggestion: Add more details to your prompt.")
else:
    print("\n your prompt has enough words to start.")