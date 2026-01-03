# 🤖 Modern RAG Q&A System

A production-ready **Retrieval-Augmented Generation (RAG)** system built with the latest AI technologies (2024-2026 standards). Upload documents, ask questions, and get AI-powered answers based on your content.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![LangChain](https://img.shields.io/badge/LangChain-1.2+-green.svg)](https://python.langchain.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.39-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

### 📚 Multiple Input Sources
- **Web URLs**: Load content from multiple websites
- **PDF Documents**: Extract text from PDF files
- **Word Documents**: Support for DOCX files
- **Text Files**: Plain text file upload
- **Direct Text**: Paste text directly into the app

### 🧠 Advanced AI Capabilities
- **OpenAI Integration**: Best-in-class GPT models (gpt-3.5-turbo, gpt-4)
- **Free Alternatives**: HuggingFace models (1000 calls/month, resets monthly)
- **Semantic Search**: Find relevant information using vector embeddings
- **Context-Aware Answers**: Generate accurate responses based on your documents
- **Source Attribution**: See which documents were used to generate answers
- **Easy Model Switching**: Change models by editing `.env` file

### 🎯 Modern Architecture
- **Latest LangChain APIs**: Using LangChain 1.2+ patterns (updated January 2026)
- **Modern Dependencies**: All libraries updated to 2024-2026 versions
- **OpenAI & HuggingFace**: Support for both paid and free LLM providers
- **Type Safety**: Full type hints throughout the codebase
- **Comprehensive Logging**: Track system behavior for debugging
- **Error Handling**: Graceful failure recovery

## 🚀 Quick Start

### Prerequisites
- Python 3.10, 3.11, or 3.12
- **Choose ONE:**
  - **OpenAI API key** ([Get one](https://platform.openai.com/api-keys)) - Best quality, ~$0.50/1000 queries
  - **HuggingFace API key** ([Get one](https://huggingface.co/settings/tokens)) - Free, 1000 calls/month
- 8GB RAM minimum
- Internet connection for model downloads

### Installation

1. **Clone or download this repository**
   ```bash
   cd modern-rag-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env and add your API key
   # For OpenAI (recommended):
   OPENAI_API_KEY=sk-your_key_here
   LLM_MODEL=gpt-3.5-turbo
   
   # OR for HuggingFace (free):
   HUGGINGFACE_API_KEY=hf_your_key_here
   LLM_MODEL=google/flan-t5-base
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, navigate to the URL shown in the terminal

## 📖 Usage Guide

### Step 1: Add Knowledge
1. Select your input type (Text, PDF, DOCX, TXT, or Link)
2. Provide your content:
   - **Text**: Paste directly
   - **Files**: Upload using the file picker
   - **URLs**: Enter one or more web addresses
3. Click "Process & Create Knowledge Base"
4. Wait for processing to complete (progress shown in UI)

### Step 2: Ask Questions
1. Once the knowledge base is ready, enter your question
2. Click "Get Answer"
3. View the AI-generated answer with source documents

## 🔄 Changing Models

**Quick switch** (same provider): Edit `.env` line 21
```bash
LLM_MODEL=gpt-4  # or gpt-3.5-turbo, google/flan-t5-base, etc.
```

**Full switch** (OpenAI ↔️ HuggingFace): See [MODEL_SWITCHING_GUIDE.md](MODEL_SWITCHING_GUIDE.md)

**Free alternatives**: See [FREE_MODELS_GUIDE.md](FREE_MODELS_GUIDE.md)
4. Expand "View Source Documents" to see which parts of your documents were used

### Tips for Best Results
- **Chunk Size**: Default 1000 characters works well for most documents
- **Question Specificity**: More specific questions yield better answers
- **Multiple Sources**: Combining multiple documents improves answer quality
- **URL Content**: Ensure URLs contain substantial text content

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Streamlit UI Layer                      │
├─────────────────────────────────────────────────────────────┤
│                      RAGSystem Class                        │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │   Document   │→ │   Embedding  │→ │  Vector Store   │  │
│  │  Processing  │  │  Generation  │  │    (FAISS)      │  │
│  └──────────────┘  └──────────────┘  └─────────────────┘  │
│                            ↓                                │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │   Question   │→ │  Retrieval   │→ │   LLM Answer    │  │
│  │    Input     │  │   (Top-K)    │  │   Generation    │  │
│  └──────────────┘  └──────────────┘  └─────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Key Components

- **app.py**: Main Streamlit application with UI logic
- **config.py**: Centralized configuration management
- **utils.py**: Document processing and utility functions
- **requirements.txt**: Exact dependency versions

### Technologies Used

| Component | Technology | Version |
|-----------|-----------|---------|
| UI Framework | Streamlit | 1.39.0 |
| LLM Framework | LangChain | 1.2.0+ |
| LLM Provider | OpenAI | GPT-3.5-turbo (default) |
| LLM Alternative | HuggingFace | Free models available |
| Embeddings | Sentence Transformers | 3.3.1 |
| Vector Store | FAISS | 1.9.0 |
| PDF Processing | pypdf | 5.1.0 |
| DOCX Processing | python-docx | 1.1.2 |

## ⚙️ Configuration

### Environment Variables

Edit the `.env` file to customize:

```env
# Required (choose one)
OPENAI_API_KEY=sk-your_key_here        # For OpenAI (paid)
HUGGINGFACE_API_KEY=hf_your_key_here   # For HuggingFace (free)

# Model Selection
LLM_MODEL=gpt-3.5-turbo                # OpenAI model
# LLM_MODEL=google/flan-t5-base        # HuggingFace free model
EMBEDDING_MODEL=sentence-transformers/all-mpnet-base-v2

# LLM Parameters
TEMPERATURE=0.7              # 0.0-1.0, higher = more creative
MAX_NEW_TOKENS=512          # Maximum response length

# Text Processing
CHUNK_SIZE=1000             # Document chunk size
CHUNK_OVERLAP=200           # Overlap between chunks
TOP_K_RESULTS=4             # Number of chunks to retrieve

# System
DEVICE=cpu                  # 'cpu' or 'cuda'
LOG_LEVEL=INFO             # DEBUG, INFO, WARNING, ERROR
```

### Supported Models

#### OpenAI Models (Paid, Best Quality)
- `gpt-3.5-turbo` (default, $0.50/1000 queries)
- `gpt-4` (highest quality, $2.50/1000 queries)
- `gpt-4-turbo` (balanced speed/quality)

#### HuggingFace Models (Free, 1000 calls/month)
- `google/flan-t5-base` (fastest, recommended for free tier)
- `mistralai/Mistral-7B-Instruct-v0.2` (best free quality)
- `meta-llama/Llama-2-7b-chat-hf` (good alternative)

See [MODEL_SWITCHING_GUIDE.md](MODEL_SWITCHING_GUIDE.md) for switching instructions.

#### Embedding Models (for semantic search)
- `sentence-transformers/all-mpnet-base-v2` (default, best quality)
- `sentence-transformers/all-MiniLM-L6-v2` (faster, smaller)
- `sentence-transformers/paraphrase-multilingual-mpnet-base-v2` (multilingual)

## 📊 Performance Considerations

### Memory Requirements
- **Minimum**: 8GB RAM
- **Recommended**: 16GB RAM for larger documents
- **GPU**: Optional but recommended for faster processing

### Processing Times (approximate)
- **Small document** (1-10 pages): 5-15 seconds
- **Medium document** (10-50 pages): 15-60 seconds
- **Large document** (50+ pages): 1-5 minutes
- **First run**: Additional 1-3 minutes for model downloads

### Optimization Tips
1. **Use GPU**: Set `DEVICE=cuda` if you have a compatible GPU
2. **Adjust chunk size**: Smaller chunks = faster but less context
3. **Reduce TOP_K_RESULTS**: Fewer chunks = faster responses
4. **Choose smaller models**: Trade quality for speed if needed

## 🔧 Troubleshooting

### Common Issues

**Issue**: "OPENAI_API_KEY not found" or "HUGGINGFACE_API_KEY not found"
- **Solution**: Ensure `.env` file has the correct API key for your chosen provider

**Issue**: "Error code: 429" (OpenAI) or "402 Payment Required" (HuggingFace)
- **Solution**: 
  - OpenAI: Add credits at https://platform.openai.com/account/billing
  - HuggingFace: Wait until next month (free tier resets monthly) or try different model

**Issue**: "Model not supported for task text-generation"
- **Solution**: Try a different model from [MODEL_SWITCHING_GUIDE.md](MODEL_SWITCHING_GUIDE.md)

**Issue**: Out of memory errors
- **Solution**: 
  - Use a smaller embedding model: `sentence-transformers/all-MiniLM-L6-v2`
  - Reduce CHUNK_SIZE in `.env`
  - Close other applications

**Issue**: Slow processing
- **Solution**:
  - First run downloads models (one-time delay)
  - Use GPU if available
  - Consider smaller models

**Issue**: "No module named 'X'"
- **Solution**: Reinstall requirements: `pip install -r requirements.txt`

### Getting Help
1. Check [SETUP.md](SETUP.md) for detailed setup instructions
2. Review [MIGRATION.md](MIGRATION.md) if upgrading from old version
3. Check logs in `rag_system.log` for detailed error messages
4. Ensure all dependencies are installed correctly

## 🧪 Testing

Run the basic test suite:

```bash
python tests/test_basic.py
```

This will verify:
- Configuration loading
- Embedding model initialization
- Document processing functions
- Vector store creation

## 📝 Development

### Project Structure
```
modern-rag-system/
├── app.py                        # Main Streamlit application
├── config.py                     # Configuration management
├── utils.py                      # Helper functions
├── test_rag.py                   # Component testing script
├── requirements.txt              # Dependencies
├── .env.example                  # Environment template
├── .env                          # Your config (not in git)
├── README.md                     # This file
├── SETUP.md                      # Detailed setup guide
├── MIGRATION.md                  # Migration from old version
├── MODEL_SWITCHING_GUIDE.md      # How to change models
├── FREE_MODELS_GUIDE.md          # Free alternatives & HuggingFace info
├── PROJECT_SUMMARY.md            # Technical overview
├── QUICK_REFERENCE.md            # Quick reference
└── tests/
    └── test_basic.py             # Basic tests
```

### Testing
Run the diagnostic test before using the app:
```bash
python test_rag.py
```
This tests all 7 components without running Streamlit.

### Code Style
- Follows PEP 8 guidelines
- Type hints throughout
- Comprehensive docstrings
- Logging for all major operations

### Contributing
Contributions are welcome! Please:
1. Follow the existing code style
2. Add tests for new features
3. Update documentation
4. Ensure no deprecation warnings

## 📄 License

This project is licensed under the MIT License. See LICENSE file for details.

## 🙏 Acknowledgments

Built with:
- [LangChain](https://python.langchain.com/) - LLM application framework
- [OpenAI](https://openai.com/) - GPT models
- [Hugging Face](https://huggingface.co/) - Free model hosting and APIs
- [Streamlit](https://streamlit.io/) - Web application framework
- [FAISS](https://github.com/facebookresearch/faiss) - Vector similarity search

## 📚 Additional Resources

- [Model Switching Guide](MODEL_SWITCHING_GUIDE.md) - Change LLM models
- [Free Models Guide](FREE_MODELS_GUIDE.md) - Free alternatives to OpenAI
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Hugging Face Documentation](https://huggingface.co/docs)
- [Streamlit Documentation](https://docs.streamlit.io/)

## 🔄 Version History

- **v2.0.0** (January 2026) - Complete modernization
  - Updated to LangChain 1.2+
  - Added OpenAI integration (GPT-3.5/4)
  - Maintained HuggingFace free tier support
  - Fixed all deprecated imports and APIs
  - Modern error handling and logging
  - Comprehensive documentation with guides
  - Component testing script

- **v1.0.0** (Legacy) - Original implementation
  - Basic RAG functionality
  - LangChain 0.3
  - HuggingFace only

---

**Made with ❤️ for the AI community**

For questions or issues, please check the documentation or create an issue.
