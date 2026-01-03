# 🚀 Modern RAG System - Complete Setup Guide

This guide provides detailed, step-by-step instructions for setting up the Modern RAG Q&A System.

## 📋 Table of Contents
1. [System Requirements](#system-requirements)
2. [Python Installation](#python-installation)
3. [Project Setup](#project-setup)
4. [API Key Configuration](#api-key-configuration)
5. [Running the Application](#running-the-application)
6. [Verification](#verification)
7. [Troubleshooting](#troubleshooting)
8. [Advanced Configuration](#advanced-configuration)

---

## 🖥️ System Requirements

### Minimum Requirements
- **Operating System**: Windows 10/11, macOS 10.14+, or Linux (Ubuntu 20.04+)
- **Python Version**: 3.10, 3.11, or 3.12
- **RAM**: 8GB minimum
- **Disk Space**: 5GB free (for models and dependencies)
- **Internet**: Stable connection for initial model downloads

### Recommended Requirements
- **RAM**: 16GB or more
- **CPU**: Multi-core processor (4+ cores)
- **GPU**: NVIDIA GPU with CUDA support (optional, for faster processing)
- **Internet Speed**: 10+ Mbps for faster model downloads

### Why Python 3.10+?
- **Type hints improvements**: Better static typing support
- **Performance**: 10-60% faster than Python 3.9
- **Library compatibility**: All modern AI libraries target 3.10+
- **Long-term support**: Active maintenance through 2026+

---

## 🐍 Python Installation

### Check Existing Python Version

```bash
python --version
# or
python3 --version
```

If you see Python 3.10, 3.11, or 3.12, you're good to go! Skip to [Project Setup](#project-setup).

### Installing Python (Windows)

1. **Download Python**
   - Visit [python.org/downloads](https://www.python.org/downloads/)
   - Download Python 3.11.x (recommended) or 3.10.x/3.12.x
   - Choose "Windows installer (64-bit)"

2. **Run Installer**
   - ✅ **IMPORTANT**: Check "Add Python to PATH"
   - Click "Install Now"
   - Wait for installation to complete

3. **Verify Installation**
   ```bash
   python --version
   pip --version
   ```

### Installing Python (macOS)

Using Homebrew (recommended):
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3.11
brew install python@3.11

# Verify
python3.11 --version
```

### Installing Python (Linux/Ubuntu)

```bash
# Update package list
sudo apt update

# Install Python 3.11
sudo apt install python3.11 python3.11-venv python3-pip

# Verify
python3.11 --version
```

---

## 📦 Project Setup

### Step 1: Get the Project Files

If you have the project as a zip file:
```bash
# Extract the zip file to a folder
# Navigate to the folder
cd path/to/modern-rag-system
```

If cloning from a repository:
```bash
git clone <repository-url>
cd modern-rag-system
```

### Step 2: Create Virtual Environment

**Why use a virtual environment?**
- Isolates project dependencies
- Prevents conflicts with other Python projects
- Easy to reproduce on different machines

**Windows:**
```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# You should see (venv) in your command prompt
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# You should see (venv) in your terminal prompt
```

**Troubleshooting Virtual Environment:**
- If `python -m venv` fails, install: `pip install virtualenv`
- On Ubuntu, you may need: `sudo apt install python3.11-venv`
- Always activate the venv before installing packages or running the app

### Step 3: Upgrade pip

```bash
# Ensure you have the latest pip
python -m pip install --upgrade pip
```

### Step 4: Install Dependencies

```bash
# Install all required packages
pip install -r requirements.txt
```

**Expected time**: 5-15 minutes (depending on internet speed)

**What's being installed:**
- Streamlit (UI framework)
- LangChain (AI framework)
- Hugging Face libraries (model access)
- FAISS (vector database)
- Document processing libraries
- And more...

**If installation fails:**
```bash
# Try installing with no cache
pip install --no-cache-dir -r requirements.txt

# Or install packages one by one to identify issues
pip install streamlit
pip install langchain
# ... etc
```

---

## 🔑 API Key Configuration

### Choose Your LLM Provider

You have two options:

#### Option A: OpenAI (Recommended - Best Quality)
- **Cost**: ~$0.50 per 1000 queries with GPT-3.5
- **Quality**: Best-in-class responses
- **Setup**: Requires credit card and billing setup

#### Option B: HuggingFace (Free Alternative)
- **Cost**: FREE (1,000 calls/month)
- **Quality**: Good (varies by model)
- **Setup**: No credit card needed, resets monthly

### Step 1A: Get OpenAI API Key (If Using OpenAI)

1. **Create Account**
   - Go to [platform.openai.com](https://platform.openai.com/)
   - Click "Sign Up"

2. **Add Billing**
   - Go to [Billing](https://platform.openai.com/account/billing)
   - Add payment method
   - Add credits ($5 minimum recommended)

3. **Generate API Key**
   - Go to [API Keys](https://platform.openai.com/api-keys)
   - Click "Create new secret key"
   - Name it (e.g., "RAG-System")
   - **Copy the key** (starts with `sk-`)
   - You won't see it again!

### Step 1B: Get HuggingFace API Key (If Using HuggingFace)

1. **Create Account**
   - Go to [huggingface.co](https://huggingface.co/)
   - Click "Sign Up"

2. **Generate API Token**
   - After logging in, click your profile picture
   - Select "Settings"
   - Click "Access Tokens" in the left sidebar
   - Click "New token"
   - Name it (e.g., "RAG-System")
   - Select "Read" permission
   - Click "Generate"
   - **Copy the token** (starts with `hf_`)

### Step 2: Configure Environment File

1. **Copy the example file**
   
   **Windows:**
   ```bash
   copy .env.example .env
   ```
   
   **macOS/Linux:**
   ```bash
   cp .env.example .env
   ```

2. **Edit the .env file**
   - Open `.env` in any text editor (Notepad, VSCode, etc.)
   - Choose your provider and configure accordingly:

3. **For OpenAI (Recommended):**
   ```env
   # Provider Selection
   LLM_PROVIDER=openai
   
   # API Keys
   OPENAI_API_KEY=sk-your_actual_key_here
   
   # Model
   LLM_MODEL=gpt-3.5-turbo
   
   # Embeddings (always uses HuggingFace, free)
   EMBEDDING_MODEL=sentence-transformers/all-mpnet-base-v2
   ```

4. **For HuggingFace (Free):**
   ```env
   # Provider Selection
   LLM_PROVIDER=huggingface
   
   # API Keys
   HUGGINGFACE_API_KEY=hf_your_actual_key_here
   
   # Model
   LLM_MODEL=google/flan-t5-base
   
   # Embeddings (always uses HuggingFace, free)
   EMBEDDING_MODEL=sentence-transformers/all-mpnet-base-v2
   ```

5. **Save the file**

**Security Notes:**
- ⚠️ **Never commit .env to git** (it's in .gitignore)
- ⚠️ **Don't share your API keys** publicly
- ✅ Keep .env file in project root only

**Switching Providers:**
Just change `LLM_PROVIDER` between `openai` and `huggingface` - no code changes needed!

---

## ▶️ Running the Application

### Step 1: Ensure Virtual Environment is Active

You should see `(venv)` in your command prompt. If not:

**Windows:** `venv\Scripts\activate`
**macOS/Linux:** `source venv/bin/activate`

### Step 2: Start the Application

```bash
streamlit run app.py
```

### Step 3: First Run (Model Downloads)

**First time running:**
- Models will download automatically (1-3 GB)
- This takes 3-10 minutes depending on internet speed
- You'll see download progress in the terminal
- Subsequent runs are much faster (models are cached)

**Download locations:**
- **Windows**: `C:\Users\YourName\.cache\huggingface`
- **macOS/Linux**: `~/.cache/huggingface`

### Step 4: Access the App

- Browser should open automatically to `http://localhost:8501`
- If not, manually navigate to the URL shown in terminal
- The app interface should appear!

### Step 5: Test the System

Try this quick test:
1. Select "Text" as input type
2. Paste this sample text:
   ```
   Python is a high-level programming language. It was created by Guido van Rossum and released in 1991. Python emphasizes code readability and uses significant indentation.
   ```
3. Click "Process & Create Knowledge Base"
4. Wait for success message
5. Ask: "Who created Python?"
6. Click "Get Answer"
7. You should get: "Guido van Rossum"

**If this works, your system is fully operational! 🎉**

---

## ✅ Verification

### Verification Checklist

Run through these checks to ensure everything is working:

#### ✅ Basic Setup
- [ ] Python 3.10+ installed (`python --version`)
- [ ] Virtual environment created and activated
- [ ] All packages installed without errors
- [ ] `.env` file exists with API key

#### ✅ Application Startup
- [ ] `streamlit run app.py` runs without errors
- [ ] Browser opens to application
- [ ] UI loads completely
- [ ] No error messages in terminal

#### ✅ Functionality Tests
- [ ] Can process text input
- [ ] Can upload PDF file
- [ ] Can upload DOCX file
- [ ] Can enter URL
- [ ] Vector store creates successfully
- [ ] Can ask questions
- [ ] Receives answers from AI

#### ✅ Performance
- [ ] Processing completes in reasonable time
- [ ] No memory errors
- [ ] UI remains responsive

### Manual Verification Commands

```bash
# Check Python version
python --version  # Should show 3.10, 3.11, or 3.12

# Check if packages are installed
pip list | grep streamlit
pip list | grep langchain
pip list | grep faiss

# Check if .env exists
# Windows:
dir .env
# macOS/Linux:
ls -la .env

# Test import of key modules
python -c "import streamlit; import langchain; import faiss; print('All imports successful!')"
```

---

## 🔧 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'X'"

**Cause**: Package not installed or wrong environment

**Solution**:
```bash
# Ensure virtual environment is active (should see (venv))
# Reinstall requirements
pip install -r requirements.txt

# Or install specific missing package
pip install <package-name>
```

---

### Issue: "HUGGINGFACE_API_KEY not found"

**Cause**: Environment file not configured

**Solution**:
1. Ensure `.env` file exists in project root
2. Check the file contains: `HUGGINGFACE_API_KEY=your_actual_key`
3. No spaces around the `=` sign
4. No quotes around the key
5. Restart the application

---

### Issue: "403 Forbidden" or "Model not found"

**Cause**: Model requires approval or wrong model name

**Solution**:
1. Check if model requires approval on Hugging Face
2. Visit model page and request access
3. Wait for approval (usually quick)
4. Or use alternative model:
   - Change `LLM_MODEL` in `.env`
   - Try: `google/flan-t5-large` (no approval needed)
   - Try: `mistralai/Mistral-7B-Instruct-v0.3`

---

### Issue: "Out of memory" errors

**Cause**: Insufficient RAM for model

**Solution**:
1. Close other applications
2. Use smaller models:
   ```env
   # In .env file
   EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
   LLM_MODEL=google/flan-t5-large
   ```
3. Reduce chunk size:
   ```env
   CHUNK_SIZE=500
   TOP_K_RESULTS=2
   ```
4. Consider upgrading RAM or using cloud services

---

### Issue: Very slow processing

**Cause**: CPU-only processing or large models

**Solution**:
1. **First run is always slow** (model downloads)
2. Check if models are downloaded (see download location above)
3. Use GPU if available:
   ```env
   DEVICE=cuda
   ```
4. Use smaller/faster models
5. Be patient - subsequent runs are much faster

---

### Issue: "Streamlit not found" or command not recognized

**Cause**: Virtual environment not activated or PATH issues

**Solution**:
```bash
# Windows
venv\Scripts\activate
python -m streamlit run app.py

# macOS/Linux
source venv/bin/activate
python -m streamlit run app.py
```

---

### Issue: PDF/DOCX processing fails

**Cause**: Corrupted files or wrong format

**Solution**:
1. Ensure file is valid (can open in reader)
2. Try different file
3. Check file size (very large files may timeout)
4. For PDFs: Ensure text is selectable (not scanned images)

---

### Issue: Port 8501 already in use

**Cause**: Another Streamlit app running

**Solution**:
```bash
# Use different port
streamlit run app.py --server.port 8502

# Or kill existing process
# Windows:
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# macOS/Linux:
lsof -ti:8501 | xargs kill -9
```

---

### Getting More Help

If you're still stuck:

1. **Check logs**: Look at `rag_system.log` for detailed errors
2. **Enable debug mode**: Set `LOG_LEVEL=DEBUG` in `.env`
3. **Test components**: Run `python tests/test_basic.py`
4. **Verify API key**: Test at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
5. **Check disk space**: Ensure 5GB+ free space
6. **Review dependencies**: Ensure all versions match `requirements.txt`

---

## 🎛️ Advanced Configuration

### Using GPU Acceleration

**Requirements:**
- NVIDIA GPU with CUDA support
- CUDA Toolkit installed
- cuDNN installed

**Setup:**
```bash
# Install GPU version of PyTorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install GPU version of FAISS
pip uninstall faiss-cpu
pip install faiss-gpu

# Update .env
DEVICE=cuda
```

### Custom Model Configuration

**Using different LLM:**
```env
# Fast and free (no approval needed)
LLM_MODEL=google/flan-t5-large

# High quality (may need approval)
LLM_MODEL=mistralai/Mistral-7B-Instruct-v0.3

# Balanced (default)
LLM_MODEL=meta-llama/Llama-3.2-3B-Instruct
```

**Using different embeddings:**
```env
# Fastest (smaller, less accurate)
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Balanced (default)
EMBEDDING_MODEL=sentence-transformers/all-mpnet-base-v2

# Multilingual
EMBEDDING_MODEL=sentence-transformers/paraphrase-multilingual-mpnet-base-v2
```

### Performance Tuning

**For faster processing:**
```env
CHUNK_SIZE=500          # Smaller chunks
CHUNK_OVERLAP=50        # Less overlap
TOP_K_RESULTS=2         # Fewer results
MAX_NEW_TOKENS=256      # Shorter answers
```

**For better quality:**
```env
CHUNK_SIZE=1500         # Larger chunks (more context)
CHUNK_OVERLAP=300       # More overlap (better continuity)
TOP_K_RESULTS=6         # More results (more comprehensive)
MAX_NEW_TOKENS=1024     # Longer answers
TEMPERATURE=0.7         # More creative responses
```

### Running on Server

**For remote access:**
```bash
streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

**With authentication:**
```bash
# Create credentials in .streamlit/secrets.toml
streamlit run app.py --server.enableCORS false
```

---

## 📚 Next Steps

After successful setup:

1. ✅ Read [README.md](README.md) for usage guide
2. ✅ Check [MIGRATION.md](MIGRATION.md) if updating from old version
3. ✅ Experiment with different models and settings
4. ✅ Try various document types
5. ✅ Adjust configuration for your use case

---

## 📊 Expected Performance

### First Run
- **Setup time**: 10-20 minutes (one-time)
- **Model download**: 3-10 minutes (one-time)
- **First document**: 30-60 seconds

### Subsequent Runs
- **App startup**: 5-10 seconds
- **Small document** (1-10 pages): 5-15 seconds
- **Medium document** (10-50 pages): 15-60 seconds
- **Large document** (50+ pages): 1-5 minutes
- **Query response**: 3-10 seconds

*Times vary based on hardware, model choice, and document complexity*

---

## ✨ Success Indicators

You know the setup is successful when:

1. ✅ App loads without errors
2. ✅ Can process at least one document type
3. ✅ Vector store creates successfully
4. ✅ Can ask questions and receive relevant answers
5. ✅ Source documents are shown correctly
6. ✅ No warnings about missing configurations
7. ✅ Log file shows successful operations

---

**Need more help?** Check the main [README.md](README.md) or review error logs in `rag_system.log`

**Ready to use?** Start with simple documents and gradually explore more complex use cases!

🎉 **Happy RAG-ing!**
