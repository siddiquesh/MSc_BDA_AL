import os
import json

root = r'c:\Users\asdf\Downloads\MSc_BDA_AL-'
asm_dir = os.path.join(root, 'asm')

practicals = [
    {
        "id": "asm1",
        "title": "Practical 1",
        "topic": "Descriptive Statistics",
        "desc": "Mean, median, mode, std dev, variance, skewness, kurtosis & distributions for Iris, Tips, and Stock datasets.",
        "curl_da": "da.gd/s_asm1",
        "curl_is": "is.gd/sidasm1"
    },
    {
        "id": "asm2",
        "title": "Practical 2",
        "topic": "Probability Distributions",
        "desc": "Normal distribution, effect of mean & sigma, Binomial PMF, and Poisson PMF.",
        "curl_da": "da.gd/s_asm2",
        "curl_is": "is.gd/sidasm2"
    },
    {
        "id": "asm3",
        "title": "Practical 3",
        "topic": "Confidence Intervals & Bootstrapping",
        "desc": "Student t-based 95% Confidence Interval & 5000-resample Bootstrap CI comparison on delivery time data.",
        "curl_da": "da.gd/s_asm3",
        "curl_is": "is.gd/sidasm3"
    },
    {
        "id": "asm4",
        "title": "Practical 4",
        "topic": "Hypothesis Testing",
        "desc": "Independent two-sample t-test (Titanic fare), Chi-Square test (class vs survival), One-Way ANOVA & Tukey HSD.",
        "curl_da": "da.gd/s_asm4",
        "curl_is": "is.gd/sidasm4"
    },
    {
        "id": "asm5",
        "title": "Practical 5",
        "topic": "A/B Testing",
        "desc": "Independent t-test comparing conversion/performance metrics across Control (Group A) and Treatment (Group B).",
        "curl_da": "da.gd/s_asm5",
        "curl_is": "is.gd/sidasm5"
    },
    {
        "id": "asm6",
        "title": "Practical 6",
        "topic": "Linear Regression & Correlation",
        "desc": "Diabetes dataset Simple OLS (BMI -> Target), Multiple OLS (BMI + BP + Age), and Spearman Rank Correlation.",
        "curl_da": "da.gd/s_asm6",
        "curl_is": "is.gd/sidasm6"
    },
    {
        "id": "asm7",
        "title": "Practical 7",
        "topic": "Logistic Regression & Classification",
        "desc": "Customer churn logistic model with confusion matrix & ROC/AUC, plus Penguin species classification pipeline with StandardScaler.",
        "curl_da": "da.gd/s_asm7",
        "curl_is": "is.gd/sidasm7"
    },
    {
        "id": "asm8",
        "title": "Practical 8",
        "topic": "Principal Component Analysis (PCA)",
        "desc": "PCA dimensionality reduction on Wine dataset (90% variance threshold, 2D scatter) & Breast Cancer dataset with scree plot.",
        "curl_da": "da.gd/s_asm8",
        "curl_is": "is.gd/sidasm8"
    },
    {
        "id": "asm9",
        "title": "Practical 9",
        "topic": "Bayesian Updating",
        "desc": "Medical diagnostic testing Bayesian update computing Prior, Sensitivity, Specificity, False Positive Rate & Posterior P(Disease|Positive).",
        "curl_da": "da.gd/s_asm9",
        "curl_is": "is.gd/sidasm9"
    }
]

code_dict = {}
for p in practicals:
    num = p["id"].replace("asm", "")
    with open(os.path.join(asm_dir, f'asm_{num}.py'), 'r', encoding='utf-8') as f:
        code_dict[p["id"]] = f.read()

