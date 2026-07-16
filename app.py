import streamlit as st
import streamlit.components.v1 as components

st.title("攪珠動畫模擬器")

# 使用三重引號確保內容被視為完整的字串
html_code = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; display: flex; flex-direction: column; align-items: center; background: #1a1a1a; color: white; font-family: sans-serif; }
        #canvas-container { width: 500px; height: 500px; border-radius: 50%; border: 8px solid #444; background: #222; margin-top: 20px; }
        .controls { margin-top: 20px; display: flex; gap: 10px; }
        button { padding: 10px 20px; cursor: pointer; font-weight: bold; }
    </style>
</head>
<body>
    <div id="canvas-container"></div>
    <div class="controls">
        <button id="btn-mix">開始攪珠</button>
        <button id="btn-draw">抽取號碼</button>
        <button id="btn-reset">重設</button>
    </div>
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/matter-js/0.19.0/matter.min.js"></script>
    <script>
        window.onload = () => {
            const { Engine, Render, Runner, Bodies, Composite, Body } = Matter;
            const container = document.getElementById('canvas-container');
            const engine = Engine.create({ gravity: { y: 1 } });
            
            const render = Render.create({
                element: container,
                engine: engine,
                options: { width: 500, height: 500, wireframes: false, background: 'transparent' }
            });

            // 建立邊界
            const walls = [];
            for (let i = 0; i < 120; i++) {
                const angle = (i / 120) * Math.PI * 2;
                const x = 250 + Math.cos(angle) * 240;
                const y = 250 + Math.sin(angle) * 240;
                walls.push(Bodies.rectangle(x, y, 20, 40, { isStatic: true, angle: angle, render: { visible: false } }));
            }
            Composite.add(engine.world, walls);

            // 建立球體
            const balls = [];
            const createBalls = () => {
                balls.forEach(b => Composite.remove(engine.world, b));
                balls.length = 0;
                for (let i = 1; i <= 20; i++) {
                    const b = Bodies.circle(250 + Math.random()*100 - 50, 250 + Math.random()*100 - 50, 16, {
                        restitution: 0.9,
                        render: { fillStyle: '#ff3b30' }
                    });
                    balls.push(b);
                }
                Composite.add(engine.world, balls);
            };
            createBalls();

            // 強力攪動：加大力道
            document.getElementById('btn-mix').onclick = () => {
                let count = 0;
                let mixInterval = setInterval(() => {
                    balls.forEach(b => {
                        Body.applyForce(b, b.position, { x: (Math.random()-0.5)*0.5, y: (Math.random()-0.5)*0.5 });
                    });
                    if (++count > 40) clearInterval(mixInterval);
                }, 50);
            };

            // 抽取號碼
            document.getElementById('btn-draw').onclick = () => {
                if (balls.length > 0) {
                    const idx = Math.floor(Math.random() * balls.length);
                    const chosen = balls[idx];
                    chosen.render.fillStyle = '#ffff00'; // 變黃色
                    alert("抽中球號：" + (idx + 1));
                    
                    setTimeout(() => {
                        Composite.remove(engine.world, chosen);
                        balls.splice(idx, 1);
                    }, 500);
                }
            };

            document.getElementById('btn-reset').onclick = createBalls;

            Render.run(render);
            Runner.run(Runner.create(), engine);
        };
    </script>
</body>
</html>
"""

components.html(html_code, height=700)
