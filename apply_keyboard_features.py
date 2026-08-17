import json
import os

print("Updating index.html and standalone HTML file with keyboard shortcuts...")

with open('1100_cau_triet_hoc.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

json_str = json.dumps(questions, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ôn Thi Trắc Nghiệm Triết Học Mác - Lênin (1190 Câu)</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-primary: #f8fafc;
            --bg-card: #ffffff;
            --bg-secondary: #f1f5f9;
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --text-muted: #94a3b8;
            --border-color: #e2e8f0;
            --accent-color: #4f46e5;
            --accent-hover: #4338ca;
            --accent-light: #e0e7ff;
            --correct-bg: #ecfdf5;
            --correct-border: #10b981;
            --correct-text: #047857;
            --incorrect-bg: #fef2f2;
            --incorrect-border: #ef4444;
            --incorrect-text: #b91c1c;
            --warning-bg: #fffbeb;
            --warning-border: #f59e0b;
            --warning-text: #b45309;
            --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
            --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
            --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
            --radius-sm: 8px;
            --radius-md: 12px;
            --radius-lg: 16px;
        }

        [data-theme="dark"] {
            --bg-primary: #0f172a;
            --bg-card: #1e293b;
            --bg-secondary: #334155;
            --text-primary: #f8fafc;
            --text-secondary: #cbd5e1;
            --text-muted: #64748b;
            --border-color: #334155;
            --accent-color: #6366f1;
            --accent-hover: #818cf8;
            --accent-light: #312e81;
            --correct-bg: #064e3b;
            --correct-border: #10b981;
            --correct-text: #a7f3d0;
            --incorrect-bg: #7f1d1d;
            --incorrect-border: #ef4444;
            --incorrect-text: #fecaca;
            --warning-bg: #78350f;
            --warning-border: #f59e0b;
            --warning-text: #fde68a;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Be Vietnam Pro', sans-serif;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            background-color: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.6;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            transition: background-color 0.3s, color 0.3s;
        }

        header {
            background-color: var(--bg-card);
            border-bottom: 1px solid var(--border-color);
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: var(--shadow-sm);
        }

        .header-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 12px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
        }

        .logo-group {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .logo-icon {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, #4f46e5, #7c3aed);
            color: white;
            border-radius: var(--radius-md);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            font-size: 1.2rem;
            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
        }

        .logo-title h1 {
            font-size: 1.15rem;
            font-weight: 700;
            line-height: 1.2;
            color: var(--text-primary);
        }

        .logo-title p {
            font-size: 0.8rem;
            color: var(--text-muted);
        }

        .header-actions {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 8px 16px;
            border-radius: var(--radius-sm);
            font-size: 0.875rem;
            font-weight: 600;
            cursor: pointer;
            border: 1px solid transparent;
            transition: all 0.2s ease;
            outline: none;
        }

        .btn-primary {
            background-color: var(--accent-color);
            color: white;
        }

        .btn-primary:hover {
            background-color: var(--accent-hover);
        }

        .btn-secondary {
            background-color: var(--bg-secondary);
            color: var(--text-primary);
            border-color: var(--border-color);
        }

        .btn-secondary:hover {
            background-color: var(--border-color);
        }

        .btn-icon {
            padding: 8px;
            border-radius: 50%;
            width: 38px;
            height: 38px;
        }

        .shortcut-bar {
            background-color: var(--bg-secondary);
            border-bottom: 1px solid var(--border-color);
            padding: 6px 20px;
            font-size: 0.8rem;
            color: var(--text-secondary);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 16px;
            flex-wrap: wrap;
        }

        .shortcut-badge {
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 700;
            color: var(--accent-color);
            font-size: 0.75rem;
        }

        .main-layout {
            max-width: 1200px;
            width: 100%;
            margin: 0 auto;
            padding: 24px 20px;
            display: grid;
            grid-template-columns: 1fr 320px;
            gap: 24px;
            flex: 1;
        }

        @media (max-width: 900px) {
            .main-layout {
                grid-template-columns: 1fr;
            }
        }

        .stats-bar {
            background-color: var(--bg-card);
            border-radius: var(--radius-md);
            border: 1px solid var(--border-color);
            padding: 16px 20px;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 16px;
            margin-bottom: 20px;
            box-shadow: var(--shadow-sm);
        }

        @media (max-width: 600px) {
            .stats-bar {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        .stat-item {
            text-align: center;
        }

        .stat-value {
            font-size: 1.5rem;
            font-weight: 800;
            line-height: 1.2;
        }

        .stat-label {
            font-size: 0.75rem;
            color: var(--text-muted);
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .stat-done { color: var(--accent-color); }
        .stat-correct { color: var(--correct-border); }
        .stat-incorrect { color: var(--incorrect-border); }
        .stat-rate { color: var(--warning-border); }

        .progress-bar-container {
            width: 100%;
            height: 6px;
            background-color: var(--bg-secondary);
            border-radius: 3px;
            overflow: hidden;
            margin-top: 12px;
            grid-column: 1 / -1;
        }

        .progress-bar-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--accent-color), #10b981);
            width: 0%;
            transition: width 0.3s ease;
        }

        /* Filter Controls */
        .controls-card {
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            padding: 16px;
            margin-bottom: 20px;
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            align-items: center;
            justify-content: space-between;
        }

        .search-box {
            flex: 1;
            min-width: 220px;
            position: relative;
        }

        .search-box input {
            width: 100%;
            padding: 8px 14px 8px 36px;
            border-radius: var(--radius-sm);
            border: 1px solid var(--border-color);
            background-color: var(--bg-primary);
            color: var(--text-primary);
            font-size: 0.875rem;
            outline: none;
            transition: border-color 0.2s;
        }

        .search-box input:focus {
            border-color: var(--accent-color);
        }

        .search-icon {
            position: absolute;
            left: 10px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
            pointer-events: none;
        }

        .filter-tabs {
            display: flex;
            gap: 6px;
            background-color: var(--bg-secondary);
            padding: 4px;
            border-radius: var(--radius-sm);
        }

        .filter-btn {
            padding: 6px 12px;
            font-size: 0.8rem;
            font-weight: 600;
            border: none;
            background: none;
            color: var(--text-secondary);
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .filter-btn.active {
            background-color: var(--bg-card);
            color: var(--text-primary);
            box-shadow: var(--shadow-sm);
        }

        /* Question Container */
        .question-card {
            background-color: var(--bg-card);
            border-radius: var(--radius-lg);
            border: 1px solid var(--border-color);
            padding: 28px;
            box-shadow: var(--shadow-md);
            margin-bottom: 20px;
            position: relative;
        }

        .question-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 20px;
            gap: 12px;
        }

        .question-badge {
            background-color: var(--accent-light);
            color: var(--accent-color);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .bookmark-btn {
            background: none;
            border: none;
            color: var(--text-muted);
            cursor: pointer;
            font-size: 1.25rem;
            transition: color 0.2s;
            padding: 4px;
        }

        .bookmark-btn.active {
            color: var(--warning-border);
        }

        .question-title {
            font-size: 1.15rem;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 24px;
            line-height: 1.5;
        }

        .options-list {
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-bottom: 24px;
        }

        .option-item {
            display: flex;
            align-items: flex-start;
            gap: 14px;
            padding: 14px 18px;
            border-radius: var(--radius-md);
            border: 1.5px solid var(--border-color);
            background-color: var(--bg-card);
            cursor: pointer;
            transition: all 0.2s ease;
            text-align: left;
            width: 100%;
            font-size: 0.95rem;
            color: var(--text-primary);
            position: relative;
        }

        .option-item:hover:not(.disabled) {
            border-color: var(--accent-color);
            background-color: var(--accent-light);
        }

        .option-key {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background-color: var(--bg-secondary);
            color: var(--text-secondary);
            font-weight: 700;
            font-size: 0.85rem;
            flex-shrink: 0;
            transition: all 0.2s;
        }

        .option-item:hover:not(.disabled) .option-key {
            background-color: var(--accent-color);
            color: white;
        }

        .option-text {
            flex: 1;
            padding-top: 2px;
        }

        .key-hint {
            font-size: 0.75rem;
            background-color: var(--bg-secondary);
            border: 1px solid var(--border-color);
            padding: 2px 6px;
            border-radius: 4px;
            color: var(--text-muted);
            font-weight: 600;
            flex-shrink: 0;
            align-self: center;
        }

        /* Option Feedback States */
        .option-item.selected-correct {
            border-color: var(--correct-border);
            background-color: var(--correct-bg);
            color: var(--correct-text);
        }

        .option-item.selected-correct .option-key {
            background-color: var(--correct-border);
            color: white;
        }

        .option-item.selected-incorrect {
            border-color: var(--incorrect-border);
            background-color: var(--incorrect-bg);
            color: var(--incorrect-text);
        }

        .option-item.selected-incorrect .option-key {
            background-color: var(--incorrect-border);
            color: white;
        }

        .option-item.show-correct {
            border-color: var(--correct-border);
            background-color: var(--correct-bg);
            color: var(--correct-text);
            box-shadow: 0 0 0 2px var(--correct-border);
        }

        .option-item.show-correct .option-key {
            background-color: var(--correct-border);
            color: white;
        }

        .option-item.disabled {
            cursor: default;
        }

        /* Explanation Box */
        .explanation-box {
            display: none;
            padding: 16px 20px;
            border-radius: var(--radius-md);
            margin-top: 20px;
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .explanation-box.correct {
            display: block;
            background-color: var(--correct-bg);
            border: 1px solid var(--correct-border);
            color: var(--correct-text);
        }

        .explanation-box.incorrect {
            display: block;
            background-color: var(--incorrect-bg);
            border: 1px solid var(--incorrect-border);
            color: var(--incorrect-text);
        }

        .explanation-header {
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 700;
            font-size: 1rem;
            margin-bottom: 6px;
        }

        .explanation-body {
            font-size: 0.9rem;
            line-height: 1.5;
        }

        /* Pagination & Actions */
        .nav-actions {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 12px;
        }

        .jump-box {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.875rem;
            color: var(--text-secondary);
        }

        .jump-box input {
            width: 70px;
            padding: 6px 10px;
            border-radius: var(--radius-sm);
            border: 1px solid var(--border-color);
            background-color: var(--bg-card);
            color: var(--text-primary);
            text-align: center;
            font-weight: 600;
        }

        /* Sidebar Grid Navigation */
        .sidebar {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .grid-card {
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: var(--radius-lg);
            padding: 20px;
            box-shadow: var(--shadow-sm);
        }

        .grid-card-title {
            font-size: 0.95rem;
            font-weight: 700;
            margin-bottom: 14px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .question-grid {
            display: grid;
            grid-template-columns: repeat(6, 1fr);
            gap: 6px;
            max-height: 380px;
            overflow-y: auto;
            padding-right: 4px;
        }

        .grid-item {
            aspect-ratio: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: var(--radius-sm);
            font-size: 0.75rem;
            font-weight: 600;
            border: 1px solid var(--border-color);
            background-color: var(--bg-secondary);
            color: var(--text-secondary);
            cursor: pointer;
            transition: all 0.15s;
        }

        .grid-item:hover {
            border-color: var(--accent-color);
            transform: scale(1.05);
        }

        .grid-item.active {
            outline: 2px solid var(--accent-color);
            font-weight: 800;
        }

        .grid-item.done-correct {
            background-color: var(--correct-border);
            color: white;
            border-color: var(--correct-border);
        }

        .grid-item.done-incorrect {
            background-color: var(--incorrect-border);
            color: white;
            border-color: var(--incorrect-border);
        }

        .legend {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-top: 14px;
            font-size: 0.75rem;
            color: var(--text-secondary);
        }

        .legend-item {
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .legend-dot {
            width: 12px;
            height: 12px;
            border-radius: 3px;
        }

        footer {
            margin-top: auto;
            background-color: var(--bg-card);
            border-top: 1px solid var(--border-color);
            padding: 16px 20px;
            text-align: center;
            font-size: 0.85rem;
            color: var(--text-muted);
        }
    </style>
</head>
<body>

    <header>
        <div class="header-container">
            <div class="logo-group">
                <div class="logo-icon">T</div>
                <div class="logo-title">
                    <h1>Triết Học Mác - Lênin</h1>
                    <p>1,190 câu trắc nghiệm có đáp án & giải thích</p>
                </div>
            </div>
            <div class="header-actions">
                <button class="btn btn-secondary btn-icon" id="themeToggleBtn" title="Đổi giao diện Sáng/Tối">
                    🌙
                </button>
                <button class="btn btn-secondary" id="resetProgressBtn" style="color: var(--incorrect-border);">
                    🔄 Đặt lại tiến độ
                </button>
            </div>
        </div>
        <div class="shortcut-bar">
            <span>⌨️ <strong>Phím tắt chọn đáp án:</strong> <span class="shortcut-badge">1</span>=A &nbsp; <span class="shortcut-badge">2</span>=B &nbsp; <span class="shortcut-badge">3</span>=C &nbsp; <span class="shortcut-badge">4</span>=D</span>
            <span>&bull;</span>
            <span><strong>Chuyển câu:</strong> Phím mũi tên <span class="shortcut-badge">⬅️</span> <span class="shortcut-badge">⬆️</span> (Lùi) / <span class="shortcut-badge">➡️</span> <span class="shortcut-badge">⬇️</span> (Tới)</span>
        </div>
    </header>

    <div class="main-layout">
        <main>
            <!-- Stats Summary -->
            <div class="stats-bar">
                <div class="stat-item">
                    <div class="stat-value stat-done" id="statDone">0 / 1190</div>
                    <div class="stat-label">Đã hoàn thành</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value stat-correct" id="statCorrect">0</div>
                    <div class="stat-label">Câu Đúng</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value stat-incorrect" id="statIncorrect">0</div>
                    <div class="stat-label">Câu Sai</div>
                </div>
                <div class="stat-item">
                    <div class="stat-value stat-rate" id="statRate">0%</div>
                    <div class="stat-label">Tỷ lệ chính xác</div>
                </div>
                <div class="progress-bar-container">
                    <div class="progress-bar-fill" id="progressBarFill"></div>
                </div>
            </div>

            <!-- Controls & Filters -->
            <div class="controls-card">
                <div class="search-box">
                    <span class="search-icon">🔍</span>
                    <input type="text" id="searchInput" placeholder="Tìm câu hỏi theo nội dung hoặc số câu...">
                </div>
                <div class="filter-tabs">
                    <button class="filter-btn active" data-filter="all">Tất cả (1190)</button>
                    <button class="filter-btn" data-filter="unanswered">Chưa làm</button>
                    <button class="filter-btn" data-filter="incorrect">Cần ôn lại (Sai)</button>
                    <button class="filter-btn" data-filter="bookmarked">Đã đánh dấu ⭐</button>
                </div>
            </div>

            <!-- Question Card -->
            <div class="question-card" id="questionCard">
                <div class="question-header">
                    <span class="question-badge" id="questionBadge">Câu 1 / 1190</span>
                    <button class="bookmark-btn" id="bookmarkBtn" title="Đánh dấu câu hỏi này">⭐</button>
                </div>

                <div class="question-title" id="questionText">Đang tải câu hỏi...</div>

                <div class="options-list" id="optionsContainer">
                    <!-- Option items rendered by JS -->
                </div>

                <!-- Explanation / Answer Feedback -->
                <div class="explanation-box" id="explanationBox">
                    <div class="explanation-header" id="explanationHeader">
                        <span id="explanationIcon"></span>
                        <span id="explanationTitle"></span>
                    </div>
                    <div class="explanation-body" id="explanationText"></div>
                </div>
            </div>

            <!-- Navigation Controls -->
            <div class="nav-actions">
                <button class="btn btn-secondary" id="prevBtn">⬅️ Câu trước (Phím ⬅️ ⬆️)</button>
                
                <div class="jump-box">
                    <span>Đến câu:</span>
                    <input type="number" id="jumpInput" min="1" max="1190" value="1">
                    <button class="btn btn-secondary" id="jumpBtn" style="padding: 6px 12px;">Go</button>
                </div>

                <button class="btn btn-primary" id="nextBtn">Câu tiếp (Phím ➡️ ⬇️) ➡️</button>
            </div>
        </main>

        <!-- Sidebar Navigation Grid -->
        <aside class="sidebar">
            <div class="grid-card">
                <div class="grid-card-title">
                    <span>Danh sách câu hỏi</span>
                    <span style="font-size: 0.8rem; color: var(--text-muted);" id="filteredCount">1190 câu</span>
                </div>

                <div class="question-grid" id="questionGrid">
                    <!-- Grid items 1..1190 rendered by JS -->
                </div>

                <div class="legend">
                    <div class="legend-item">
                        <div class="legend-dot" style="background: var(--bg-secondary); border: 1px solid var(--border-color);"></div> Chưa làm
                    </div>
                    <div class="legend-item">
                        <div class="legend-dot" style="background: var(--correct-border);"></div> Đúng
                    </div>
                    <div class="legend-item">
                        <div class="legend-dot" style="background: var(--incorrect-border);"></div> Sai
                    </div>
                </div>
            </div>
        </aside>
    </div>

    <footer>
        Web làm trắc nghiệm Triết Học Mác - Lênin &bull; Dữ liệu lưu trực tiếp trên thiết bị (LocalStorage) &bull; Miễn phí 100%
    </footer>

    <!-- Inline dataset -->
    <script>
    window.quizQuestions = __DATASET_PLACEHOLDER__;
    </script>

    <script>
        // State Management
        let questions = window.quizQuestions || [];
        let currentIndex = 0;
        let filteredIndices = [];
        let currentFilter = 'all';

        // Local Storage Keys
        const STORAGE_KEY_USER_ANSWERS = 'triet_quiz_user_answers';
        const STORAGE_KEY_BOOKMARKS = 'triet_quiz_bookmarks';
        const STORAGE_KEY_THEME = 'triet_quiz_theme';

        // User Data State
        let userAnswers = JSON.parse(localStorage.getItem(STORAGE_KEY_USER_ANSWERS)) || {};
        let bookmarks = JSON.parse(localStorage.getItem(STORAGE_KEY_BOOKMARKS)) || {};

        // DOM Elements
        const questionBadge = document.getElementById('questionBadge');
        const questionText = document.getElementById('questionText');
        const optionsContainer = document.getElementById('optionsContainer');
        const explanationBox = document.getElementById('explanationBox');
        const explanationIcon = document.getElementById('explanationIcon');
        const explanationTitle = document.getElementById('explanationTitle');
        const explanationText = document.getElementById('explanationText');
        const bookmarkBtn = document.getElementById('bookmarkBtn');

        const prevBtn = document.getElementById('prevBtn');
        const nextBtn = document.getElementById('nextBtn');
        const jumpInput = document.getElementById('jumpInput');
        const jumpBtn = document.getElementById('jumpBtn');

        const searchInput = document.getElementById('searchInput');
        const questionGrid = document.getElementById('questionGrid');
        const filteredCount = document.getElementById('filteredCount');

        const statDone = document.getElementById('statDone');
        const statCorrect = document.getElementById('statCorrect');
        const statIncorrect = document.getElementById('statIncorrect');
        const statRate = document.getElementById('statRate');
        const progressBarFill = document.getElementById('progressBarFill');
        const themeToggleBtn = document.getElementById('themeToggleBtn');
        const resetProgressBtn = document.getElementById('resetProgressBtn');

        // Theme Initialization
        const savedTheme = localStorage.getItem(STORAGE_KEY_THEME) || 'light';
        document.documentElement.setAttribute('data-theme', savedTheme);
        themeToggleBtn.textContent = savedTheme === 'dark' ? '☀️' : '🌙';

        themeToggleBtn.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem(STORAGE_KEY_THEME, newTheme);
            themeToggleBtn.textContent = newTheme === 'dark' ? '☀️' : '🌙';
        });

        // Initialize App
        function initApp() {
            if (!questions || questions.length === 0) {
                questionText.textContent = "Không thể tải dữ liệu câu hỏi. Tải lại trang...";
                return;
            }
            applyFilters();
            renderStats();
            renderQuestion(currentIndex);
        }

        // Apply Search and Category Filters
        function applyFilters() {
            const searchTerm = searchInput.value.trim().toLowerCase();

            filteredIndices = [];
            questions.forEach((q, idx) => {
                const qNum = q.id;
                const qContent = (q.question || '').toLowerCase();
                const uAns = userAnswers[qNum];
                const isBookmarked = !!bookmarks[qNum];

                let matchesSearch = true;
                if (searchTerm) {
                    matchesSearch = qNum.toString().includes(searchTerm) || qContent.includes(searchTerm);
                }

                let matchesTab = true;
                if (currentFilter === 'unanswered') {
                    matchesTab = !uAns;
                } else if (currentFilter === 'incorrect') {
                    matchesTab = uAns && !uAns.isCorrect;
                } else if (currentFilter === 'bookmarked') {
                    matchesTab = isBookmarked;
                }

                if (matchesSearch && matchesTab) {
                    filteredIndices.push(idx);
                }
            });

            filteredCount.textContent = filteredIndices.length + ' câu';
            renderGrid();

            if (filteredIndices.length > 0) {
                if (!filteredIndices.includes(currentIndex)) {
                    currentIndex = filteredIndices[0];
                }
            }
        }

        // Render Sidebar Navigation Grid
        function renderGrid() {
            questionGrid.innerHTML = '';
            filteredIndices.forEach(idx => {
                const q = questions[idx];
                const item = document.createElement('div');
                item.className = 'grid-item';
                item.textContent = q.id;

                const uAns = userAnswers[q.id];
                if (uAns) {
                    if (uAns.isCorrect) {
                        item.classList.add('done-correct');
                    } else {
                        item.classList.add('done-incorrect');
                    }
                }

                if (idx === currentIndex) {
                    item.classList.add('active');
                }

                item.addEventListener('click', () => {
                    currentIndex = idx;
                    renderQuestion(currentIndex);
                    renderGrid();
                });

                questionGrid.appendChild(item);
            });
        }

        // Render Current Question
        function renderQuestion(index) {
            if (index < 0 || index >= questions.length) return;

            const q = questions[index];
            const qNum = q.id;

            questionBadge.textContent = 'Câu ' + qNum + ' / ' + questions.length;
            questionText.textContent = qNum + '. ' + q.question;

            if (bookmarks[qNum]) {
                bookmarkBtn.classList.add('active');
            } else {
                bookmarkBtn.classList.remove('active');
            }

            optionsContainer.innerHTML = '';
            explanationBox.className = 'explanation-box';
            explanationBox.style.display = 'none';

            const userState = userAnswers[qNum];
            const isAnswered = !!userState;

            const labelToKeyNum = { 'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5' };

            q.options.forEach(opt => {
                const btn = document.createElement('button');
                btn.className = 'option-item';

                if (isAnswered) {
                    btn.classList.add('disabled');

                    if (opt.label === q.correct) {
                        btn.classList.add('show-correct');
                    }
                    if (opt.label === userState.selectedLabel && !userState.isCorrect) {
                        btn.classList.add('selected-incorrect');
                    }
                }

                const keyNum = labelToKeyNum[opt.label] || '';

                btn.innerHTML = '<div class="option-key">' + opt.label + '</div>' +
                    '<div class="option-text">' + opt.text + '</div>' +
                    (keyNum ? '<span class="key-hint" title="Bấm phím ' + keyNum + ' trên bàn phím để chọn">Phím ' + keyNum + '</span>' : '');

                if (!isAnswered) {
                    btn.addEventListener('click', () => handleSelectOption(q, opt.label));
                }

                optionsContainer.appendChild(btn);
            });

            if (isAnswered) {
                const wrongReason = (q.wrong_explanations && userState.selectedLabel) ? q.wrong_explanations[userState.selectedLabel] : '';
                showExplanation(userState.isCorrect, userState.selectedLabel, q.correct, q.explanation || q.raw_answer, wrongReason, q.options);
            }

            jumpInput.value = qNum;
            renderGrid();
        }

        // Option Click Handler
        function handleSelectOption(q, selectedLabel) {
            const isCorrect = (selectedLabel === q.correct);

            userAnswers[q.id] = {
                selectedLabel: selectedLabel,
                isCorrect: isCorrect,
                timestamp: Date.now()
            };

            localStorage.setItem(STORAGE_KEY_USER_ANSWERS, JSON.stringify(userAnswers));
            renderStats();
            renderQuestion(currentIndex);
        }

        // Show Explanation / Answer Feedback
        function showExplanation(isCorrect, selectedLabel, correctLabel, expText, wrongReason, optionsList) {
            explanationBox.style.display = 'block';

            const optMap = {};
            if (optionsList) {
                optionsList.forEach(o => optMap[o.label] = o.text);
            }

            if (isCorrect) {
                explanationBox.className = 'explanation-box correct';
                explanationIcon.textContent = '🎉';
                explanationTitle.textContent = 'Chính Xác!';
                explanationText.innerHTML = '<div style="font-weight: 600; margin-bottom: 6px;">Bạn đã chọn đúng đáp án <strong>' + correctLabel + '</strong>: ' + (optMap[correctLabel] || '') + '</div>' +
                    '<div style="line-height: 1.6; margin-top: 8px; white-space: pre-line;">' + (expText || '') + '</div>';
            } else {
                explanationBox.className = 'explanation-box incorrect';
                explanationIcon.textContent = '❌';
                explanationTitle.textContent = 'Chưa Chính Xác!';
                
                const selectedText = optMap[selectedLabel] ? (' (' + optMap[selectedLabel] + ')') : '';
                const correctText = optMap[correctLabel] ? (' (' + optMap[correctLabel] + ')') : '';

                explanationText.innerHTML = 
                    '<div style="margin-bottom: 6px; font-weight: 600;">' +
                        '🔴 Lựa chọn của bạn: <strong>' + selectedLabel + '</strong>' + selectedText +
                    '</div>' +
                    (wrongReason ? '<div style="background: rgba(239, 68, 68, 0.08); border-left: 3px solid var(--incorrect-border); padding: 8px 12px; margin: 8px 0; border-radius: 6px; font-size: 0.88rem;">' +
                        '<strong>⚠️ Lý do lựa chọn của bạn chưa đúng:</strong><br>' + wrongReason +
                    '</div>' : '') +
                    '<div style="margin-bottom: 6px; font-weight: 600; margin-top: 10px;">' +
                        '🟢 Đáp án chuẩn xác: <strong>' + correctLabel + '</strong>' + correctText +
                    '</div>' +
                    '<div style="line-height: 1.6; margin-top: 8px; border-top: 1px dashed var(--border-color); padding-top: 8px; white-space: pre-line;">' +
                        (expText || '') +
                    '</div>';
            }
        }

        // Render Summary Statistics
        function renderStats() {
            const total = questions.length;
            const answeredKeys = Object.keys(userAnswers);
            const doneCount = answeredKeys.length;
            
            let correctCount = 0;
            answeredKeys.forEach(k => {
                if (userAnswers[k].isCorrect) correctCount++;
            });

            const incorrectCount = doneCount - correctCount;
            const rate = doneCount > 0 ? Math.round((correctCount / doneCount) * 100) : 0;
            const progressPercent = Math.round((doneCount / total) * 100);

            statDone.textContent = doneCount + ' / ' + total;
            statCorrect.textContent = correctCount;
            statIncorrect.textContent = incorrectCount;
            statRate.textContent = rate + '%';
            progressBarFill.style.width = progressPercent + '%';
        }

        // Event Listeners
        prevBtn.addEventListener('click', () => {
            if (currentIndex > 0) {
                currentIndex--;
                renderQuestion(currentIndex);
            }
        });

        nextBtn.addEventListener('click', () => {
            if (currentIndex < questions.length - 1) {
                currentIndex++;
                renderQuestion(currentIndex);
            }
        });

        jumpBtn.addEventListener('click', () => {
            const val = parseInt(jumpInput.value, 10);
            if (val >= 1 && val <= questions.length) {
                currentIndex = val - 1;
                renderQuestion(currentIndex);
            }
        });

        jumpInput.addEventListener('keyup', (e) => {
            if (e.key === 'Enter') {
                jumpBtn.click();
            }
        });

        bookmarkBtn.addEventListener('click', () => {
            const qNum = questions[currentIndex].id;
            if (bookmarks[qNum]) {
                delete bookmarks[qNum];
            } else {
                bookmarks[qNum] = true;
            }
            localStorage.setItem(STORAGE_KEY_BOOKMARKS, JSON.stringify(bookmarks));
            renderQuestion(currentIndex);
        });

        // Filter tab buttons
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                currentFilter = btn.dataset.filter;
                applyFilters();
                renderQuestion(currentIndex);
            });
        });

        // Search input
        searchInput.addEventListener('input', () => {
            applyFilters();
            renderQuestion(currentIndex);
        });

        // Reset progress
        resetProgressBtn.addEventListener('click', () => {
            if (confirm('Bạn có chắc chắn muốn xóa toàn bộ lịch sử tiến độ làm bài không?')) {
                userAnswers = {};
                bookmarks = {};
                localStorage.removeItem(STORAGE_KEY_USER_ANSWERS);
                localStorage.removeItem(STORAGE_KEY_BOOKMARKS);
                initApp();
            }
        });

        // Key to option label mapping: 1->A, 2->B, 3->C, 4->D
        const keyToLabelMap = {
            '1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E',
            'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E'
        };

        // Keyboard shortcuts listener: 1=A, 2=B, 3=C, 4=D, Arrow keys navigation
        document.addEventListener('keydown', (e) => {
            if (document.activeElement && (document.activeElement.tagName === 'INPUT' || document.activeElement.tagName === 'TEXTAREA')) {
                return;
            }

            const key = e.key;

            if (key === 'ArrowLeft' || key === 'ArrowUp') {
                e.preventDefault();
                prevBtn.click();
            } else if (key === 'ArrowRight' || key === 'ArrowDown') {
                e.preventDefault();
                nextBtn.click();
            } else if (keyToLabelMap[key.toLowerCase()]) {
                const label = keyToLabelMap[key.toLowerCase()];
                const q = questions[currentIndex];
                const hasOption = q && q.options && q.options.some(o => o.label === label);
                if (hasOption && !userAnswers[q.id]) {
                    e.preventDefault();
                    handleSelectOption(q, label);
                }
            }
        });

        // Launch App
        initApp();
    </script>
</body>
</html>
"""

final_html = html_template.replace("__DATASET_PLACEHOLDER__", json_str)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

with open('triet_1100_cau_trac_nghiem_standalone.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Applied keyboard shortcuts to index.html and standalone file successfully!")
