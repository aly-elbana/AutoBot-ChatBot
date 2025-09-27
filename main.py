import gradio as gr
from gradio_functions import respond, stop_response, clear_chat

with gr.Blocks(title="AutoBot ChatBot", css="""
    .small-textbox textarea {
        min-height: 30px;
        max-height: 200px;
        padding: 4px 8px !important;
        font-size: 14px !important;
        overflow-y: auto;
        resize: vertical;
    }
    .gr-row {
        align-items: center !important;
        display: flex !important;
        gap: 8px !important;
    }
    .gr-row > div:nth-child(2),
    .gr-row > div:nth-child(3) {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
""") as demo:
    gr.Row(scale=2)
    gr.Row(scale=2)
    gr.Markdown("# 💬 AutoBot ChatBot\n\n  \n \n ")

    chatbot = gr.Chatbot(type="messages", height="70vh", show_label=False)

    with gr.Row():
        with gr.Column(scale=4):
            msg = gr.Textbox(
                placeholder="Type your question here...", 
                show_label=False,
                elem_classes="small-textbox",
            )
        with gr.Column(scale=2):
            with gr.Row(scale=2):
                with gr.Column(scale=1, min_width=120):
                    file_in = gr.File(
                        type="filepath", 
                        file_types=[".png", ".jpg", ".jpeg", ".pdf", ".txt", ".py", ".json", ".yaml", ".ipynb", 
                                   ".js", ".jsx", ".ts", ".tsx", ".html", ".css", ".scss", ".sass", ".less",
                                   ".cpp", ".c", ".h", ".hpp", ".cc", ".cxx", ".java", ".kt", ".scala",
                                   ".php", ".rb", ".go", ".rs", ".swift", ".dart", ".r", ".m", ".mm",
                                   ".cs", ".csx", ".xml", ".csv", ".sql", ".md", ".rst", ".tex", ".log", ".ini", ".cfg",
                                   ".sh", ".bash", ".zsh", ".fish", ".ps1", ".bat", ".cmd"],
                        label="Upload", 
                        height=40,
                        
                    )
                with gr.Column(scale=1, min_width=80):
                    send_btn = gr.Button("Send", scale=1)

    with gr.Row():
        stop_btn = gr.Button("⏹ Stop", variant="stop")
        clear_btn = gr.Button("Clear Chat")

    
    demo.queue()

    send_event = send_btn.click(
        respond, inputs=[msg, chatbot, file_in],
        outputs=[chatbot, msg, file_in, msg, send_btn]
    )
    submit_event = msg.submit(
        respond, inputs=[msg, chatbot, file_in],
        outputs=[chatbot, msg, file_in, msg, send_btn]
    )

    stop_btn.click(
        fn=stop_response,
        inputs=[chatbot],
        outputs=[chatbot, msg, file_in, msg, send_btn],
        cancels=[send_event, submit_event]
    )

    clear_btn.click(clear_chat, outputs=[chatbot, msg, file_in, msg, send_btn])

if __name__ == "__main__":
    demo.launch(share=True)
