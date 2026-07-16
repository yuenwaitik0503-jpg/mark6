import streamlit as st
import streamlit.components.v1 as components

st.title("攪珠動畫模擬器")

# 將 HTML, CSS, JS 全部包在一起
html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; display: flex; flex-direction: column; align-items: center; background: #1a1a1a; color: white; }
        #canvas-container { width: 500px; height: 500px; border-radius: 50%; border: 8px solid #444; background: #222; margin-top: 20px; }
        .controls { margin-top: 20px; }
    </style>
</head>
<body>
    <div id="canvas-container"></div>
    <div class="controls">
        <button id="btn-mix">開始攪珠</button>
        <button id="btn-draw">抽取號碼</button>
        <button id="btn-reset">重設</button>
    </div>
    <div id="drawn-container"></div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/matter-js/0.19.0/matter.min.js"></script>
    <script>
        // 確保 DOM 載入後才執行 Matter.js
        const { Engine, Render, Runner, Bodies, Composite } = Matter;
        const container = document.getElementById('canvas-container');
        
        const engine = Engine.create();
        const render = Render.create({
            element: container,
            engine: engine,
            options: { width: 500, height: 500, wireframes: false, background: 'transparent' }
        });

        // 建立邊界與球的邏輯... (請放入之前完整的那段 JS 程式碼)
        Render.run(render);
        Runner.run(Runner.create(), engine);
    </script>
</body>
</html>
"""

# 增加高度設定，讓 iframe 有空間顯示 canvas
components.html(html_code, height=700, width=600)
