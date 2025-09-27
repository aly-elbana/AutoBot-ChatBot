from dotenv import load_dotenv
import os

# import gradio as gr
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from model_charac import system_prompt

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature=0.5
)

# Define prompt with history support
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="history"),
    ("user", "{input}")
])


chain = prompt | llm | StrOutputParser()

def chat_with_teacher(_user_input, _history):
    response_text = chain.invoke({
        "input": _user_input,
        "history": _history
    })
    return response_text

history = []


while True:
    user_input = input("\n💡 Ask your AI Teacher: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("👋 Goodbye, happy learning!")
        break
    answer = chat_with_teacher(user_input, history)
    print("\n📘 Answer:\n", answer)
    # Append messages to history
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=answer))

