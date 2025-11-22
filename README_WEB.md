# Jarvis - AI Chatbot Web Interface

A standalone web-based AI chatbot interface that can be opened directly in any modern browser for public access and demonstration purposes.

## 🚀 Quick Start

1. **Open the Interface**: Simply open `chatbot_web.html` in any modern web browser
2. **Get API Key**: You'll be prompted to enter your Gemini API key (get one at [Google AI Studio](https://makersuite.google.com/app/apikey))
3. **Start Chatting**: Begin your conversation with the AI assistant!

## ✨ Features

### 🤖 AI Integration
- **Direct Gemini API Integration**: No backend server required
- **Latest Gemini 2.5 Flash Model**: Fast and efficient responses
- **Safety Settings**: Built-in content filtering and safety measures

### 💬 Chat Interface
- **Modern UI**: Clean, responsive design with smooth animations
- **Dark/Light Theme**: Toggle between themes with the moon/sun button
- **Code Syntax Highlighting**: Automatic highlighting for code blocks
- **Copy Code**: One-click copying of code snippets
- **Message Reactions**: Interactive emoji reactions for messages

### 🎤 Voice Features
- **Voice Input**: Click the microphone button to speak your messages
- **Voice Output**: The AI can read responses aloud
- **Real-time Feedback**: Visual indicators for listening and speaking states

### 📱 Responsive Design
- **Mobile Friendly**: Optimized for smartphones and tablets
- **Touch Interactions**: Touch-friendly buttons and controls
- **Adaptive Layout**: Adjusts to different screen sizes

### 🔧 Advanced Features
- **Auto-resizing Input**: Text area grows as you type
- **Keyboard Shortcuts**: Enter to send, Shift+Enter for new line
- **Connection Status**: Visual indicator for API connectivity
- **Error Handling**: Graceful error messages and recovery
- **Local Storage**: Remembers your API key and theme preference

## 🔑 API Key Setup

### Option 1: URL Parameter (Recommended for Public Sharing)
Add your API key to the URL:
```
file:///path/to/chatbot_web.html?api_key=YOUR_API_KEY_HERE
```

### Option 2: Local Storage
The interface will prompt you for your API key and remember it for future sessions.

### Option 3: Manual Entry
Simply open the HTML file and enter your API key when prompted.

## 🌐 Public Access

This interface is designed for public web access:

- **No Server Required**: Runs entirely in the browser
- **Cross-Platform**: Works on Windows, Mac, Linux, iOS, Android
- **Shareable**: Can be hosted on any web server or shared as a file
- **Demo Ready**: Perfect for demonstrations and presentations

## 🎨 Customization

### Adding Your Branding
Edit the HTML file to customize:
- Title: Change in `<title>` tag
- Header: Modify the chat header text
- Colors: Update CSS custom properties
- Logo: Replace the robot emoji with your logo

### API Configuration
Modify the JavaScript configuration:
```javascript
this.modelName = 'gemini-2.5-flash'; // Change model
this.apiKey = 'your-api-key'; // Set default key
```

## 🔒 Security Notes

- API keys are stored locally in your browser
- No data is sent to external servers except the Gemini API
- Consider the privacy implications when sharing the interface publicly

## 🛠️ Technical Details

- **Framework**: Vanilla JavaScript (no dependencies)
- **API**: Google Gemini 2.5 Flash
- **Storage**: Browser localStorage for settings
- **Audio**: Web Speech API for voice features
- **Responsive**: CSS Grid and Flexbox

## 📋 Requirements

- Modern web browser (Chrome, Firefox, Safari, Edge)
- Internet connection for API calls
- Microphone access for voice features (optional)
- Valid Gemini API key

## 🚨 Troubleshooting

### Common Issues:
1. **"API key not found"**: Enter a valid Gemini API key
2. **"Network error"**: Check your internet connection
3. **"Voice not working"**: Allow microphone permissions
4. **"Theme not saving"**: Enable localStorage in your browser

### Browser Compatibility:
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

## 📝 License

This project is designed for educational and demonstration purposes. Ensure compliance with Google's Gemini API terms of service when using publicly.

---

**Ready to chat?** Just open `chatbot_web.html` in your browser and start your AI conversation! 🤖✨