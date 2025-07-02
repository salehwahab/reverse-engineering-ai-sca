import gradio as gr
from langchain_upstage import ChatUpstage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain.schema import AIMessage, HumanMessage
from pathlib import Path
import os
import time

UPSTAGE_API_KEY = 'up_jPLrNhquQw7Ie8fpfR6Q6HM6M0LSd'
llm = ChatUpstage(api_key=UPSTAGE_API_KEY, streaming=True)

# More general chat
chat_with_history_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", 
         """
C to Assembly Conversion:
Take the C code with the specified architecture.
Provide the corresponding assembly code based on that.
If the architecture is not mentioned, ask for it.
You can convert the C code to architectures like x86, ARM, RISC-V and others.
The architecture does not have to be specified. The general terms like x86, ARM, RISC-V are enough

Scope of Responses:
Do not provide answers outside an assembly code.
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
    assembly_code = ai_content[start_index:end_index]
    
    # Save the assembly code to a file
    output_file = "output.s"
    with open(output_file, "w") as f:
        f.write(assembly_code)
    
    return output_file

def upload_c_file(file):
    with open(file.name, 'r') as f:
        c_code = f.read()
    return c_code

def convert_c_to_assembly(c_code, architecture, progress=gr.Progress()):
    message = f"C code:\n{c_code}\nArchitecture: {architecture}"
    history = []
    total_steps = 10  # Simulating 10 steps for the progress bar

    for step in range(total_steps):
        progress((step + 1) / total_steps, f"Step {step + 1}/{total_steps}: Processing...")
        time.sleep(0.5)  # Simulating processing time for each step

    for response in chat(message, history):
        pass
    assembly_file = save_assembly_code(response)
    return assembly_file

def update_download_button(filepath):
    return gr.UploadButton(visible=False), gr.DownloadButton(label=f"Download {Path(filepath).name}", value=filepath, visible=True)

with gr.Blocks() as demo:
    gr.Markdown("Upload a .c file and specify the architecture to receive the corresponding .s file.")
    
    with gr.Row():
        with gr.Column():
            upload_button = gr.UploadButton("Upload .c file", file_count="single")
            architecture_input = gr.Textbox(label="Architecture (e.g., x86, ARM, RISC-V)")
            convert_button = gr.Button("Convert to Assembly")
            download_button = gr.DownloadButton(visible=False)

    c_code = gr.Textbox(visible=False)
    
    upload_button.upload(upload_c_file, upload_button, c_code)
    convert_button.click(convert_c_to_assembly, inputs=[c_code, architecture_input], outputs=download_button).then(
        update_download_button, inputs=[download_button], outputs=[upload_button, download_button]
    )
    
if __name__ == "__main__":
    demo.launch()
