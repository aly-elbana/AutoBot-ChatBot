# AI ChatBot - AutoBot

A sophisticated AI-powered chatbot with multimodal capabilities, supporting text, images, PDFs, and extensive file format support including programming languages, data formats, and documentation files.

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

- **Multimodal Support**: Handles text, images, PDFs, and extensive file format support
- **Programming Languages**: JavaScript, TypeScript, C++, Java, Python, PHP, Ruby, Go, Rust, Swift, Dart, R, Scala, Kotlin, Objective-C, C#
- **Web Development**: HTML, CSS, SCSS, SASS, LESS
- **Data Formats**: JSON, YAML, XML, CSV, SQL
- **Documentation**: Markdown, reStructuredText, LaTeX
- **Scripts**: Bash, Zsh, Fish, PowerShell, Batch
- **Config Files**: INI, CFG, Log files
- **Streaming Responses**: Real-time response generation with typing animation
- **Smart File Detection**: Automatic file type recognition with appropriate icons
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
- CSV file processing
- XML file parsing
- Smart file type detection with icons
- Support for 30+ file formats

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

### Programming Languages

- **JavaScript**: `.js`, `.jsx`
- **TypeScript**: `.ts`, `.tsx`
- **C/C++**: `.cpp`, `.c`, `.h`, `.hpp`, `.cc`, `.cxx`
- **Java**: `.java`
- **Python**: `.py`
- **PHP**: `.php`
- **Ruby**: `.rb`
- **Go**: `.go`
- **Rust**: `.rs`
- **Swift**: `.swift`
- **Dart**: `.dart`
- **R**: `.r`
- **Scala**: `.scala`
- **Kotlin**: `.kt`
- **Objective-C**: `.m`, `.mm`
- **C#**: `.cs`, `.csx`

### Web Development

- **HTML**: `.html`
- **CSS**: `.css`, `.scss`, `.sass`, `.less`

### Data Formats

- **JSON**: `.json`
- **YAML**: `.yaml`, `.yml`
- **XML**: `.xml`
- **CSV**: `.csv`
- **SQL**: `.sql`

### Documentation

- **Markdown**: `.md`
- **reStructuredText**: `.rst`
- **LaTeX**: `.tex`

### Scripts

- **Bash**: `.sh`, `.bash`
- **Zsh**: `.zsh`
- **Fish**: `.fish`
- **PowerShell**: `.ps1`
- **Batch**: `.bat`, `.cmd`

### Other Formats

- **Images**: `.png`, `.jpg`, `.jpeg`
- **Documents**: `.pdf`
- **Notebooks**: `.ipynb`
- **Config**: `.ini`, `.cfg`
- **Logs**: `.log`
- **Text**: `.txt`

## Usage

1. Start the application
2. Type your message in the text box
3. Optionally upload a file (supports 30+ file formats)
4. Click "Send" or press Enter
5. Watch the AI respond with streaming animation

## New Features

### Smart File Type Detection

- **Automatic Recognition**: The bot automatically detects file types and displays appropriate icons
- **Visual Indicators**: Each file type has a unique emoji icon (🐍 for Python, 🟨 for JavaScript, ⚙️ for C++, etc.)
- **Type-Specific Processing**: Different file types are processed with specialized handlers

### Enhanced File Support

- **Programming Languages**: Full support for 15+ programming languages
- **Data Processing**: CSV and XML files are parsed and formatted for better analysis
- **Web Development**: Complete support for HTML, CSS, and related technologies
- **Documentation**: Markdown, LaTeX, and other documentation formats

### Improved User Experience

- **File Type Display**: Shows file type in chat messages (e.g., "📄 (with PDF)", "🐍 (with Python)")
- **Better Error Handling**: Graceful handling of unsupported or corrupted files
- **Enhanced Processing**: Specialized processing for different file types

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
- `csv` (built-in): CSV file processing
- `xml.etree.ElementTree` (built-in): XML file parsing

## Examples

### Uploading Code Files

```
User: "Can you review this JavaScript code?"
[Uploads: script.js]
Bot: "🟨 (with JavaScript) I'll analyze your JavaScript code..."
```

### Working with Data Files

```
User: "Analyze this CSV data"
[Uploads: data.csv]
Bot: "📊 (with CSV) I'll examine your CSV data..."
```

### Processing Documentation

```
User: "Help me understand this markdown file"
[Uploads: README.md]
Bot: "📝 (with Markdown) I'll help you understand this documentation..."
```

## File Type Icons

| File Type  | Icon | Description          |
| ---------- | ---- | -------------------- |
| Python     | 🐍   | Python files         |
| JavaScript | 🟨   | JavaScript/JSX files |
| TypeScript | 🔷   | TypeScript/TSX files |
| C/C++      | ⚙️   | C/C++ source files   |
| Java       | ☕   | Java files           |
| C#         | 🔷   | C# source files      |
| HTML       | 🌐   | HTML files           |
| CSS        | 🎨   | CSS/SCSS/SASS files  |
| JSON       | 📋   | JSON data files      |
| CSV        | 📊   | CSV data files       |
| PDF        | 📄   | PDF documents        |
| Markdown   | 📝   | Markdown files       |
| Bash       | 🐚   | Shell scripts        |
