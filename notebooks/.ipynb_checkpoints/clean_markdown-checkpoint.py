#!/usr/bin/env python3
"""
Clean markdown files for LaTeX conversion
"""

import re

def clean_markdown_file(input_file, output_file):
    """Clean a markdown file for LaTeX conversion"""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove emojis and special characters
    content = re.sub(r'[🎯📊🔍💡📈📋🚀🧠🏭🔬]', '', content)
    
    # Fix R² symbols
    content = content.replace('R²', 'R^2')
    
    # Fix underscores in dataset names
    content = re.sub(r'([a-zA-Z])_([a-zA-Z])', r'\1 \2', content)
    
    # Remove any remaining problematic characters
    content = re.sub(r'[^\x00-\x7F]+', '', content)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Cleaned {input_file} -> {output_file}")

if __name__ == "__main__":
    # Clean all three markdown files
    clean_markdown_file('EXECUTIVE_SUMMARY.md', 'EXECUTIVE_SUMMARY_clean.md')
    clean_markdown_file('COMPREHENSIVE_RESEARCH_REPORT.md', 'COMPREHENSIVE_RESEARCH_REPORT_clean.md')
    clean_markdown_file('TECHNICAL_APPENDIX.md', 'TECHNICAL_APPENDIX_clean.md')
