#!/usr/bin/env python3
"""
Create a comprehensive PDF from all three markdown files
"""

import re
import os

def clean_markdown_for_latex(text):
    """Clean markdown text for LaTeX conversion"""
    
    # Remove emojis and special characters
    text = re.sub(r'[🎯📊🔍💡📈📋🚀🧠🏭🔬]', '', text)
    
    # Convert headers
    text = re.sub(r'^# (.+)$', r'\\section{\1}', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'\\subsection{\1}', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.+)$', r'\\subsubsection{\1}', text, flags=re.MULTILINE)
    text = re.sub(r'^#### (.+)$', r'\\paragraph{\1}', text, flags=re.MULTILINE)
    
    # Close headers properly
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('\\section{') or line.startswith('\\subsection{') or line.startswith('\\subsubsection{') or line.startswith('\\paragraph{'):
            if i + 1 < len(lines) and not lines[i + 1].startswith('\\') and lines[i + 1].strip() != '':
                lines[i] += '}'
    text = '\n'.join(lines)
    
    # Convert bold text
    text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', text)
    
    # Convert italic text
    text = re.sub(r'\*(.+?)\*', r'\\textit{\1}', text)
    
    # Convert code blocks
    text = re.sub(r'```(.+?)```', r'\\begin{verbatim}\1\\end{verbatim}', text, flags=re.DOTALL)
    
    # Convert inline code
    text = re.sub(r'`(.+?)`', r'\\texttt{\1}', text)
    
    # Convert lists
    text = re.sub(r'^- (.+)$', r'\\item \1', text, flags=re.MULTILINE)
    
    # Convert tables (basic)
    lines = text.split('\n')
    in_table = False
    table_lines = []
    table_start = 0
    
    for i, line in enumerate(lines):
        if '|' in line and not line.strip().startswith('|') and not line.strip().endswith('|'):
            # Start of table
            in_table = True
            table_lines = [line]
            table_start = i
        elif in_table and '|' in line:
            # Table row
            table_lines.append(line)
        elif in_table and '|' not in line and line.strip() != '':
            # End of table
            if table_lines:
                # Convert table to LaTeX
                latex_table = convert_table_to_latex(table_lines)
                lines[table_start:i] = [latex_table]
                # Adjust remaining indices
                i = table_start + 1
            in_table = False
            table_lines = []
    
    text = '\n'.join(lines)
    
    # Escape special LaTeX characters
    text = text.replace('&', '\\&')
    text = text.replace('%', '\\%')
    text = text.replace('$', '\\$')
    text = text.replace('#', '\\#')
    text = text.replace('^', '\\textasciicircum{}')
    text = text.replace('_', '\\_')
    text = text.replace('{', '\\{')
    text = text.replace('}', '\\}')
    text = text.replace('~', '\\textasciitilde{}')
    text = text.replace('\\', '\\textbackslash{}')
    
    # Fix R² symbols
    text = text.replace('R²', 'R$^2$')
    
    # Fix underscores in dataset names
    text = re.sub(r'([a-zA-Z])_([a-zA-Z])', r'\1 \2', text)
    
    return text

def convert_table_to_latex(table_lines):
    """Convert markdown table to LaTeX table"""
    
    if not table_lines:
        return ""
    
    # Remove empty lines
    table_lines = [line for line in table_lines if line.strip()]
    
    if len(table_lines) < 2:
        return ""
    
    # Split first line to get headers
    headers = [cell.strip() for cell in table_lines[0].split('|') if cell.strip()]
    
    # Create LaTeX table
    latex_table = "\\begin{table}[h!]\n\\centering\n\\begin{tabular}{" + "c" * len(headers) + "}\n\\toprule\n"
    
    # Add headers
    latex_table += " & ".join(headers) + " \\\\\n\\midrule\n"
    
    # Add data rows
    for line in table_lines[1:]:
        if '|' in line:
            cells = [cell.strip() for cell in line.split('|') if cell.strip()]
            if len(cells) == len(headers):
                latex_table += " & ".join(cells) + " \\\\\n"
    
    latex_table += "\\bottomrule\n\\end{tabular}\n\\caption{Performance Results}\n\\end{table}\n"
    
    return latex_table

def create_comprehensive_pdf():
    """Create a comprehensive PDF from all three markdown files"""
    
    # Read all markdown files
    with open('COMPREHENSIVE_RESEARCH_REPORT.md', 'r', encoding='utf-8') as f:
        comprehensive_report = f.read()
    
    with open('EXECUTIVE_SUMMARY.md', 'r', encoding='utf-8') as f:
        executive_summary = f.read()
    
    with open('TECHNICAL_APPENDIX.md', 'r', encoding='utf-8') as f:
        technical_appendix = f.read()
    
    # Clean and convert to LaTeX
    comprehensive_latex = clean_markdown_for_latex(comprehensive_report)
    executive_latex = clean_markdown_for_latex(executive_summary)
    technical_latex = clean_markdown_for_latex(technical_appendix)
    
    # Create comprehensive LaTeX document
    latex_content = f"""
\\documentclass[11pt,a4paper]{{article}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[T1]{{fontenc}}
\\usepackage{{amsmath}}
\\usepackage{{amsfonts}}
\\usepackage{{amssymb}}
\\usepackage{{graphicx}}
\\usepackage{{booktabs}}
\\usepackage{{longtable}}
\\usepackage{{array}}
\\usepackage{{multirow}}
\\usepackage{{wrapfig}}
\\usepackage{{float}}
\\usepackage{{colortbl}}
\\usepackage{{pdflscape}}
\\usepackage{{tabu}}
\\usepackage{{threeparttable}}
\\usepackage{{threeparttablex}}
\\usepackage{{makecell}}
\\usepackage{{xcolor}}
\\usepackage{{geometry}}
\\usepackage{{enumitem}}
\\usepackage{{hyperref}}
\\usepackage{{fancyhdr}}
\\usepackage{{titlesec}}

\\geometry{{margin=1in}}

\\pagestyle{{fancy}}
\\fancyhf{{}}
\\fancyhead[LE,RO]{{\\thepage}}
\\fancyhead[LO,RE]{{\\leftmark}}

\\title{{A Comprehensive Comparative Analysis of Machine Learning and Statistical Models}}
\\author{{ML vs Statistical Models Research Team}}
\\date{{\\today}}

\\begin{{document}}

\\maketitle

\\tableofcontents
\\newpage

\\section{{Executive Summary}}
{executive_latex}

\\newpage
\\section{{Comprehensive Research Report}}
{comprehensive_latex}

\\newpage
\\section{{Technical Appendix}}
{technical_latex}

\\end{{document}}
"""
    
    # Write LaTeX file
    with open('comprehensive_full_report.tex', 'w', encoding='utf-8') as f:
        f.write(latex_content)
    
    print("Comprehensive LaTeX document created: comprehensive_full_report.tex")

if __name__ == "__main__":
    create_comprehensive_pdf()