with open(os.path.join(asm_dir, 'all_asm_practicals.py'), 'r', encoding='utf-8') as f:
    code_dict["asm_all"] = f.read()

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MSc BDA - Applied Statistical Methods (ASM Practicals 1-9)</title>
  <style>
    :root {
      --bg-primary: #0b0f19;
      --bg-secondary: #131b2e;
      --bg-card: #1a233a;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --accent: #38bdf8;
      --accent-hover: #0284c7;
      --code-bg: #070b14;
      --border: #263352;
      --success: #10b981;
      --purple: #a855f7;
      --purple-hover: #9333ea;
      --amber: #f59e0b;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    body { background-color: var(--bg-primary); color: var(--text-main); display: flex; min-height: 100vh; }

    /* Sidebar */
    .sidebar {
      width: 300px;
      background-color: var(--bg-secondary);
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      position: fixed;
      top: 0; bottom: 0; left: 0;
      z-index: 100;
    }

    .sidebar-header {
      padding: 18px 16px;
      border-bottom: 1px solid var(--border);
      background: linear-gradient(135deg, #131b2e, #0b0f19);
    }
    .sidebar-header h1 { font-size: 1.15rem; color: var(--accent); margin-bottom: 4px; }
    .sidebar-header p { font-size: 0.78rem; color: var(--text-muted); }

    .switch-banner {
      display: inline-block;
      margin-top: 10px;
      padding: 5px 10px;
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 6px;
      color: var(--accent);
      text-decoration: none;
      font-size: 0.78rem;
      font-weight: 600;
      transition: all 0.2s;
    }
    .switch-banner:hover { background: rgba(56, 189, 248, 0.25); color: #fff; }

    .nav-list { list-style: none; overflow-y: auto; flex-grow: 1; padding: 10px 8px; }
    .nav-item {
      padding: 10px 12px;
      margin-bottom: 4px;
      border-radius: 8px;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      color: #cbd5e1;
      font-size: 0.85rem;
      transition: all 0.2s;
      border: 1px solid transparent;
    }
    .nav-item:hover { background-color: #1e2c4a; color: #fff; }
    .nav-item.active { background-color: rgba(56, 189, 248, 0.15); border-color: var(--accent); color: var(--accent); font-weight: 600; }
    .nav-item-sub { font-size: 0.72rem; color: var(--text-muted); margin-top: 2px; }

    .mega-btn-wrap { padding: 14px 12px; border-top: 1px solid var(--border); background-color: var(--bg-secondary); }
    .btn-mega {
      width: 100%;
      background: linear-gradient(135deg, var(--purple), var(--purple-hover));
      color: white;
      border: none;
      padding: 12px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.88rem;
      cursor: pointer;
      box-shadow: 0 4px 14px rgba(168, 85, 247, 0.35);
      transition: all 0.2s;
    }
    .btn-mega:hover { transform: translateY(-1px); box-shadow: 0 6px 18px rgba(168, 85, 247, 0.5); }

    /* Main Content */
    .content { margin-left: 300px; padding: 32px 40px; flex-grow: 1; max-width: 1200px; }
    .section-header { margin-bottom: 24px; }
    .section-header h2 { font-size: 1.8rem; margin-bottom: 8px; color: #fff; }
    .section-header p { color: var(--text-muted); font-size: 0.95rem; line-height: 1.5; }

    /* Cheat Sheet Box */
    .cheat-box {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px;
      margin-bottom: 30px;
    }
    .cheat-box h3 { color: var(--amber); font-size: 1.1rem; margin-bottom: 12px; display: flex; align-items: center; gap: 8px; }
    .cheat-table { width: 100%; border-collapse: collapse; font-size: 0.88rem; }
    .cheat-table th, .cheat-table td { padding: 10px 12px; text-align: left; border-bottom: 1px solid var(--border); }
    .cheat-table th { color: var(--accent); font-weight: 600; }
    .code-pill {
      background: #050811;
      padding: 4px 8px;
      border-radius: 6px;
      border: 1px solid #1f2b45;
      color: #38bdf8;
      font-family: monospace;
      font-size: 0.85rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .code-pill:hover { background: #0f182c; border-color: var(--accent); }

    /* Code Card */
    .code-card {
      background-color: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow: hidden;
      margin-bottom: 30px;
    }
    .card-head {
      background-color: #151e33;
      padding: 14px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
    }
    .card-head-title { font-weight: 600; font-size: 1rem; color: #e2e8f0; }
    .btn-copy {
      background-color: #243252;
      color: #f1f5f9;
      border: 1px solid var(--border);
      padding: 7px 14px;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.82rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }
    .btn-copy:hover { background-color: var(--accent); color: #0b0f19; }

    pre {
      background-color: var(--code-bg);
      padding: 20px;
      overflow-x: auto;
      font-family: "Consolas", "Courier New", monospace;
      font-size: 0.88rem;
      line-height: 1.5;
      color: #e2e8f0;
      max-height: 600px;
    }

    /* Toast */
    .toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: var(--success);
      color: #0b0f19;
      padding: 12px 20px;
      border-radius: 8px;
      font-weight: 700;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 1000;
    }
    .toast.show { transform: translateY(0); opacity: 1; }
  </style>
</head>
<body>

  <!-- Sidebar -->
  <aside class="sidebar">
    <div class="sidebar-header">
      <h1>📊 ASM Practicals</h1>
      <p>Applied Statistical Methods • Practicals 1-9</p>
      <a href="index.html" class="switch-banner">⚡ Switch to AL Practicals</a>
    </div>

    <ul class="nav-list">
      <li class="nav-item active" onclick="scrollToSec('cheat-sheet')">
        <span>⚡ Quick Curl Cheat Sheet</span>
        <span class="nav-item-sub">One-click Jupyter copy</span>
      </li>
"""

for p in practicals:
    html_content += f"""      <li class="nav-item" onclick="scrollToSec('{p['id']}')">
        <span>{p['title']}</span>
        <span class="nav-item-sub">{p['topic']}</span>
      </li>
"""

html_content += f"""    </ul>

    <div class="mega-btn-wrap">
      <button class="btn-mega" onclick="copyCode('asm_all')">📋 Copy ALL ASM (1 to 9)</button>
    </div>
  </aside>

  <!-- Main Content -->
  <main class="content">

    <!-- Cheat Sheet Section -->
    <section id="cheat-sheet" class="cheat-box">
      <h3>⚡ Jupyter Notebook Quick Copy (Type in Cell)</h3>
      <p style="color: var(--text-muted); font-size: 0.85rem; margin-bottom: 14px;">
        Run any of these in a Jupyter cell to instantly copy that practical's code into your clipboard (then press Ctrl + V to paste):
      </p>
      <table class="cheat-table">
        <thead>
          <tr>
            <th>Practical</th>
            <th>da.gd (Short)</th>
            <th>is.gd (sid Format)</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr style="background: rgba(168, 85, 247, 0.1);">
            <td><strong>ALL Practicals (1-9)</strong></td>
            <td><code class="code-pill" onclick="copyText('!curl -sL da.gd/s_asm0 | clip')">!curl -sL da.gd/s_asm0 | clip</code></td>
            <td><code class="code-pill" onclick="copyText('!curl -sL is.gd/sidasmall | clip')">!curl -sL is.gd/sidasmall | clip</code></td>
            <td><button class="btn-copy" onclick="copyCode('asm_all')">Copy All</button></td>
          </tr>
"""

for p in practicals:
    html_content += f"""          <tr>
            <td><strong>{p['title']}</strong> ({p['topic']})</td>
            <td><code class="code-pill" onclick="copyText('!curl -sL {p['curl_da']} | clip')">!curl -sL {p['curl_da']} | clip</code></td>
            <td><code class="code-pill" onclick="copyText('!curl -sL {p['curl_is']} | clip')">!curl -sL {p['curl_is']} | clip</code></td>
            <td><button class="btn-copy" onclick="copyCode('{p['id']}')">Copy</button></td>
          </tr>
"""

html_content += """        </tbody>
      </table>
    </section>

    <!-- Practical Sections -->
"""

for p in practicals:
    code_raw = code_dict[p["id"]].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    html_content += f"""    <section id="{p['id']}" class="code-card">
      <div class="card-head">
        <div>
          <div class="card-head-title">{p['title']} — {p['topic']}</div>
          <div style="font-size: 0.78rem; color: var(--text-muted); margin-top: 3px;">
            Jupyter: <code class="code-pill" onclick="copyText('!curl -sL {p['curl_is']} | clip')">!curl -sL {p['curl_is']} | clip</code>
          </div>
        </div>
        <button class="btn-copy" onclick="copyCode('{p['id']}')">📋 Copy Code</button>
      </div>
      <pre><code>{code_raw}</code></pre>
    </section>
"""

html_content += f"""  </main>

  <div id="toast" class="toast">✓ Copied to clipboard!</div>

  <script>
    const codeData = {json.dumps(code_dict)};

    function copyCode(key) {{
      const text = codeData[key];
      if (!text) return;
      navigator.clipboard.writeText(text).then(() => {{
        showToast(key === 'asm_all' ? '✓ ALL ASM Practicals (1-9) Copied!' : '✓ ' + key.toUpperCase() + ' Code Copied!');
      }});
    }}

    function copyText(str) {{
      navigator.clipboard.writeText(str).then(() => {{
        showToast('✓ Command copied: ' + str);
      }});
    }}

    function showToast(msg) {{
      const toast = document.getElementById('toast');
      toast.innerText = msg;
      toast.classList.add('show');
      setTimeout(() => {{ toast.classList.remove('show'); }}, 2500);
    }}

    function scrollToSec(id) {{
      const el = document.getElementById(id);
      if (el) {{
        el.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
        document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
        event.currentTarget.classList.add('active');
      }}
    }}
  </script>
</body>
</html>
"""

with open(os.path.join(root, 'asm.html'), 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated asm.html successfully! Size:", len(html_content))
