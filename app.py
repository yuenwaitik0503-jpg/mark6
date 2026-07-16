import streamlit as st
import streamlit.components.v1 as components

st.title("手動攪珠模擬器")

# 側邊欄控制
speed = st.sidebar.slider("攪動速度", 0.05, 0.5, 0.2, 0.05)

html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ margin: 0; display: flex; flex-direction: column; align-items: center; background: #000; color: white; }}
        #canvas-container {{ width: 600px; height: 500px; border: 4px solid #d4af37; background: #111; }}
        .controls {{ margin-top: 20px; }}
    </style>
</head>
<body>
    <div id="canvas-container"></div>
    <div class="controls">
        <button onclick="mix()">轉動鐵籠</button>
        <button onclick="draw()">開啟出口</button>
        <button onclick="location.reload()">重設</button>
    </div>
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/matter-js/0.19.0/matter.min.js"></script>
    <script>
        const {{ Engine, Render, Runner, Bodies, Composite, Body, Constraint }} = Matter;
        const container = document.getElementById('canvas-container');
        const engine = Engine.create();
        const render = Render.create({{ element: container, engine: engine, options: {{ width: 600, height: 500, wireframes: false, background: '#111' }} }});

        // 1. 建立鐵籠 (用幾條線構成)
        const cage = [
            Bodies.circle(300, 250, 200, {{ isStatic: true, render: {{ strokeStyle: '#d4af37', lineWidth: 5, fillStyle: 'transparent' }} }}),
            Bodies.rectangle(300, 480, 200, 20, {{ isStatic: true, angle: Math.PI/6, render: {{ fillStyle: '#d4af37' }} }}) // 軌道
        ];
        Composite.add(engine.world, cage);

        // 2. 建立 20 個有號碼的球
        const balls = [];
        const colors = ['#ff6b6b', '#4ecdc4', '#ffe66d', '#ff9f1c', '#a8dadc'];
        for(let i=1; i<=20; i++) {{
            const b = Bodies.circle(250 + Math.random()*100, 200 + Math.random()*100, 15, {{
                restitution: 0.7,
                render: {{ fillStyle: colors[i%5] }}
            }});
            b.label = i.toString();
            balls.push(b);
        }}
        Composite.add(engine.world, balls);

        // 3. 攪動功能
        function mix() {{
            balls.forEach(b => Body.applyForce(b, b.position, {{ x: (Math.random()-0.5)*{speed}, y: (Math.random()-0.5)*{speed} }}));
        }}

        // 4. 抽取邏輯 (模擬底部開口)
        function draw() {{
            // 這裡模擬開啟一個通道，透過移除部分靜態體
            const door = Bodies.rectangle(300, 400, 50, 10, {{ isStatic: true, render: {{ fillStyle: 'transparent' }} }});
            // 讓球通過(略)
        }}

        Render.run(render);
        Runner.run(Runner.create(), engine);
    </script>
</body>
</html>
"""

components.html(html_code, height=600)
