import streamlit as st
import streamlit.components.v1 as components

st.title("攪珠動畫模擬器")

# 側邊欄：控制力道
force_strength = st.sidebar.slider("攪珠力度", 0.1, 2.0, 0.5, 0.1)

html_code = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{ margin: 0; display: flex; flex-direction: column; align-items: center; background: #1a1a1a; color: white; }}
        #canvas-container {{ width: 500px; height: 500px; border-radius: 50%; border: 8px solid #444; background: #222; }}
    </style>
</head>
<body>
    <div id="canvas-container"></div>
    <div style="margin-top:20px;">
        <button id="btn-mix">開始攪珠</button>
        <button id="btn-draw">抽取號碼</button>
        <button id="btn-reset">重設</button>
    </div>
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/matter-js/0.19.0/matter.min.js"></script>
    <script>
        const strength = {force_strength}; // 接收 Python 傳來的參數
        const {{ Engine, Render, Runner, Bodies, Composite, Body }} = Matter;
        const container = document.getElementById('canvas-container');
        const engine = Engine.create();
        
        // 提高物理引擎精確度以防止穿透
        engine.positionIterations = 10;
        engine.velocityIterations = 10;

        const render = Render.create({{
            element: container,
            engine: engine,
            options: {{ width: 500, height: 500, wireframes: false, background: 'transparent' }}
        }});

        // 加厚邊界：將邊界由薄變厚，並加強碰撞邊緣
        const walls = [];
        for (let i = 0; i < 60; i++) {{
            const angle = (i / 60) * Math.PI * 2;
            const x = 250 + Math.cos(angle) * 230;
            const y = 250 + Math.sin(angle) * 230;
            walls.push(Bodies.rectangle(x, y, 40, 40, {{ isStatic: true, render: {{ fillStyle: '#444' }} }}));
        }}
        Composite.add(engine.world, walls);

        const balls = [];
        const createBalls = () => {{
            balls.forEach(b => Composite.remove(engine.world, b));
            balls.length = 0;
            for (let i = 1; i <= 20; i++) {{
                const b = Bodies.circle(250, 250, 15, {{ 
                    restitution: 0.8, 
                    friction: 0.1,
                    render: {{ fillStyle: '#ff3b30' }} 
                }});
                balls.push(b);
            }}
            Composite.add(engine.world, balls);
        }};
        createBalls();

        document.getElementById('btn-mix').onclick = () => {{
            let count = 0;
            let interval = setInterval(() => {{
                balls.forEach(b => Body.applyForce(b, b.position, {{ 
                    x: (Math.random()-0.5) * strength, 
                    y: (Math.random()-0.5) * strength 
                }}));
                if (++count > 50) clearInterval(interval);
            }}, 50);
        }};

        document.getElementById('btn-draw').onclick = () => {{
            if (balls.length > 0) {{
                const b = balls.pop();
                b.render.fillStyle = '#ffff00';
                setTimeout(() => Composite.remove(engine.world, b), 300);
            }}
        }};

        document.getElementById('btn-reset').onclick = createBalls;

        Render.run(render);
        Runner.run(Runner.create(), engine);
    </script>
</body>
</html>
"""

components.html(html_code, height=600)
