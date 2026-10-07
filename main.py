import streamlit as st
import streamlit.components.v1 as components

# Set Streamlit page configuration
st.set_page_config(
    page_title="SAT Prep Hub",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit header padding and default footer
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
            max-width: 100% !important;
        }
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Complete HTML/CSS/JS single-file content
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SAT Prep Hub</title>
  <style>
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    :root {
      --navy-900: #0f172a;
      --navy-800: #1e293b;
      --blue-600: #2563eb;
      --blue-700: #1d4ed8;
      --blue-50: #eff6ff;
      --slate-50: #f8fafc;
      --slate-100: #f1f5f9;
      --slate-200: #e2e8f0;
      --slate-400: #94a3b8;
      --slate-600: #475569;
      --slate-800: #1e293b;
      --emerald-600: #059669;
      --emerald-50: #ecfdf5;
      --rose-600: #e11d48;
      --border-radius: 8px;
      --font-stack: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    body {
      font-family: var(--font-stack);
      background-color: var(--slate-100);
      color: var(--slate-800);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 40px;
    }

    .app-header {
      background-color: var(--navy-900);
      color: #ffffff;
      padding: 0 1.5rem;
      height: 64px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
      position: sticky;
      top: 0;
      z-index: 100;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-weight: 700;
      font-size: 1.15rem;
      letter-spacing: -0.02em;
    }

    .brand-badge {
      background-color: var(--blue-600);
      color: white;
      font-size: 0.75rem;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      text-transform: uppercase;
      font-weight: 800;
      letter-spacing: 0.05em;
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .nav-btn {
      background: transparent;
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: white;
      padding: 0.4rem 0.85rem;
      border-radius: 6px;
      font-size: 0.85rem;
      font-weight: 500;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.15s ease;
    }

    .nav-btn:hover {
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.4);
    }

    .kbd-shortcut {
      background: rgba(255, 255, 255, 0.2);
      padding: 0.1rem 0.35rem;
      border-radius: 3px;
      font-size: 0.7rem;
      font-family: monospace;
      text-transform: uppercase;
    }

    .container {
      max-width: 1100px;
      margin: 2rem auto;
      padding: 0 1rem;
    }

    .status-alert {
      display: none;
      background-color: var(--emerald-50);
      border: 1px solid #a7f3d0;
      color: #065f46;
      padding: 0.85rem 1.25rem;
      border-radius: var(--border-radius);
      margin-bottom: 1.5rem;
      font-size: 0.9rem;
      font-weight: 500;
      align-items: center;
      justify-content: space-between;
      box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }

    .status-alert.active {
      display: flex;
    }

    .close-alert {
      background: none;
      border: none;
      color: #065f46;
      font-size: 1.2rem;
      cursor: pointer;
      line-height: 1;
    }

    .view-panel {
      display: none;
    }

    .view-panel.active {
      display: block;
    }

    .dashboard-hero {
      background: linear-gradient(135deg, var(--navy-900) 0%, var(--navy-800) 100%);
      color: white;
      padding: 2.5rem;
      border-radius: 12px;
      margin-bottom: 2rem;
      box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }

    .dashboard-hero h1 {
      font-size: 2rem;
      font-weight: 800;
      margin-bottom: 0.5rem;
      letter-spacing: -0.025em;
    }

    .dashboard-hero p {
      color: var(--slate-400);
      font-size: 1rem;
      max-width: 650px;
    }

    .shortcuts-bar {
      display: flex;
      gap: 1.5rem;
      margin-top: 1.5rem;
      padding-top: 1.25rem;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      flex-wrap: wrap;
    }

    .shortcut-pill {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.85rem;
      color: #e2e8f0;
    }

    .shortcut-pill kbd {
      background: rgba(255,255,255,0.15);
      border: 1px solid rgba(255,255,255,0.25);
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
      font-family: monospace;
      font-weight: 600;
    }

    .grid-3 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(310px, 1fr));
      gap: 1.5rem;
    }

    .card {
      background: white;
      border: 1px solid var(--slate-200);
      border-radius: 10px;
      padding: 1.75rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.15s ease, box-shadow 0.15s ease;
      box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

    .card:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 16px -4px rgba(0, 0, 0, 0.08);
      border-color: #cbd5e1;
    }

    .card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1rem;
    }

    .card-icon {
      width: 44px;
      height: 44px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.25rem;
    }

    .icon-math { background: #dbeafe; color: var(--blue-600); }
    .icon-ela { background: #fce7f3; color: #db2777; }
    .icon-import { background: #fef3c7; color: #d97706; }

    .card-title {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--navy-900);
      margin-bottom: 0.5rem;
    }

    .card-desc {
      color: var(--slate-600);
      font-size: 0.9rem;
      margin-bottom: 1.5rem;
      flex-grow: 1;
    }

    .card-btn {
      width: 100%;
      padding: 0.65rem 1rem;
      border: none;
      border-radius: 6px;
      font-weight: 600;
      font-size: 0.9rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      transition: background 0.15s ease;
    }

    .btn-primary { background: var(--blue-600); color: white; }
    .btn-primary:hover { background: var(--blue-700); }

    .btn-secondary { background: var(--slate-800); color: white; }
    .btn-secondary:hover { background: var(--navy-900); }

    .btn-outline { background: white; border: 1px solid var(--slate-200); color: var(--slate-800); }
    .btn-outline:hover { background: var(--slate-50); border-color: var(--slate-400); }

    .drop-zone {
      border: 2px dashed #cbd5e1;
      border-radius: 8px;
      padding: 1.5rem;
      text-align: center;
      background: var(--slate-50);
      cursor: pointer;
      transition: all 0.2s ease;
      margin-top: 1rem;
    }

    .drop-zone.dragover {
      border-color: var(--blue-600);
      background: var(--blue-50);
    }

    .drop-zone-text {
      font-size: 0.85rem;
      color: var(--slate-600);
    }

    .test-header {
      background: white;
      padding: 1rem 1.5rem;
      border-radius: 8px;
      border: 1px solid var(--slate-200);
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1.5rem;
    }

    .test-title {
      font-weight: 700;
      font-size: 1.1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .test-body {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1.5rem;
    }

    .test-body.split-view {
      grid-template-columns: 1fr 1fr;
    }

    @media (max-width: 768px) {
      .test-body.split-view {
        grid-template-columns: 1fr;
      }
    }

    .panel-box {
      background: white;
      border: 1px solid var(--slate-200);
      border-radius: 8px;
      padding: 1.75rem;
    }

    .passage-box {
      font-size: 0.95rem;
      color: #334155;
      line-height: 1.7;
      max-height: 500px;
      overflow-y: auto;
      padding-right: 0.5rem;
    }

    .question-tag {
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--slate-400);
      letter-spacing: 0.05em;
      margin-bottom: 0.5rem;
    }

    .question-text {
      font-weight: 600;
      font-size: 1.05rem;
      color: var(--navy-900);
      margin-bottom: 1.25rem;
    }

    .options-list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      margin-bottom: 1.5rem;
    }

    .option-item {
      display: flex;
      align-items: center;
      padding: 0.85rem 1rem;
      border: 1px solid var(--slate-200);
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.15s ease;
      font-size: 0.95rem;
    }

    .option-item:hover {
      background: var(--slate-50);
      border-color: var(--slate-400);
    }

    .option-item.selected {
      border-color: var(--blue-600);
      background: var(--blue-50);
      font-weight: 600;
    }

    .option-key {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      border: 1px solid var(--slate-400);
      display: flex;
      align-items: center;
      justify-content: center;
      margin-right: 0.75rem;
      font-size: 0.8rem;
      font-weight: 700;
      flex-shrink: 0;
    }

    .option-item.selected .option-key {
      background: var(--blue-600);
      color: white;
      border-color: var(--blue-600);
    }

    .test-actions {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 1rem;
      border-top: 1px solid var(--slate-200);
    }

    .feedback-box {
      margin-top: 1rem;
      padding: 1rem;
      border-radius: 6px;
      font-size: 0.9rem;
      display: none;
    }

    .feedback-box.correct {
      display: block;
      background: var(--emerald-50);
      border: 1px solid #a7f3d0;
      color: #065f46;
    }

    .feedback-box.incorrect {
      display: block;
      background: #fff1f2;
      border: 1px solid #fecdd3;
      color: #9f1239;
    }

    .reference-sheet {
      display: none;
      background: #f8fafc;
      border: 1px solid var(--slate-200);
      border-radius: 8px;
      padding: 1rem;
      margin-bottom: 1.5rem;
      font-size: 0.85rem;
    }

    .reference-sheet.active {
      display: block;
    }

    .ref-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
      gap: 0.75rem;
      text-align: center;
      margin-top: 0.5rem;
    }

    .ref-item {
      background: white;
      padding: 0.5rem;
      border-radius: 4px;
      border: 1px solid var(--slate-200);
    }
  </style>
