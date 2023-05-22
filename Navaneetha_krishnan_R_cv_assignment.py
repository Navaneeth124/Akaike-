#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install PyPDF2


# In[3]:


pip install openai


# In[4]:


import PyPDF2
import openai


# In[5]:


# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

# Function to generate objective questions with multiple correct answers
def generate_questions_from_text(text):
    # Specify the OpenAI API parameters
    prompt = "Generate objective questions with multiple correct answers based on the following text:\n\n" + text + "\n\nQuestion:"
    model = "text-davinci-003"  # or any other GPT-3.5 based model
    max_tokens = 75  # Adjust the value based on desired question length

    # Generate questions using the OpenAI API
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=10,  # Number of questions to generate
        stop=None,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Process the API response to extract the generated questions
    questions = []
    for choice in response.choices:
        question = choice.text.strip().replace("\n", " ")
        if question:
            questions.append(question)

    return questions


# In[13]:


# Specify your OpenAI API key
openai.api_key = "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"

# Specify the path to the PDF file
pdf_file_path = "C:\\Users\\seeyo\\Desktop\\Tasks Given by company\\data annotated\\chapter-2.pdf"

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_file_path)

# Generate questions from the extracted text
generated_questions = generate_questions_from_text(pdf_text)

# Print the generated questions
for i, question in enumerate(generated_questions, 1):
    print(f"Question {i}: {question}")


# ## here with we need to buy the API key in openai

# In[10]:


# Specify the path to the PDF file
pdf_file_path = "C:\\Users\\seeyo\\Desktop\\Tasks Given by company\\data annotated\\chapter-2.pdf"

# Extract text from the PDF
pdf_text = extract_text_from_pdf(pdf_file_path)


# In[11]:


pdf_text


# In[ ]:




