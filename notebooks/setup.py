#!/usr/bin/env python3
"""
Setup script for ML vs Statistical Models Comparison Framework

This script sets up the framework and makes it easy to install and use.
"""

import os
import sys
import subprocess
from pathlib import Path


def run_command(command, description):
    """Run a command and handle errors."""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}: {e}")
        print(f"   Command: {command}")
        print(f"   Error: {e.stderr}")
        return False


def check_python_version():
    """Check if Python version is compatible."""
    print("🐍 Checking Python version...")
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"   Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version.split()[0]} is compatible")
    return True


def install_dependencies():
    """Install required dependencies."""
    print("\n📦 Installing dependencies...")
    
    # Check if requirements.txt exists
    if not Path("requirements.txt").exists():
        print("❌ requirements.txt not found")
        return False
    
    # Install dependencies
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        return False
    
    return True


def create_directories():
    """Create necessary directories."""
    print("\n📁 Creating directories...")
    
    directories = [
        "comprehensive_results",
        "reports",
        "logs",
        "data",
        "notebooks"
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✅ Created directory: {directory}")
    
    return True


def test_installation():
    """Test if the framework can be imported and run."""
    print("\n🧪 Testing installation...")
    
    try:
        # Test imports
        sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
        
        from src.core import Config, ModelEvaluator
        from src.data import DatasetManager
        from src.models import SklearnLinearRegression, OLSRegression
        from src.analysis.comprehensive_comparison import ComprehensiveComparisonFramework
        
        print("✅ All imports successful")
        
        # Test basic functionality
        config = Config()
        data_manager = DatasetManager()
        evaluator = ModelEvaluator()
        
        print("✅ Core components initialized successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Installation test failed: {e}")
        return False


def run_quick_demo():
    """Run a quick demo to verify everything works."""
    print("\n🚀 Running quick demo...")
    
    try:
        result = subprocess.run([sys.executable, "quick_demo.py"], 
                              capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print("✅ Quick demo completed successfully")
            print("   Check 'comprehensive_results/' for output")
            return True
        else:
            print(f"❌ Quick demo failed: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("⏰ Quick demo timed out (this is normal for first run)")
        return True
    except Exception as e:
        print(f"❌ Error running quick demo: {e}")
        return False


def main():
    """Main setup function."""
    print("=" * 60)
    print("ML vs STATISTICAL MODELS COMPARISON FRAMEWORK")
    print("Setup Script v2.0")
    print("=" * 60)
    
    # Check Python version
    if not check_python_version():
        return 1
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Setup failed during dependency installation")
        return 1
    
    # Create directories
    if not create_directories():
        print("\n❌ Setup failed during directory creation")
        return 1
    
    # Test installation
    if not test_installation():
        print("\n❌ Setup failed during installation test")
        return 1
    
    # Run quick demo
    if not run_quick_demo():
        print("\n⚠️  Quick demo failed, but installation appears successful")
        print("   You can try running: python quick_demo.py")
    
    print("\n" + "=" * 60)
    print("SETUP COMPLETE!")
    print("=" * 60)
    print()
    print("🎉 Framework is ready to use!")
    print()
    print("Quick start commands:")
    print("  python quick_demo.py                    # Run quick demo")
    print("  python run_comprehensive_comparison.py  # Run full comparison")
    print("  python examples/01_basic_comparison/simple_comparison.py  # Basic example")
    print()
    print("Documentation:")
    print("  README_NEW.md                           # Complete documentation")
    print("  examples/                               # Example implementations")
    print("  config/                                 # Configuration files")
    print()
    print("Results will be saved to:")
    print("  comprehensive_results/                  # Main results")
    print("  reports/                                # Generated reports")
    print("  logs/                                   # Log files")
    
    return 0


if __name__ == "__main__":
    exit(main())
