import gradio as gr

from langchain_upstage import ChatUpstage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain.schema import AIMessage, HumanMessage
import os
UPSTAGE_API_KEY = 'up_jPLrNhquQw7Ie8fpfR6Q6HM6M0LSd'
llm = ChatUpstage(api_key=UPSTAGE_API_KEY, streaming=True)

# More general chat
chat_with_history_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", 
         """
C to Assembly Conversion:
Take the C code with the specified environment and architecture.
Provide the corresponding assembly code based on that.
If the architecture is not mentioned, ask for it.
The architecture does not have to be specified. The general terms like x86, arm, RISC-V are enough

Simulating Assembly Code Execution:
You cannot execute the assembly code but you can simulate it only and give the expected output.
You can simulate the expected output from the assembly code.
you can Act like the terminal or command prompt.
If the code requires user input, prompt the user for it and wait for their response.
Do not insert your own input or assume the users input; only show the output based on the user's input.
Follow the code structure and sequence step by step, ensuring to wait for user input when needed.


Scope of Responses:
Do not provide answers outside the conversion of C code to assembly code and simulating the results.
If asked something outside this scope, respond with "Sorry, I am a C code to assembly tool."
Example:

Choose an option:

Sine
Cosine
Tangent
Exit
Enter your choice:
User: 1

You: Enter the angle in degrees: 30
Sine(30.00) = 0.5000

Choose an option:

Sine
Cosine
Tangent
Exit
Enter your choice:
User: 2

You: Enter the angle in degrees: 45
Cosine(45.00) = 0.7071

Choose an option:

Sine
Cosine
Tangent
Exit
Enter your choice:
User: 3

You: Enter the angle in degrees: 60
Tangent(60.00) = 1.7321

Choose an option:

Sine
Cosine
Tangent
Exit
Enter your choice:
User: 4

You: Exiting the program.

As shown in the example, wait for the user's input at each step and provide the corresponding output.
         """
         ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{message}"),
    ]
)

chain = chat_with_history_prompt | llm | StrOutputParser()

def chat(message, history):
    history_langchain_format = []
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))
        save_assembly_code(ai)

    generator = chain.stream({"message": message, "history": history_langchain_format})

    assistant = ""
    for gen in generator:
        assistant += gen
        yield assistant

def save_assembly_code(ai_content):
    start_marker = "```assembly\n"
    end_marker = "```"
    start_index = ai_content.find(start_marker) + len(start_marker)
    end_index = ai_content.find(end_marker, start_index)
    
    if start_index != -1 and end_index != -1:
        assembly_code = ai_content[start_index:end_index].strip()
        with open("output.s", "w") as file:
            file.write(assembly_code)
    else:
        print("No assembly code found in the AI content.")

with gr.Blocks() as demo:
    chatbot = gr.ChatInterface(
        chat,
        examples=[],
        title="Solar Chatbot for C to assembly",
        description="One Tool For All Computing Architechtures",
    )
    chatbot.chatbot.height = 500

if __name__ == "__main__":
    demo.launch()
