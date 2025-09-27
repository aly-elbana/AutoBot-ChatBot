"""
Gradio interface functions for the AI ChatBot.
"""
import gradio as gr
from functions import chat_with_teacher_streaming


def respond(message, history, file):
    """
    Handle user input and generate response.
    
    Args:
        message (str): User's message
        history (list): Chat history
        file (str): Uploaded file path
    
    Yields:
        tuple: Updated chat state
    """
    if not (message and message.strip()) and not file:
        return history, "", None, gr.update(interactive=True), gr.update(interactive=True)

    yield history, "", None, gr.update(interactive=False), gr.update(interactive=False)

    for updated_history in chat_with_teacher_streaming(message, history, file):
        yield updated_history, "", None, gr.update(interactive=False), gr.update(interactive=False)

    yield updated_history, "", None, gr.update(interactive=True), gr.update(interactive=True)


def clear_chat():
    """
    Clear the chat history and reset the interface.
    
    Returns:
        tuple: Reset chat state
    """
    return [], "", None, gr.update(interactive=True), gr.update(interactive=True)


def stop_response(history):
    """
    Stop the current response generation.
    
    Args:
        history (list): Current chat history
    
    Returns:
        tuple: Updated chat state
    """
    if history and history[-1]["role"] == "assistant":
        if history[-1]["content"] in ["⏳ Thinking...", ""] or history[-1]["content"].endswith("response..."):
            history.pop(-1)
    return history, "", None, gr.update(interactive=True), gr.update(interactive=True)
