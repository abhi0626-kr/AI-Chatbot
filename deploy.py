#!/usr/bin/env python3
"""
Automated Deployment Script for ROSSI 46 Chatbot
Makes the chatbot publicly accessible with one command
"""

import os
import sys
import time
import webbrowser
import http.server
import socketserver
import subprocess
from pathlib import Path

# Fix Unicode encoding for Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.detach())

class ChatbotDeployer:
    def __init__(self):
        self.project_dir = Path(__file__).parent
        self.files_to_deploy = [
            'chatbot_web.html',
            'index.html',
            'README_WEB.md',
            'server.py'
        ]

    def check_requirements(self):
        """Check if all required files exist"""
        print("🔍 Checking requirements...")
        missing_files = []

        for file in self.files_to_deploy:
            if not (self.project_dir / file).exists():
                missing_files.append(file)

        if missing_files:
            print(f"❌ Missing files: {', '.join(missing_files)}")
            return False

        print("✅ All required files found!")
        return True

    def start_local_server(self):
        """Start local server for testing"""
        print("\n🚀 Starting local server...")
        print("=" * 50)

        try:
            # Change to project directory
            os.chdir(self.project_dir)

            # Start server in background
            server_process = subprocess.Popen([
                sys.executable, 'server.py'
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Wait a moment for server to start
            time.sleep(2)

            # Check if server is running
            if server_process.poll() is None:
                print("✅ Local server started successfully!")
                print("🌐 Access your chatbot at: http://localhost:8000")
                print("🤖 Main interface: http://localhost:8000/chatbot_web.html")
                print("📄 Landing page: http://localhost:8000/index.html")
                print("\n📋 Available files:")
                for file in self.files_to_deploy:
                    print(f"   • http://localhost:8000/{file}")

                print("\n💡 Press Ctrl+C to stop the server")
                print("=" * 50)

                # Open browser automatically
                try:
                    webbrowser.open('http://localhost:8000/chatbot_web.html')
                    print("🌐 Opening chatbot in default browser...")
                except Exception as e:
                    print(f"⚠️  Could not open browser automatically: {e}")

                return True
            else:
                print("❌ Failed to start server")
                return False

        except Exception as e:
            print(f"❌ Error starting server: {e}")
            return False

    def create_deployment_package(self):
        """Create a zip file for easy deployment"""
        print("\n📦 Creating deployment package...")

        try:
            import zipfile

            zip_name = "rossi46_chatbot_deployment.zip"
            zip_path = self.project_dir / zip_name

            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for file in self.files_to_deploy:
                    if (self.project_dir / file).exists():
                        zipf.write(self.project_dir / file, file)
                        print(f"   📄 Added: {file}")

            print(f"✅ Deployment package created: {zip_name}")
            print(f"📂 Size: {(zip_path.stat().st_size / 1024 / 1024):.2f} MB")
            return zip_name

        except Exception as e:
            print(f"❌ Error creating deployment package: {e}")
            return None

    def show_hosting_options(self):
        """Show different hosting options"""
        print("\n🌍 HOSTING OPTIONS FOR PUBLIC ACCESS:")
        print("=" * 50)

        options = [
            {
                "name": "GitHub Pages (FREE)",
                "steps": [
                    "1. Create a GitHub repository",
                    "2. Upload chatbot_web.html and index.html",
                    "3. Go to Settings > Pages",
                    "4. Select 'Deploy from a branch'",
                    "5. Your site will be at: https://username.github.io/repo-name/"
                ],
                "url": "https://pages.github.com/"
            },
            {
                "name": "Netlify (FREE)",
                "steps": [
                    "1. Go to netlify.com",
                    "2. Drag & drop the files or connect to Git",
                    "3. Deploy automatically",
                    "4. Get a public URL like: https://amazing-site-name.netlify.app"
                ],
                "url": "https://netlify.com"
            },
            {
                "name": "Vercel (FREE)",
                "steps": [
                    "1. Go to vercel.com",
                    "2. Connect your GitHub/GitLab account",
                    "3. Import your project",
                    "4. Deploy with one click",
                    "5. Get instant HTTPS URL"
                ],
                "url": "https://vercel.com"
            },
            {
                "name": "Firebase Hosting (FREE)",
                "steps": [
                    "1. Install Firebase CLI: npm install -g firebase-tools",
                    "2. Login: firebase login",
                    "3. Initialize: firebase init hosting",
                    "4. Deploy: firebase deploy",
                    "5. Get your public URL"
                ],
                "url": "https://firebase.google.com/docs/hosting"
            },
            {
                "name": "Local Server (Development)",
                "steps": [
                    "1. Run: python server.py",
                    "2. Find your IP address",
                    "3. Share: http://YOUR_IP:8000/chatbot_web.html",
                    "4. Others can access from same network"
                ],
                "url": "Local network only"
            }
        ]

        for i, option in enumerate(options, 1):
            print(f"\n{i}. {option['name']}")
            print(f"   🔗 {option['url']}")
            print("   Steps:")
            for step in option['steps']:
                print(f"   {step}")

        print("\n" + "=" * 50)

    def show_seo_tips(self):
        """Show SEO optimization tips"""
        print("\n🔍 SEO TIPS FOR BETTER SEARCH VISIBILITY:")
        print("=" * 50)

        tips = [
            "✅ Use descriptive titles and descriptions",
            "✅ Add relevant keywords: 'AI chatbot', 'ROSSI 46', 'free AI'",
            "✅ Share on social media for backlinks",
            "✅ Submit to search engines manually",
            "✅ Create a custom domain name",
            "✅ Add meta tags for social sharing",
            "✅ Write a blog post about your chatbot",
            "✅ Share in AI and tech communities"
        ]

        for tip in tips:
            print(f"   {tip}")

        print("\n💡 Search terms that will find your chatbot:")
        print("   • 'ROSSI 46 chatbot'")
        print("   • 'ROSSI 46 AI'")
        print("   • 'free AI chatbot'")
        print("   • 'online AI assistant'")
        print("   • 'Gemini chatbot interface'")

    def run_deployment_wizard(self):
        """Run interactive deployment wizard"""
        print("\n🤖 ROSSI 46 CHATBOT DEPLOYMENT WIZARD")
        print("=" * 50)

        if not self.check_requirements():
            return

        print("\nChoose deployment option:")
        print("1. 🚀 Start Local Server (for testing)")
        print("2. 📦 Create Deployment Package")
        print("3. 🌍 Show Hosting Options")
        print("4. 🔍 Show SEO Tips")
        print("5. 📋 Show All Options")

        try:
            choice = input("\nEnter your choice (1-5): ").strip()

            if choice == '1':
                self.start_local_server()
            elif choice == '2':
                self.create_deployment_package()
                print("\n✅ Deployment package created!")
                print("📤 Upload the .zip file to any hosting service")
            elif choice == '3':
                self.show_hosting_options()
            elif choice == '4':
                self.show_seo_tips()
            elif choice == '5':
                self.start_local_server()
                self.create_deployment_package()
                self.show_hosting_options()
                self.show_seo_tips()
            else:
                print("❌ Invalid choice")

        except KeyboardInterrupt:
            print("\n👋 Deployment wizard cancelled")
        except Exception as e:
            print(f"❌ Error in deployment wizard: {e}")

def main():
    """Main deployment function"""
    print("🚀 ROSSI 46 CHATBOT AUTOMATED DEPLOYMENT")
    print("=" * 50)

    deployer = ChatbotDeployer()
    deployer.run_deployment_wizard()

if __name__ == "__main__":
    main()