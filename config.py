"""
Configuration Management for Modern RAG System
==============================================
Centralized configuration using environment variables and constants.

Usage:
    from config import Config
    config = Config()
    print(config.LLM_MODEL)
"""

import os
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """
    Configuration class for RAG system.
    Loads settings from environment variables with sensible defaults.
    """
    
    def __init__(self):
        """Initialize configuration and validate required settings."""
        # LLM Provider Selection
        self.LLM_PROVIDER: str = os.getenv('LLM_PROVIDER', 'openai').lower()
        
        if self.LLM_PROVIDER not in ['openai', 'huggingface']:
            raise ValueError(
                f"Invalid LLM_PROVIDER: {self.LLM_PROVIDER}. "
                "Supported values: 'openai', 'huggingface'"
            )
        
        # API Keys
        self.HUGGINGFACE_API_KEY: Optional[str] = os.getenv('HUGGINGFACE_API_KEY')
        self.OPENAI_API_KEY: Optional[str] = os.getenv('OPENAI_API_KEY')
        
        # Validate required API key based on provider
        if self.LLM_PROVIDER == 'openai' and not self.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY not found in environment variables. "
                "Please add it to your .env file or change LLM_PROVIDER to 'huggingface'."
            )
        
        if self.LLM_PROVIDER == 'huggingface' and not self.HUGGINGFACE_API_KEY:
            raise ValueError(
                "HUGGINGFACE_API_KEY not found in environment variables. "
                "Please add it to your .env file or change LLM_PROVIDER to 'openai'."
            )
        
        # Set environment variables
        if self.HUGGINGFACE_API_KEY:
            os.environ['HUGGINGFACEHUB_API_TOKEN'] = self.HUGGINGFACE_API_KEY
        if self.OPENAI_API_KEY:
            os.environ['OPENAI_API_KEY'] = self.OPENAI_API_KEY
        
        # Model Configuration - set default based on provider
        if self.LLM_PROVIDER == 'openai':
            default_model = 'gpt-3.5-turbo'
        else:  # huggingface
            default_model = 'google/flan-t5-base'
        
        self.LLM_MODEL: str = os.getenv('LLM_MODEL', default_model)
        
        self.EMBEDDING_MODEL: str = os.getenv(
            'EMBEDDING_MODEL',
            'sentence-transformers/all-mpnet-base-v2'
        )
        
        # LLM Parameters
        self.TEMPERATURE: float = float(os.getenv('TEMPERATURE', '0.7'))
        self.MAX_NEW_TOKENS: int = int(os.getenv('MAX_NEW_TOKENS', '512'))
        
        # Text Splitting Parameters
        self.CHUNK_SIZE: int = int(os.getenv('CHUNK_SIZE', '1000'))
        self.CHUNK_OVERLAP: int = int(os.getenv('CHUNK_OVERLAP', '200'))
        
        # Retrieval Parameters
        self.TOP_K_RESULTS: int = int(os.getenv('TOP_K_RESULTS', '4'))
        
        # Device Configuration
        self.DEVICE: str = os.getenv('DEVICE', 'cpu')
        
        # Logging Configuration
        self.LOG_LEVEL: str = os.getenv('LOG_LEVEL', 'INFO')
        self.LOG_FILE: str = os.getenv('LOG_FILE', 'rag_system.log')
        
        # Validation
        self._validate_config()
    
    def _validate_config(self) -> None:
        """Validate configuration values."""
        if self.TEMPERATURE < 0 or self.TEMPERATURE > 1:
            raise ValueError(f"TEMPERATURE must be between 0 and 1, got {self.TEMPERATURE}")
        
        if self.CHUNK_SIZE < 100:
            raise ValueError(f"CHUNK_SIZE must be at least 100, got {self.CHUNK_SIZE}")
        
        if self.CHUNK_OVERLAP >= self.CHUNK_SIZE:
            raise ValueError(
                f"CHUNK_OVERLAP ({self.CHUNK_OVERLAP}) must be less than "
                f"CHUNK_SIZE ({self.CHUNK_SIZE})"
            )
        
        if self.TOP_K_RESULTS < 1:
            raise ValueError(f"TOP_K_RESULTS must be at least 1, got {self.TOP_K_RESULTS}")
    
    def __repr__(self) -> str:
        """Return string representation (hiding sensitive data)."""
        return (
            f"Config(\n"
            f"  LLM_MODEL='{self.LLM_MODEL}',\n"
            f"  EMBEDDING_MODEL='{self.EMBEDDING_MODEL}',\n"
            f"  TEMPERATURE={self.TEMPERATURE},\n"
            f"  CHUNK_SIZE={self.CHUNK_SIZE},\n"
            f"  CHUNK_OVERLAP={self.CHUNK_OVERLAP},\n"
            f"  TOP_K_RESULTS={self.TOP_K_RESULTS},\n"
            f"  DEVICE='{self.DEVICE}'\n"
            f")"
        )


# Constants
APP_NAME = "Modern RAG Q&A System"
APP_VERSION = "2.0.0"
MIN_PYTHON_VERSION = "3.10"
SUPPORTED_FILE_TYPES = {
    'PDF': ['.pdf'],
    'DOCX': ['.docx', '.doc'],
    'TXT': ['.txt']
}
