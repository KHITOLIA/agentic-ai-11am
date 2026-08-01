from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

hf_pipeline = pipeline(
    task = "text-generation",
    model = model,
    tokenizer = tokenizer
)

from langchain_huggingface import HuggingFacePipeline

llm = HuggingFacePipeline(pipeline = hf_pipeline)

prompt = "What is machine learning"
generated_text = llm.invoke(prompt)
print(generated_text)