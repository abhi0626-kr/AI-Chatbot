import os
from typing import Dict, Any

class Config:
    """Configuration settings for the Gemini Chatbot"""

    # API Configuration
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    DEFAULT_MODEL = os.getenv('DEFAULT_MODEL', 'gemini-2.5-flash')

    # Available Models (September 2025)
    AVAILABLE_MODELS = {
        'gemini-2.5-pro': {
            'name': 'Gemini 2.5 Pro',
            'description': 'Most advanced reasoning and complex tasks',
            'features': ['Enhanced thinking', 'Advanced coding', 'Multimodal understanding'],
            'best_for': ['Complex analysis', 'Research', 'Advanced coding tasks']
        },
        'gemini-2.5-flash': {
            'name': 'Gemini 2.5 Flash',
            'description': 'Best price-performance with adaptive thinking',
            'features': ['Cost efficient', 'Fast responses', 'Good reasoning'],
            'best_for': ['General chat', 'Quick tasks', 'Daily assistance']
        },
        'gemini-2.0-flash': {
            'name': 'Gemini 2.0 Flash',
            'description': 'Next generation features and real-time streaming',
            'features': ['Real-time capabilities', 'Advanced features', 'High speed'],
            'best_for': ['Real-time interactions', 'Streaming responses']
        }
    }

    # Chat Configuration
    MAX_CHAT_HISTORY = 100
    RATE_LIMIT_DELAY = 0.1  # seconds between requests

    # Safety Settings
    SAFETY_SETTINGS = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        }
    ]

    # System Instructions
    SYSTEM_INSTRUCTION = """You are a helpful AI assistant powered by Google's latest Gemini API (2025). 
    You provide accurate, informative, and engaging responses while maintaining a professional yet friendly tone.

    Key capabilities:
    - Answer questions across various topics
    - Help with coding and technical problems
    - Assist with creative writing and brainstorming
    - Provide analysis and explanations
    - Support learning and education

    Guidelines:
    - Be helpful and accurate
    - If unsure, acknowledge uncertainty
    - Maintain user privacy and safety
    - Provide step-by-step guidance when needed
    - Use examples to clarify complex concepts
    """

    @classmethod
    def validate_config(cls) -> Dict[str, Any]:
        """Validate configuration and return status"""
        issues = []

        if not cls.GEMINI_API_KEY:
            issues.append("GEMINI_API_KEY not set")

        if cls.DEFAULT_MODEL not in cls.AVAILABLE_MODELS:
            issues.append(f"DEFAULT_MODEL '{cls.DEFAULT_MODEL}' not in available models")

        return {
            'valid': len(issues) == 0,
            'issues': issues,
            'config': {
                'api_key_set': bool(cls.GEMINI_API_KEY),
                'default_model': cls.DEFAULT_MODEL,
                'available_models': list(cls.AVAILABLE_MODELS.keys())
            }
        }
