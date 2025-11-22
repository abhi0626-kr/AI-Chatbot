# 🤖 Latest Gemini Chatbot 2025

A comprehensive AI chatbot powered by Google's latest Gemini API with cutting-edge features and best practices implementation.

## ✨ Features

- **Latest Gemini Models (September 2025)**
  - Gemini 2.5 Pro (enhanced reasoning)
  - Gemini 2.5 Flash (best price-performance) 
  - Gemini 2.0 Flash (next-generation features)

- **Advanced Capabilities**
  - Streaming responses for real-time interaction
  - Chat history management
  - Multiple interface options (CLI, Web, API)
  - Error handling and rate limiting
  - Secure API key management
  - Modern safety safeguards

- **Multiple Interfaces**
  - Command-line interface
  - Web-based chat interface
  - REST API server
  - Configurable and extensible

## 🚀 Quick Start

### 1. Get Your Gemini API Key

1. Visit [Google AI Studio](https://ai.google.dev/)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### 2. Setup Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env file and add your API key
GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Chatbot

**Command Line Interface:**
```bash
python app.py
```

**Web Interface:**
```bash
python flask_server.py
# Then open http://localhost:5000 in your browser
```

## 📁 Project Structure

```
latest_gemini_chatbot_2025/
├── app.py                 # Main CLI chatbot application
├── flask_server.py        # Web server with API endpoints
├── web_interface.html     # Modern web chat interface
├── config.py             # Configuration and settings
├── requirements.txt      # Python dependencies
├── .env.example         # Environment variables template
└── README.md           # This file
```

## 🔧 Configuration

### Available Models

| Model | Description | Best For |
|-------|-------------|----------|
| `gemini-2.5-pro` | Most advanced reasoning | Complex analysis, research |
| `gemini-2.5-flash` | Best price-performance | General chat, quick tasks |
| `gemini-2.0-flash` | Next-generation features | Real-time interactions |

### Environment Variables

- `GEMINI_API_KEY` - Your Gemini API key (required)
- `DEFAULT_MODEL` - Default model to use (optional)

## 🎮 Usage Examples

### Command Line
```bash
python app.py
# Choose model and start chatting
```

### Web Interface
```bash
python flask_server.py
# Open browser to http://localhost:5000
```

### API Integration
```python
from app import GeminiChatbot

chatbot = GeminiChatbot(api_key="your_key", model_name="gemini-2.5-flash")
response = chatbot.get_response("Hello, how are you?")
print(response)
```

## 🔐 Security Best Practices

- ✅ API keys stored in environment variables
- ✅ Input validation and sanitization
- ✅ Rate limiting protection
- ✅ Error handling with fallbacks
- ✅ Safety settings configured
- ✅ No hardcoded secrets in code

## 📈 Latest API Features (2025)

- **Enhanced Reasoning**: Adaptive thinking capabilities
- **Multimodal Support**: Text, image, audio, and video
- **Streaming Responses**: Real-time conversation flow
- **Safety Improvements**: Advanced content filtering
- **Better Performance**: Improved speed and accuracy
- **Tool Integration**: Function calling and external APIs

## 🛠️ Development

### Adding New Features

1. Fork the repository
2. Create your feature branch
3. Add your improvements
4. Test thoroughly
5. Submit a pull request

### Custom Models

To add support for new models, update the `AVAILABLE_MODELS` in `config.py`:

```python
AVAILABLE_MODELS = {
    'your-custom-model': {
        'name': 'Your Model Name',
        'description': 'Model description',
        'features': ['Feature 1', 'Feature 2'],
        'best_for': ['Use case 1', 'Use case 2']
    }
}
```

## 📊 Performance Tips

- Use `gemini-2.5-flash` for balanced performance
- Implement caching for repeated queries
- Use streaming for long responses
- Monitor API usage and costs
- Optimize prompts for better results

## 🚨 Troubleshooting

### Common Issues

**API Key Error:**
```
Error: GEMINI_API_KEY not found
```
**Solution:** Set your API key in the `.env` file

**Model Not Available:**
```
Error: Model not available
```
**Solution:** Check model name and your API access level

**Rate Limit Exceeded:**
```
Error: Rate limit exceeded
```
**Solution:** Implement longer delays between requests

## 📞 Support

For issues and questions:
- Check the [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- Review the troubleshooting section
- Check environment variable setup
- Verify API key permissions

## 🔄 Updates

This project uses the latest Gemini API features as of September 2025. Check for updates regularly to get new capabilities and improvements.

## ⚖️ License

This project is open source and available under the MIT License.

---

**Happy Chatting! 🎉**

Built with ❤️ using Google's Gemini API
