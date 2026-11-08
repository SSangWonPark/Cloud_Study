from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# 아주 단순한 서버 저장 상태 (실제로 Flask 프로세스가 "동적"으로 뭔가를 기억한다는 걸 보여주기 위함)
click_count = 0

PAGE = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Interactive Particles - SangWon's EC2 App</title>
<style>
  body { margin:0; background:#111; overflow:hidden; font-family: sans-serif; color:#eee; }
  #info { position:absolute; top:16px; left:16px; z-index:10; }
  #info h2 { margin:0 0 4px 0; font-size:18px; }
  #info p { margin:0; font-size:14px; color:#aaa; }
  canvas { display:block; cursor: pointer; }
</style>
</head>
<body>
<div id="info">
  <h2>클릭해서 파티클 터뜨리기</h2>
  <p>전체 클릭 수 (Flask 서버에 저장됨): <span id="count">0</span></p>
</div>
<canvas id="canvas"></canvas>
<script>
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

let particles = [];

function spawnBurst(x, y) {
  for (let i = 0; i < 40; i++) {
    const angle = Math.random() * Math.PI * 2;
    const speed = Math.random() * 5 + 2;
    particles.push({
      x, y,
      vx: Math.cos(angle) * speed,
      vy: Math.sin(angle) * speed,
      life: 60,
      color: `hsl(${Math.random() * 360}, 80%, 60%)`
    });
  }
}

function update() {
  ctx.fillStyle = 'rgba(17,17,17,0.2)';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  particles.forEach(p => {
    p.x += p.vx;
    p.y += p.vy;
    p.vy += 0.05;
    p.life -= 1;
    ctx.beginPath();
    ctx.arc(p.x, p.y, 3, 0, Math.PI * 2);
    ctx.fillStyle = p.color;
    ctx.fill();
  });
  particles = particles.filter(p => p.life > 0);
  requestAnimationFrame(update);
}
update();

canvas.addEventListener('click', async (e) => {
  spawnBurst(e.clientX, e.clientY);
  try {
    const res = await fetch('/api/click', { method: 'POST' });
    const data = await res.json();
    document.getElementById('count').innerText = data.total;
  } catch (err) {
    console.error(err);
  }
});

async function loadCount() {
  try {
    const res = await fetch('/api/stats');
    const data = await res.json();
    document.getElementById('count').innerText = data.total;
  } catch (err) {
    console.error(err);
  }
}
loadCount();

window.addEventListener('resize', () => {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
});
</script>
</body>
</html>
"""


@app.route('/')
def index():
    return render_template_string(PAGE)


@app.route('/api/click', methods=['POST'])
def click():
    global click_count
    click_count += 1
    return jsonify(total=click_count)


@app.route('/api/stats')
def stats():
    return jsonify(total=click_count)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
