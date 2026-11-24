"""Script to generate the complete final university assignment report HTML and PDF.

Target PDF: Case37_37_Likhith_Gowda_M_S.pdf
Student: Likhith Gowda M S (ENG24CS0105 / Roll 37 / Section 5B)
Institution: Dayananda Sagar University, Bengaluru
"""

import base64
import os
import subprocess
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
OUTPUT_PDF = os.path.join(BASE_DIR, "Case37_37_Likhith_Gowda_M_S.pdf")

os.makedirs(REPORTS_DIR, exist_ok=True)


def get_image_base64(filename):
    path = os.path.join(SCREENSHOTS_DIR, filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded}"
    return ""


def read_file_safe(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return ""


def md_to_html_simple(md_text):
    """Convert markdown elements into clean print-ready HTML."""
    lines = md_text.split("\n")
    html_lines = []
    in_table = False
    in_code = False
    code_block = []

    for line in lines:
        stripped = line.strip()

        # Code block handling
        if stripped.startswith("```"):
            if in_code:
                in_code = False
                html_lines.append(f"<pre><code>{''.join(code_block)}</code></pre>")
                code_block = []
            else:
                in_code = True
            continue
        if in_code:
            code_block.append(line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;") + "\n")
            continue

        # Table handling
        if stripped.startswith("|") and stripped.endswith("|"):
            if "---" in stripped:
                continue
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if not in_table:
                in_table = True
                html_lines.append('<div class="table-responsive"><table class="report-table">')
                html_lines.append("<thead><tr>" + "".join(f"<th>{c}</th>" for c in cells) + "</tr></thead><tbody>")
            else:
                html_lines.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
            continue
        elif in_table:
            in_table = False
            html_lines.append("</tbody></table></div>")

        if not stripped:
            html_lines.append("<br>")
            continue

        # Headers
        if stripped.startswith("# "):
            html_lines.append(f'<h1 class="report-h1">{stripped[2:]}</h1>')
        elif stripped.startswith("## "):
            html_lines.append(f'<h2 class="report-h2">{stripped[3:]}</h2>')
        elif stripped.startswith("### "):
            html_lines.append(f'<h3 class="report-h3">{stripped[4:]}</h3>')
        elif stripped.startswith("#### "):
            html_lines.append(f'<h4 class="report-h4">{stripped[5:]}</h4>')
        elif stripped.startswith("- "):
            html_lines.append(f'<li class="report-li">{stripped[2:]}</li>')
        elif stripped.startswith("---"):
            html_lines.append('<hr class="report-hr">')
        else:
            # Inline bold and code
            processed = stripped
            # Bold
            import re
            processed = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", processed)
            processed = re.sub(r"`(.*?)`", r"<code>\1</code>", processed)
            html_lines.append(f"<p>{processed}</p>")

    if in_table:
        html_lines.append("</tbody></table></div>")
    if in_code:
        html_lines.append(f"<pre><code>{''.join(code_block)}</code></pre>")

    return "\n".join(html_lines)


def build_full_report_html():
    img_sdlc = get_image_base64("incremental_sdlc.png")
    img_kanban = get_image_base64("kanban.png")
    img_burndown = get_image_base64("burndown.png")
    img_cat = get_image_base64("01_catalog_home.png")
    img_cart = get_image_base64("02_cart_out_of_stock.png")
    img_sub = get_image_base64("03_substitution_engine.png")
    img_checkout = get_image_base64("04_checkout_slot_selection.png")
    img_confirm = get_image_base64("05_order_confirmation.png")
    img_health = get_image_base64("06_health_check_json.png")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Case37_37_Likhith_Gowda_M_S - University Practical Lab Record</title>
<style>
@page {{
    size: A4 portrait;
    margin: 20mm 15mm 20mm 15mm;
    @bottom-right {{
        content: counter(page);
    }}
}}
body {{
    font-family: "Segoe UI", -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
    color: #1a1a1a;
    line-height: 1.5;
    font-size: 10.5pt;
    background: #fff;
    margin: 0;
    padding: 0;
}}
.page-break {{
    page-break-before: always;
}}
.cover-page {{
    text-align: center;
    padding: 40px 20px;
    height: 90vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}}
.univ-header {{
    font-size: 19pt;
    font-weight: 800;
    color: #0b5394;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 4px;
}}
.dept-header {{
    font-size: 13pt;
    font-weight: 600;
    color: #333;
    margin-bottom: 25px;
}}
.record-title {{
    font-size: 20pt;
    font-weight: 800;
    color: #198754;
    text-transform: uppercase;
    margin: 20px 0 10px 0;
    border-top: 3px solid #198754;
    border-bottom: 3px solid #198754;
    padding: 12px 0;
}}
.case-badge {{
    display: inline-block;
    background: #212529;
    color: #ffc107;
    font-weight: bold;
    font-size: 13pt;
    padding: 6px 16px;
    border-radius: 4px;
    margin-bottom: 20px;
}}
.details-table {{
    width: 90%;
    margin: 25px auto;
    border-collapse: collapse;
    text-align: left;
}}
.details-table td {{
    padding: 8px 14px;
    border: 1px solid #ced4da;
    font-size: 11pt;
}}
.details-table td.label {{
    font-weight: bold;
    background: #f8f9fa;
    width: 38%;
}}
.report-h1 {{
    font-size: 16pt;
    font-weight: 800;
    color: #0b5394;
    border-bottom: 2px solid #0b5394;
    padding-bottom: 6px;
    margin-top: 25px;
    margin-bottom: 15px;
    page-break-after: avoid;
}}
.report-h2 {{
    font-size: 13pt;
    font-weight: 700;
    color: #198754;
    margin-top: 20px;
    margin-bottom: 10px;
    page-break-after: avoid;
}}
.report-h3 {{
    font-size: 11pt;
    font-weight: 700;
    color: #333;
    margin-top: 15px;
    margin-bottom: 6px;
    page-break-after: avoid;
}}
.report-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 14px 0;
    font-size: 9.5pt;
}}
.report-table th, .report-table td {{
    border: 1px solid #dee2e6;
    padding: 6px 8px;
    text-align: left;
}}
.report-table th {{
    background-color: #f1f3f5;
    font-weight: 700;
    color: #212529;
}}
.report-table tr:nth-child(even) {{
    background-color: #fafbfc;
}}
pre {{
    background-color: #f8f9fa;
    border: 1px solid #e9ecef;
    border-left: 4px solid #198754;
    padding: 8px 12px;
    font-family: Consolas, monospace;
    font-size: 8.5pt;
    overflow-x: auto;
    white-space: pre-wrap;
    word-wrap: break-word;
    margin: 10px 0;
}}
code {{
    font-family: Consolas, monospace;
    background: #eef2f5;
    padding: 1px 4px;
    border-radius: 3px;
    font-size: 9pt;
}}
.figure-container {{
    text-align: center;
    margin: 16px 0;
    page-break-inside: avoid;
}}
.figure-img {{
    max-width: 90%;
    height: auto;
    border: 1px solid #dee2e6;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}}
.figure-caption {{
    font-size: 9pt;
    color: #666;
    font-style: italic;
    margin-top: 6px;
}}
.badge {{
    display: inline-block;
    padding: 2px 6px;
    font-size: 8.5pt;
    font-weight: bold;
    border-radius: 3px;
}}
.badge-pass {{ background: #d1e7dd; color: #0f5132; }}
.badge-fail {{ background: #f8d7da; color: #842029; }}
</style>
</head>
<body>

<!-- ========================================== -->
<!-- 1. COVER PAGE                             -->
<!-- ========================================== -->
<div class="cover-page">
    <div>
        <div class="univ-header">Dayananda Sagar University</div>
        <div class="dept-header">School of Engineering • Department of Computer Science & Engineering<br>Bengaluru, Karnataka - 560078</div>
        <div class="case-badge">CASE STUDY 37 • ACADEMIC PRACTICAL RECORD</div>
        <div class="record-title">AI IN SOFTWARE ENGINEERING<br>LABORATORY PROJECT REPORT</div>
        <p style="font-size: 13pt; font-weight: 600; color: #495057; margin-top: 15px;">Project: Online Grocery Ordering and Slot-Based Delivery with Substitution Logic</p>
    </div>

    <div>
        <table class="details-table">
            <tr><td class="label">Student Name</td><td><strong>Likhith Gowda M S</strong></td></tr>
            <tr><td class="label">University Seat Number (USN)</td><td><strong>ENG24CS0105</strong></td></tr>
            <tr><td class="label">Roll / Case Number</td><td><strong>37</strong></td></tr>
            <tr><td class="label">Academic Semester & Section</td><td><strong>5th Semester • Section 5B</strong></td></tr>
            <tr><td class="label">Degree & Department</td><td>B.Tech in Computer Science and Engineering</td></tr>
            <tr><td class="label">Software Process Model Assigned</td><td><strong>Incremental Lifecycle Model</strong></td></tr>
            <tr><td class="label">Agile Methodology Assigned</td><td><strong>Kanban Framework (WIP Limits)</strong></td></tr>
            <tr><td class="label">Primary Prototype Module</td><td><strong>Intelligent Product Substitution Logic</strong></td></tr>
            <tr><td class="label">Required AI Tool Specified</td><td><strong>ChatGPT (OpenAI GPT-4o)</strong></td></tr>
            <tr><td class="label">Verified Code Coverage</td><td><strong>85.0% (PyTest 21/21 Passing)</strong></td></tr>
            <tr><td class="label">GitHub Repository Link</td><td><a href="https://github.com/LikhithGowdaMS/Case37-Online-Grocery">https://github.com/LikhithGowdaMS/Case37-Online-Grocery</a></td></tr>
        </table>
    </div>

    <div style="margin-top: 20px; font-size: 10pt; color: #6c757d;">
        Submitted in partial fulfillment of the course requirements for<br>
        <strong>24CS501: AI in Software Engineering</strong> • November 2026
    </div>
</div>

<div class="page-break"></div>

<!-- ========================================== -->
<!-- 2. PART 1: CASE TASKS A TO E               -->
<!-- ========================================== -->
<h1 class="report-h1">Part 1: Case Tasks A to E (Case 37 — Online Grocery)</h1>
"""

    # Add Case Tasks
    for task_name in ["Task_A_Incremental_Lifecycle.md", "Task_B_Kanban_Order_Picking.md", "Task_C_Substitution_Logic_DevOps.md", "Task_D_Testing_Defect_Prediction.md", "Task_E_Quality_Ethics_Pricing.md"]:
        path = os.path.join(BASE_DIR, "case_tasks", task_name)
        text = read_file_safe(path)
        html += f'<div class="task-section">{md_to_html_simple(text)}</div>'
        if "Task_A" in task_name and img_sdlc:
            html += f'<div class="figure-container"><img class="figure-img" src="{img_sdlc}"><div class="figure-caption">Figure A.1: Incremental SDLC Process Model for FreshCart Grocery</div></div>'
        elif "Task_B" in task_name and img_kanban:
            html += f'<div class="figure-container"><img class="figure-img" src="{img_kanban}"><div class="figure-caption">Figure B.1: Kanban Board with WIP Limits for Order Picking & Substitution</div></div>'
            if img_burndown:
                html += f'<div class="figure-container"><img class="figure-img" src="{img_burndown}"><div class="figure-caption">Figure B.2: Sprint Burndown Progress Chart</div></div>'
        html += '<div class="page-break"></div>'

    # Add Visual Application Gallery
    html += """<h1 class="report-h1">Visual Execution Evidence — FreshCart Online Grocery Web Application</h1>
    <p>The following real application screenshots were captured using headless Google Chrome 131 against the locally executed Flask application running on port 5000 with persistent SQLite database storage:</p>
    """
    gallery = [
        ("01_catalog_home.png", "Figure V.1: FreshCart Grocery Product Catalogue (Dairy, Staples, Produce, Bakery)"),
        ("02_cart_out_of_stock.png", "Figure V.2: Shopping Cart detecting Out-of-Stock Item (Amul Taaza Milk) and Prompting Substitution"),
        ("03_substitution_engine.png", "Figure V.3: Intelligent Substitution Review: Side-by-Side Comparison with Accept/Reject Decisioning"),
        ("04_checkout_slot_selection.png", "Figure V.4: Guaranteed Delivery Slot Selection with Capacity Enforcement (Evening Slot Full)"),
        ("05_order_confirmation.png", "Figure V.5: Verified Order Confirmation with Persistent Code and Substituted Item Breakdown"),
        ("06_health_check_json.png", "Figure V.6: Live Site Reliability Monitoring Healthcheck Probe Endpoint (/health)"),
    ]
    for img_file, cap in gallery:
        b64 = get_image_base64(img_file)
        if b64:
            html += f'<div class="figure-container"><img class="figure-img" src="{b64}"><div class="figure-caption">{cap}</div></div><br>'

    html += '<div class="page-break"></div>'

    # Add Part 2: Theory Questions T1.1 to T5.5
    html += '<h1 class="report-h1">Part 2: Theory Questions T1.1 to T5.5 (All 25 Questions)</h1>'
    for mod in ["Module_1_Theory.md", "Module_2_Theory.md", "Module_3_Theory.md", "Module_4_Theory.md", "Module_5_Theory.md"]:
        path = os.path.join(BASE_DIR, "theory_answers", mod)
        text = read_file_safe(path)
        html += f'<div class="theory-mod">{md_to_html_simple(text)}</div><div class="page-break"></div>'

    # Add Part 3: Lab Experiments L1.1 to L5.5
    html += '<h1 class="report-h1">Part 3: Practical Lab Experiments L1.1 to L5.5 (All 25 Experiments)</h1>'
    exp_folders = [
        "Module-1-SDLC/L1.1", "Module-1-SDLC/L1.2", "Module-1-SDLC/L1.3", "Module-1-SDLC/L1.4", "Module-1-SDLC/L1.5",
        "Module-2-Agile/L2.1", "Module-2-Agile/L2.2", "Module-2-Agile/L2.3", "Module-2-Agile/L2.4", "Module-2-Agile/L2.5",
        "Module-3-Development/L3.1", "Module-3-Development/L3.2", "Module-3-Development/L3.3", "Module-3-Development/L3.4", "Module-3-Development/L3.5",
        "Module-4-Testing/L4.1", "Module-4-Testing/L4.2", "Module-4-Testing/L4.3", "Module-4-Testing/L4.4", "Module-4-Testing/L4.5",
        "Module-5-Quality-Assurance/L5.1", "Module-5-Quality-Assurance/L5.2", "Module-5-Quality-Assurance/L5.3", "Module-5-Quality-Assurance/L5.4", "Module-5-Quality-Assurance/L5.5",
    ]
    for exp in exp_folders:
        path = os.path.join(BASE_DIR, exp, "README.md")
        text = read_file_safe(path)
        html += f'<div class="experiment-block">{md_to_html_simple(text)}</div><hr class="report-hr">'

    html += '<div class="page-break"></div>'

    # Add Appendix A: AI Usage Log
    html += '<div class="appendix-section">' + md_to_html_simple(read_file_safe(os.path.join(BASE_DIR, "AI_Usage_Log.md"))) + '</div><div class="page-break"></div>'

    # Add Appendix B: AI Disclosure
    html += '<div class="appendix-section">' + md_to_html_simple(read_file_safe(os.path.join(BASE_DIR, "AI_Disclosure.md"))) + '</div><div class="page-break"></div>'

    # Add Appendix C: Master Checklist
    html += '<div class="appendix-section">' + md_to_html_simple(read_file_safe(os.path.join(BASE_DIR, "ASSIGNMENT_CHECKLIST.md"))) + '</div>'

    html += """
</body>
</html>"""

    html_path = os.path.join(REPORTS_DIR, "final_report.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated comprehensive report HTML: {html_path} ({os.path.getsize(html_path):,} bytes)")
    return html_path


def render_pdf(html_path):
    print(f"Rendering PDF report via Headless Chrome: {OUTPUT_PDF}...")
    cmd = [
        CHROME_PATH,
        "--headless=new",
        "--no-sandbox",
        "--disable-gpu",
        "--disable-dev-shm-usage",
        "--no-pdf-header-footer",
        f"--print-to-pdf={OUTPUT_PDF}",
        html_path,
    ]
    subprocess.run(cmd, check=True)
    if os.path.exists(OUTPUT_PDF):
        size_kb = os.path.getsize(OUTPUT_PDF) / 1024
        print(f"SUCCESS: Final PDF generated successfully at {OUTPUT_PDF} ({size_kb:.1f} KB)")
        return True
    return False


if __name__ == "__main__":
    html_file = build_full_report_html()
    success = render_pdf(html_file)
    print("PDF Generation:", "SUCCESS" if success else "FAILED")
