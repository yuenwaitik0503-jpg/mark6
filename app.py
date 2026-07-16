<!DOCTYPE html>
<html>
<head>
    <style>
        body { margin: 0; display: flex; flex-direction: column; align-items: center; background: #1a1a1a; color: white; font-family: sans-serif; }
        #canvas-container { width: 500px; height: 500px; border-radius: 50%; border: 8px solid #444; background: #222; margin-top: 20px; }
        .controls { margin-top: 20px; display: flex; gap: 10px; }
        button { padding: 10px 20px; cursor: pointer; }
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
            const { Engine, Render, Runner, Bodies, Composite, Body, Events } = Matter;
            const container = document.getElementById('canvas-container');
            const engine = Engine.create({ gravity: { y: 1.2 } });
            
            const render = Render.create({
                element: container,
                engine: engine,
                options: { width: 500, height: 500, wireframes: false, background: 'transparent' }
            });

            // 建立封閉圓形邊界
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
                    const b = Bodies.circle(250 + Math.random()*50, 250 + Math.random()*50, 16, {
                        restitution: 0.8,
                        render: { fillStyle: '#ff3b30' }
                    });
                    balls.push(b);
                }
                Composite.add(engine.world, balls);
            };
            createBalls();

            // 攪動機制
            let mixInterval;
            document.getElementById('btn-mix').onclick = () => {
                mixInterval = setInterval(() => {
                    balls.forEach(b => Body.applyForce(b, b.position, { x: (Math.random()-0.5)*0.02, y: (Math.random()-0.5)*0.02 }));
                }, 50);
                setTimeout(() => clearInterval(mixInterval), 2000);
            };

            document.getElementById('btn-reset').onclick = createBalls;

            Render.run(render);
            Runner.run(Runner.create(), engine);
        };
    </script>
</body>
</html>
