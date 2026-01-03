"""
Quick test script to verify RAG system components
Run: python test_rag.py
"""

import os
os.environ["USER_AGENT"] = "ModernRAG/2.0.0"

print("=" * 60)
print("RAG SYSTEM TEST")
print("=" * 60)

# Test 1: Configuration
print("\n1. Testing Configuration...")
try:
    from config import Config
    config = Config()
    print("   ✅ Config loaded")
    print(f"   Model: {config.LLM_MODEL}")
except Exception as e:
    print(f"   ❌ Config failed: {e}")
    exit(1)

# Test 2: Embeddings
print("\n2. Testing Embeddings...")
try:
    from langchain_huggingface import HuggingFaceEmbeddings
    embeddings = HuggingFaceEmbeddings(
        model_name=config.EMBEDDING_MODEL,
        model_kwargs={'device': config.DEVICE},
        encode_kwargs={'normalize_embeddings': True}
    )
    test_embed = embeddings.embed_query("test")
    print(f"   ✅ Embeddings work (dimension: {len(test_embed)})")
except Exception as e:
    print(f"   ❌ Embeddings failed: {e}")
    exit(1)

# Test 3: LLM Initialization
print("\n3. Testing LLM...")
try:
    if config.LLM_PROVIDER == 'openai':
        from langchain_openai import ChatOpenAI
        llm = ChatOpenAI(
            model=config.LLM_MODEL,
            temperature=config.TEMPERATURE,
            max_tokens=config.MAX_NEW_TOKENS
        )
    elif config.LLM_PROVIDER == 'huggingface':
        from langchain_huggingface import HuggingFaceEndpoint
        llm = HuggingFaceEndpoint(
            repo_id=config.LLM_MODEL,
            huggingfacehub_api_token=config.HUGGINGFACE_API_KEY,
            temperature=config.TEMPERATURE,
            max_new_tokens=config.MAX_NEW_TOKENS,
            timeout=120
        )
    else:
        raise ValueError(f"Unsupported LLM provider: {config.LLM_PROVIDER}")
    print("   ✅ LLM initialized")
except Exception as e:
    print(f"   ❌ LLM init failed: {e}")
    exit(1)

# Test 4: Document Processing
print("\n4. Testing Document Processing...")
try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
    from langchain_core.documents import Document
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20
    )
    
    test_doc = Document(
        page_content="Python was created by Guido van Rossum in 1991. It emphasizes code readability.",
        metadata={"source": "test"}
    )
    
    splits = text_splitter.split_documents([test_doc])
    print(f"   ✅ Text splitting works ({len(splits)} chunks)")
except Exception as e:
    print(f"   ❌ Document processing failed: {e}")
    exit(1)

# Test 5: Vector Store
print("\n5. Testing Vector Store...")
try:
    from langchain_community.vectorstores import FAISS
    
    vector_store = FAISS.from_documents(splits, embeddings)
    print("   ✅ Vector store created")
except Exception as e:
    print(f"   ❌ Vector store failed: {e}")
    exit(1)

# Test 6: Retrieval
print("\n6. Testing Retrieval...")
try:
    retriever = vector_store.as_retriever(search_kwargs={"k": 2})
    docs = retriever.invoke("Who created Python?")
    print(f"   ✅ Retrieval works ({len(docs)} docs found)")
except Exception as e:
    print(f"   ❌ Retrieval failed: {e}")
    exit(1)

# Test 7: Simple Q&A Test
print("\n7. Testing LLM Query...")
print("   (This may take 10-30 seconds...)")
try:
    # Get relevant docs
    docs = retriever.invoke("Who created Python?")
    context = "\n\n".join([doc.page_content for doc in docs])
    
    # Create simple prompt
    prompt = f"Answer the question based on the context:\n\nContext: {context}\n\nQuestion: Who created Python?\n\nAnswer:"
    
    # Query LLM
    answer = llm.invoke(prompt)
    # Extract content from AIMessage object
    answer_text = answer.content if hasattr(answer, 'content') else str(answer)
    print(f"   ✅ Q&A works!")
    print(f"   Question: Who created Python?")
    print(f"   Answer: {answer_text[:200] if len(answer_text) > 200 else answer_text}")
except Exception as e:
    print(f"   ❌ Q&A failed: {e}")
    print(f"   Error type: {type(e).__name__}")
    import traceback
    traceback.print_exc()
    exit(1)

print("\n" + "=" * 60)
print("✅ ALL TESTS PASSED - System is working!")
print("=" * 60)
print("\nYou can now run: streamlit run app.py")