</head>
<body>

  <header class="app-header">
    <div class="brand">
      <span>SAT Prep Hub</span>
      <span class="brand-badge">Digital</span>
    </div>
    <div class="nav-actions">
      <button class="nav-btn" onclick="showView('dashboardView')" title="Dashboard (Esc)">
        <span>Home</span>
        <span class="kbd-shortcut">Esc</span>
      </button>
      <button class="nav-btn" onclick="showView('mathView')" title="Math Practice (Ctrl+M)">
        <span>Math</span>
        <span class="kbd-shortcut">Ctrl+M</span>
      </button>
      <button class="nav-btn" onclick="showView('elaView')" title="ELA Practice (Ctrl+E)">
        <span>ELA</span>
        <span class="kbd-shortcut">Ctrl+E</span>
      </button>
      <button class="nav-btn" onclick="triggerImport()" title="Import Test File (Ctrl+H)">
        <span>Import HTML</span>
        <span class="kbd-shortcut">Ctrl+H</span>
      </button>
    </div>
  </header>

  <main class="container">
    <div id="statusAlert" class="status-alert">
      <span id="statusMessage">File loaded successfully.</span>
      <button class="close-alert" onclick="dismissAlert()">&times;</button>
    </div>

    <!-- VIEW 1: Dashboard -->
    <section id="dashboardView" class="view-panel active">
      <div class="dashboard-hero">
        <h1>Digital SAT Prep Suite</h1>
        <p>Master the Digital SAT with interactive practice modules, instant question feedback, and rapid custom HTML test importing.</p>
        <div class="shortcuts-bar">
          <div class="shortcut-pill"><kbd>Ctrl</kbd> + <kbd>M</kbd> Math Practice</div>
          <div class="shortcut-pill"><kbd>Ctrl</kbd> + <kbd>E</kbd> ELA Practice</div>
          <div class="shortcut-pill"><kbd>Ctrl</kbd> + <kbd>H</kbd> Import HTML Test</div>
          <div class="shortcut-pill"><kbd>Esc</kbd> Return Home</div>
        </div>
      </div>

      <div class="grid-3">
        <div class="card">
          <div>
            <div class="card-header">
              <div class="card-icon icon-math">&sum;</div>
              <span class="kbd-shortcut">Ctrl+M</span>
            </div>
            <h2 class="card-title">Math Section</h2>
            <p class="card-desc">Practice Algebra, Advanced Math, Problem-Solving, and Geometry. Built-in reference sheet available.</p>
          </div>
          <button class="card-btn btn-primary" onclick="showView('mathView')">Start Math Practice</button>
        </div>

        <div class="card">
          <div>
            <div class="card-header">
              <div class="card-icon icon-ela">&para;</div>
              <span class="kbd-shortcut">Ctrl+E</span>
            </div>
            <h2 class="card-title">Reading & Writing</h2>
            <p class="card-desc">Master Craft and Structure, Information and Ideas, Standard English Conventions, and Expression of Ideas.</p>
          </div>
