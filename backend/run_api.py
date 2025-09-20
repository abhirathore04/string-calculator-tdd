"""
Run script for String Calculator API Server
"""
import sys
import os

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

if __name__ == '__main__':
    # Import and run the Flask app
    from api import app
    
    print("🚀 Starting String Calculator API Server...")
    print("📍 Server running at: http://localhost:5000")
    print("🏥 Health check: http://localhost:5000/api/health")
    print("📚 API docs: http://localhost:5000/")
    print("🔗 Frontend should run at: http://localhost:3000")
    print("\n🧮 String Calculator API is ready!")
    print("Press Ctrl+C to stop the server")
    print("-" * 50)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
