from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser

model = ChatGroq(model = "llama-3.3-70b-versatile", temperature = 0, max_tokens = 4000)
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = '''Generate short and simple notes from the following text {text}''',
    input_variables = ['text']
)

prompt2 = PromptTemplate(
    template = '''Generate 5 short question answers from the following text {text}''',
    input_variables = ['text'] 
)

prompt3 = PromptTemplate(
    template = '''Merge the provided notes and quizinto a single document \n {notes} and quiz \n {quiz}''',
    input_variables = ['notes', 'quiz']
)

parallel_chain = RunnableParallel(
    {
        'notes' : prompt1 | model | parser,
        'quiz' : prompt2 | model | parser
    }
)
merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain

text = '''A Support Vector Machine (SVM) is a popular supervised machine learning algorithm used mainly for classification and sometimes regression tasks. It finds the best line or boundary—called a hyperplane—to separate data points into different groups or classes.How SVM WorksHyperplane: A decision boundary that splits the different classes of data. In a 2D space, it is a simple line; in 3D, it is a flat plane.Margin: The distance between the dividing line and the closest data points from each group. SVM tries to make this gap as wide as possible.Support Vectors: The specific data points that sit closest to the dividing line. They control the position and orientation of the hyperplane.Key Features of SVMLinear vs. Non-Linear: If data can be split with a straight line, it uses a linear SVM. If data is mixed up and cannot be split easily, it uses a kernel trick to lift data into a higher dimension where a clean cut is possible.Common Uses: Spam filtering, image recognition, face detection, and medical diagnosis (like sorting benign vs. malignant tumors)'''
# result = parallel_chain.invoke({"text" : text})

# for item in result.items():
#     print(item[0], item[1])
#     print()
result = chain.invoke({"text": text })
print(result)

# d = {'a' : 10,
#      'b' : 20}

# for i in d.items():
#     print(i[0], i[1])

# give the sentiment and summary of the review and pass it to llm for improvement