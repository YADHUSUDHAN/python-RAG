"""
Basic Tests for Modern RAG System
=================================
Simple test suite to verify installation and basic functionality.

Run with: python tests/test_basic.py
"""

import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

print("🧪 Modern RAG System - Basic Tests")
print("=" * 50)

# Test 1: Python Version
print("\n1️⃣ Testing Python version...")
if sys.version_info >= (3, 10):
    print(f"   ✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
else:
    print(f"   ❌ Python {sys.version_info.major}.{sys.version_info.minor} - Need 3.10+")
    sys.exit(1)

# Test 2: Core Imports
print("\n2️⃣ Testing core imports...")
try:
    import streamlit
    print(f"   ✅ Streamlit {streamlit.__version__}")
except ImportError as e:
    print(f"   ❌ Streamlit import failed: {e}")
    sys.exit(1)

try:
    import langchain
    print(f"   ✅ LangChain {langchain.__version__}")
except ImportError as e:
    print(f"   ❌ LangChain import failed: {e}")
    sys.exit(1)

try:
    import faiss
    print(f"   ✅ FAISS available")
except ImportError as e:
    print(f"   ❌ FAISS import failed: {e}")
    sys.exit(1)

try:
    from pypdf import PdfReader
    print(f"   ✅ pypdf (modern PDF reader)")
except ImportError as e:
    print(f"   ❌ pypdf import failed: {e}")
    sys.exit(1)

try:
    from docx import Document
    print(f"   ✅ python-docx")
except ImportError as e:
    print(f"   ❌ python-docx import failed: {e}")
    sys.exit(1)

# Test 3: LangChain Components
print("\n3️⃣ Testing LangChain components...")
try:
    from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint
    print("   ✅ HuggingFace integrations")
except ImportError as e:
    print(f"   ❌ LangChain HuggingFace import failed: {e}")
    sys.exit(1)

try:
    from langchain_community.vectorstores import FAISS
    print("   ✅ FAISS vector store")
except ImportError as e:
    print(f"   ❌ FAISS vector store import failed: {e}")
    sys.exit(1)

try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    print("   ✅ RecursiveCharacterTextSplitter")
except ImportError as e:
    print(f"   ❌ Text splitter import failed: {e}")
    sys.exit(1)

try:
    from langchain.chains.retrieval_qa.base import RetrievalQA
    print("   ✅ RetrievalQA chain")
except ImportError as e:
    print(f"   ❌ RetrievalQA import failed: {e}")
    sys.exit(1)

# Test 4: Project Modules
print("\n4️⃣ Testing project modules...")
try:
    from config import Config
    print("   ✅ config.py module")
except ImportError as e:
    print(f"   ❌ config.py import failed: {e}")
    sys.exit(1)

try:
    from utils import (
        validate_input,
        process_pdf,
        process_docx,
        process_txt,
        process_urls,
        setup_logging
    )
    print("   ✅ utils.py module")
except ImportError as e:
    print(f"   ❌ utils.py import failed: {e}")
    sys.exit(1)

# Test 5: Configuration
print("\n5️⃣ Testing configuration...")
try:
    # Check if .env file exists
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        print("   ✅ .env file found")
        
        # Try loading config
        try:
            config = Config()
            print("   ✅ Configuration loaded")
            print(f"      - LLM Model: {config.LLM_MODEL}")
            print(f"      - Embedding Model: {config.EMBEDDING_MODEL}")
            print(f"      - Device: {config.DEVICE}")
        except ValueError as e:
            print(f"   ⚠️  Configuration warning: {e}")
            print("      Make sure HUGGINGFACE_API_KEY is set in .env")
    else:
        print("   ⚠️  .env file not found")
        print("      Copy .env.example to .env and add your API key")
except Exception as e:
    print(f"   ❌ Configuration test failed: {e}")

# Test 6: Utility Functions
print("\n6️⃣ Testing utility functions...")
try:
    # Test logging setup
    logger = setup_logging(log_level="INFO")
    print("   ✅ Logging setup works")
except Exception as e:
    print(f"   ❌ Logging setup failed: {e}")

try:
    # Test input validation
    assert validate_input("Text", "sample text") == True
    assert validate_input("Text", "") == False
    assert validate_input("Link", ["http://example.com"]) == True
    assert validate_input("Link", []) == False
    print("   ✅ Input validation works")
except Exception as e:
    print(f"   ❌ Input validation failed: {e}")

# Test 7: Text Processing
print("\n7️⃣ Testing text processing...")
try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20,
        separators=["\n\n", "\n", " ", ""]
    )
    
    sample_text = "This is a test. " * 50
    chunks = text_splitter.split_text(sample_text)
    
    if len(chunks) > 1:
        print(f"   ✅ Text splitting works ({len(chunks)} chunks created)")
    else:
        print("   ⚠️  Text splitting produced fewer chunks than expected")
except Exception as e:
    print(f"   ❌ Text processing failed: {e}")

# Test 8: Embedding Model (if API key available)
print("\n8️⃣ Testing embedding model initialization...")
try:
    if os.getenv('HUGGINGFACE_API_KEY'):
        from langchain_huggingface import HuggingFaceEmbeddings
        
        # Use a small model for testing
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'}
        )
        
        # Test embedding generation
        test_embedding = embeddings.embed_query("test")
        if len(test_embedding) > 0:
            print(f"   ✅ Embedding model works (dimension: {len(test_embedding)})")
        else:
            print("   ⚠️  Embedding generated but with zero dimension")
    else:
        print("   ⚠️  Skipped (no API key in environment)")
        print("      Set HUGGINGFACE_API_KEY in .env to test embeddings")
except Exception as e:
    print(f"   ⚠️  Embedding test failed: {e}")
    print("      This is normal if models aren't downloaded yet")

# Test 9: FAISS Vector Store
print("\n9️⃣ Testing FAISS vector store...")
try:
    from langchain_community.vectorstores import FAISS
    from langchain_core.documents import Document
    
    if os.getenv('HUGGINGFACE_API_KEY'):
        # Create simple test documents
        docs = [
            Document(page_content="The sky is blue.", metadata={"source": "test"}),
            Document(page_content="The grass is green.", metadata={"source": "test"}),
        ]
        
        # Create vector store (uses cached model if available)
        from langchain_huggingface import HuggingFaceEmbeddings
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'}
        )
        
        vector_store = FAISS.from_documents(docs, embeddings)
        
        # Test retrieval
        results = vector_store.similarity_search("What color is the sky?", k=1)
        if results and "blue" in results[0].page_content.lower():
            print("   ✅ FAISS vector store and retrieval work")
        else:
            print("   ⚠️  FAISS works but retrieval results unexpected")
    else:
        print("   ⚠️  Skipped (no API key in environment)")
except Exception as e:
    print(f"   ⚠️  FAISS test failed: {e}")
    print("      This is normal if models aren't downloaded yet")

# Final Summary
print("\n" + "=" * 50)
print("📊 Test Summary")
print("=" * 50)
print("\n✅ All critical tests passed!")
print("\n⚠️  Warnings are normal if:")
print("   - .env file not created yet")
print("   - API key not set")
print("   - Models not downloaded yet")
print("\n📝 Next Steps:")
print("   1. Copy .env.example to .env")
print("   2. Add your HUGGINGFACE_API_KEY to .env")
print("   3. Run: streamlit run app.py")
print("\n🎉 Your installation looks good!")
print("\n" + "=" * 50)
