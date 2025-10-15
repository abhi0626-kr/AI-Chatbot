#!/usr/bin/env python3
"""
Test runner for Gemini Chatbot project
"""

import os
from dotenv import load_dotenv
import sys
import json
from datetime import datetime

def test_environment():
    """Test environment setup"""
    print("🔍 Testing Environment Setup...")

    issues = []

    # Check Python version
    if sys.version_info < (3, 8):
        issues.append("Python 3.8+ required")
    else:
        print("✅ Python version OK")

    # Check API key
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        issues.append("GEMINI_API_KEY not set")
    else:
        print("✅ API key configured")

    # Check dependencies
    try:
        import google.generativeai as genai
        print("✅ google-generativeai installed")
    except ImportError:
        issues.append("google-generativeai not installed")

    return issues

def test_config():
    """Test configuration"""
    print("\n🔍 Testing Configuration...")

    try:
        from config import Config
        validation = Config.validate_config()

        if validation['valid']:
            print("✅ Configuration valid")
        else:
            print("❌ Configuration issues:")
            for issue in validation['issues']:
                print(f"  - {issue}")

        return validation['issues']
    except Exception as e:
        return [f"Config import error: {e}"]

def test_basic_functionality():
    """Test basic chatbot functionality"""
    print("\n🔍 Testing Basic Functionality...")

    issues = []

    try:
        from app import GeminiChatbot
        api_key = os.getenv('GEMINI_API_KEY')

        if api_key:
            chatbot = GeminiChatbot(api_key, "gemini-2.5-flash")

            # Test simple response
            response = chatbot.get_response("Say 'Hello World' in response.")

            if response and len(response) > 0:
                print("✅ Basic chat functionality working")
            else:
                issues.append("Empty response from chatbot")
        else:
            issues.append("Cannot test without API key")

    except Exception as e:
        issues.append(f"Chatbot test failed: {e}")

    return issues

def test_web_server():
    """Test Flask server setup"""
    print("\n🔍 Testing Web Server...")

    issues = []

    try:
        from flask_server import app

        with app.test_client() as client:
            # Test health endpoint
            response = client.get('/api/health')

            if response.status_code == 200:
                print("✅ Web server responds correctly")
            else:
                issues.append(f"Health endpoint returned {response.status_code}")

    except Exception as e:
        issues.append(f"Web server test failed: {e}")

    return issues

def main():
    # Load environment variables from .env file
    load_dotenv()
    """Main test runner"""
    print("🧪 Gemini Chatbot Test Suite")
    print("=" * 50)

    all_issues = []

    # Run all tests
    all_issues.extend(test_environment())
    all_issues.extend(test_config())
    all_issues.extend(test_basic_functionality())
    all_issues.extend(test_web_server())

    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Summary")

    if not all_issues:
        print("✅ All tests passed! Your chatbot is ready to use.")
        print("\n🚀 Getting Started:")
        print("  • Run: python app.py (for CLI)")
        print("  • Run: python flask_server.py (for web interface)")
    else:
        print("❌ Issues found:")
        for i, issue in enumerate(all_issues, 1):
            print(f"  {i}. {issue}")
        print("\n🔧 Fix these issues before using the chatbot.")

    # Save test results
    test_results = {
        'timestamp': datetime.now().isoformat(),
        'total_issues': len(all_issues),
        'issues': all_issues,
        'status': 'PASS' if not all_issues else 'FAIL'
    }

    with open('test_results.json', 'w') as f:
        json.dump(test_results, f, indent=2)

    print(f"\n📄 Test results saved to test_results.json")

    return 0 if not all_issues else 1

if __name__ == "__main__":
    sys.exit(main())
