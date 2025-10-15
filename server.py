#!/usr/bin/env python3
"""
Simple HTTP Server for ROSSI 46 Chatbot
Serves the chatbot interface for public access
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

class ChatbotHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(Path(__file__).parent), **kwargs)

    def end_headers(self):
        # Add security headers
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'DENY')
        self.send_header('X-XSS-Protection', '1; mode=block')
        super().end_headers()

    def log_message(self, format, *args):
        # Custom log format
        print(f"[{self.log_date_time_string()}] {format % args}")

def main():
    # Configuration
    PORT = 8000
    HOST = '0.0.0.0'  # Listen on all interfaces for public access

    # Change to the directory containing the chatbot files
    os.chdir(Path(__file__).parent)

    # Create server with address reuse
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer((HOST, PORT), ChatbotHTTPRequestHandler) as httpd:
        print("ROSSI 46 Chatbot Server Starting...")
        print(f"Server running at: http://localhost:{PORT}")
        print(f"Public access: http://YOUR_IP:{PORT}")
        print(f"Chatbot interface: http://localhost:{PORT}/chatbot_web.html")
        print("Available files:")

        # List available files
        for file in sorted(Path('.').glob('*')):
            if file.is_file() and not file.name.startswith('.'):
                print(f"   - http://localhost:{PORT}/{file.name}")

        print("\nTips:")
        print("   - Open http://localhost:8000/chatbot_web.html in your browser")
        print("   - Share your public IP with others for remote access")
        print("   - Press Ctrl+C to stop the server")
        print("\n" + "="*50)

        try:
            # Automatically open browser
            webbrowser.open(f'http://localhost:{PORT}/chatbot_web.html')
            print("Opening chatbot in default browser...")

            # Start serving
            httpd.serve_forever()

        except KeyboardInterrupt:
            print("\nServer stopped by user")
        except Exception as e:
            print(f"\nError starting server: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()