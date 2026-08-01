from ollama import generate

# Send a single prompt to the local model
response = generate(
    model='llama3.2',
    prompt='Write a short poem about open-source software.'
)

# Extract and print the final text response
print(response['response'])