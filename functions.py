"""
Core chat functionality for the AI ChatBot.
"""
import os
import time
from config import get_llm
from model_charac import system_prompt
from file_handlers import (pdf_to_text, ipynb_to_text, image_to_base64, read_text_file, 
                          csv_to_text, xml_to_text, get_file_type_info)


def chat_with_teacher_streaming(message, history, file=None):
    """
    Core chat function with streaming support for file uploads.
    
    Args:
        message (str): User's message
        history (list): Chat history
        file (str): Path to uploaded file (optional)
    
    Yields:
        list: Updated chat history
    """
    try:
        # Get LLM instance
        llm = get_llm()
        
        # Build messages list for llm.invoke
        messages = []
        messages.append({
            "role": "system",
            "content": [{"type": "text", "text": system_prompt}]
        })

        # Add conversation history
        for msg in history:
            role = msg.get("role", "user")
            text = msg.get("content", "")
            messages.append({
                "role": "user" if role == "user" else "assistant",
                "content": [{"type": "text", "text": text}]
            })

        # Prepare current user content
        user_content = []
        if message and message.strip():
            user_content.append({"type": "text", "text": message})

        # Handle file uploads
        if file:
            ext = os.path.splitext(file)[1].lower()
            icon, file_type = get_file_type_info(file)
            
            if ext in [".png", ".jpg", ".jpeg"]:
                # Handle image files
                b64data, mime = image_to_base64(file)
                user_content.append({
                    "type": "image",
                    "source_type": "base64",
                    "mime_type": mime,
                    "data": b64data
                })
                history.append({"role": "user", "content": f"{message} {icon} (with {file_type})"})
            elif ext == ".pdf":
                # Handle PDF files
                pdf_text = pdf_to_text(file)
                user_content.append({"type": "text", "text": f"\n{icon} {file_type} Content:\n{pdf_text}"})
                history.append({"role": "user", "content": f"{message} {icon} (with {file_type})"})
            elif ext == ".ipynb":
                # Handle Jupyter notebooks
                nb_text = ipynb_to_text(file)
                user_content.append({"type": "text", "text": f"\n{icon} {file_type} Content:\n{nb_text}"})
                history.append({"role": "user", "content": f"{message} {icon} (with {file_type})"})
            elif ext == ".csv":
                # Handle CSV files
                csv_text = csv_to_text(file)
                user_content.append({"type": "text", "text": f"\n{icon} {file_type} Content:\n{csv_text}"})
                history.append({"role": "user", "content": f"{message} {icon} (with {file_type})"})
            elif ext == ".xml":
                # Handle XML files
                xml_text = xml_to_text(file)
                user_content.append({"type": "text", "text": f"\n{icon} {file_type} Content:\n{xml_text}"})
                history.append({"role": "user", "content": f"{message} {icon} (with {file_type})"})
            else:
                # Handle other text files (code files, scripts, configs, etc.)
                file_text = read_text_file(file)
                user_content.append({"type": "text", "text": f"\n{icon} {file_type} Content:\n{file_text}"})
                history.append({"role": "user", "content": f"{message} {icon} (with {file_type})"})
        else:
            history.append({"role": "user", "content": message})

        messages.append({"role": "user", "content": user_content})

        # Thinking animation
        thinking_steps = [
            "🧠 Analyzing input...",
            "🔎 Understanding context...",
            "🏗️ Structuring answer...",
            "✍️ Finalizing response..."
        ]
        history.append({"role": "assistant", "content": ""})
        for step in thinking_steps:
            history[-1]["content"] = step
            yield history
            time.sleep(0.6)

        history[-1]["content"] = ""
        yield history

        # Call LLM
        full_response = llm.invoke(messages)

        if hasattr(full_response, "content"):
            response_text = full_response.content
        else:
            response_text = str(full_response)

        # Stream response character by character
        response = ""
        for ch in response_text:
            response += ch
            history[-1]["content"] = response
            yield history
            time.sleep(0.01)

    except Exception as e:
        history.append({"role": "assistant", "content": f"❌ Error: {e}"})
        yield history