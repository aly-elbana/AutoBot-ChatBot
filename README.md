# AI ChatBot - AutoBot

A sophisticated AI-powered chatbot with multimodal capabilities, supporting text, images, PDFs, and various file formats.

## Project Structure

```
├── main.py                 # Main application entry point
├── config.py              # Configuration and LLM setup
├── functions.py           # Core chat functionality
├── gradio_functions.py    # Gradio interface handlers
├── file_handlers.py       # File processing utilities
├── model_charac.py        # AI character/prompt configuration
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Features

- **Multimodal Support**: Handles text, images, PDFs, and various file formats
- **Streaming Responses**: Real-time response generation with typing animation
- **File Upload**: Support for images, PDFs, Jupyter notebooks, and text files
- **Modern UI**: Clean, responsive Gradio interface
- **Error Handling**: Robust error handling and user feedback

## File Descriptions

### `main.py`

- Application entry point
- Gradio interface setup
- UI components and event handlers

### `config.py`

- Environment variable loading
- LLM configuration and initialization
- API key management

### `functions.py`

- Core chat logic with streaming
- Message processing and history management
- File upload integration

### `gradio_functions.py`

- Gradio-specific event handlers
- UI state management
- User interaction functions

### `file_handlers.py`

- PDF text extraction
- Image base64 encoding
- Jupyter notebook processing
- Text file reading utilities

### `model_charac.py`

- AI character configuration
- System prompts and personality settings

## Installation

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Set up environment variables:

```bash
# Create .env file
GEMINI_API_KEY=your_gemini_api_key_here
```

3. Run the application:

```bash
python main.py
```

## Supported File Types

- **Images**: `.png`, `.jpg`, `.jpeg`
- **Documents**: `.pdf`
- **Notebooks**: `.ipynb`
- **Text Files**: `.txt`, `.py`, `.json`, `.yaml`

## Usage

1. Start the application
2. Type your message in the text box
3. Optionally upload a file (image, PDF, etc.)
4. Click "Send" or press Enter
5. Watch the AI respond with streaming animation

## Architecture

The application follows a modular architecture:

- **Separation of Concerns**: Each module has a specific responsibility
- **Clean Imports**: No circular dependencies
- **Error Handling**: Comprehensive error management
- **Streaming**: Real-time response generation
- **File Processing**: Dedicated handlers for different file types

## Dependencies

- `gradio`: Web interface framework
- `langchain-google-genai`: Google Gemini AI integration
- `PyPDF2`: PDF text extraction
- `python-dotenv`: Environment variable management
