let tasks = [];
let screenTimeMinutes = 0;

// Dynamic starry night background
const starCanvas = document.createElement('canvas');
document.body.appendChild(starCanvas);
starCanvas.style.position = 'fixed';
starCanvas.style.top = 0;
starCanvas.style.left = 0;
starCanvas.style.zIndex = -1;
starCanvas.width = window.innerWidth;
starCanvas.height = window.innerHeight;
const ctxBg = starCanvas.getContext('2d');

const stars = Array.from({ length: 500 }, () => ({
  x: Math.random() * starCanvas.width,
  y: Math.random() * starCanvas.height,
  radius: Math.random() * 1.5,
  alpha: Math.random(),
  delta: 0.005 + Math.random() * 0.015
}));

let meteors = [];
function spawnMeteor() {
  meteors.push({
    x: Math.random() * starCanvas.width,
    y: 0,
    dx: 2 + Math.random() * 2,
    dy: 4 + Math.random() * 2,
    length: 80 + Math.random() * 40,
    trail: 10
  });
  const nextMeteorDelay = 5000 + Math.random() * 5000;
  setTimeout(spawnMeteor, nextMeteorDelay);
}

function animateStars() {
  ctxBg.clearRect(0, 0, starCanvas.width, starCanvas.height);
  ctxBg.fillStyle = 'black';
  ctxBg.fillRect(0, 0, starCanvas.width, starCanvas.height);

  stars.forEach(star => {
    star.alpha += star.delta;
    if (star.alpha <= 0 || star.alpha >= 1) star.delta = -star.delta;
    ctxBg.beginPath();
    ctxBg.arc(star.x, star.y, star.radius, 0, 2 * Math.PI);
    ctxBg.fillStyle = `rgba(255, 255, 255, ${star.alpha})`;
    ctxBg.fill();
  });

  // Draw meteors with fading trail
  meteors.forEach((meteor, index) => {
    for (let i = 0; i < meteor.trail; i++) {
      let trailX = meteor.x - (meteor.dx * i);
      let trailY = meteor.y - (meteor.dy * i);
      let alpha = 1 - i / meteor.trail;
      ctxBg.beginPath();
      ctxBg.moveTo(trailX, trailY);
      ctxBg.lineTo(trailX - 2, trailY - 2);
      ctxBg.strokeStyle = `rgba(255, 255, 255, ${alpha})`;
      ctxBg.lineWidth = 2;
      ctxBg.stroke();
    }

    meteor.x += meteor.dx;
    meteor.y += meteor.dy;
    if (meteor.x > starCanvas.width || meteor.y > starCanvas.height) {
      meteors.splice(index, 1);
    }
  });

  requestAnimationFrame(animateStars);
}
spawnMeteor();
animateStars();



function addTask() {
  let taskInput = document.getElementById('taskInput');
  if (taskInput.value.trim() === '') {
    alert("Please enter a task name!");
    return;
  }

  tasks.push({name: taskInput.value, completed: false, timeSpent: 0, timer: null, startTime: null});
  taskInput.value = '';
  updateTaskList();
  updateChart();
}

function toggleComplete(index) {
  tasks[index].completed = !tasks[index].completed;
  updateTaskList();
}

function removeTask(index) {
  if (tasks[index].timer) {
    clearInterval(tasks[index].timer);
  }
  tasks.splice(index, 1);
  updateTaskList();
  updateChart();
}

function updateTaskList() {
  let taskList = document.getElementById('taskList');
  taskList.innerHTML = '';

  tasks.forEach((task, index) => {
    let taskItem = document.createElement('li');

    taskItem.innerHTML = `
      <span class="${task.completed ? 'complete' : ''}">${task.name} (${Math.floor(task.timeSpent/60)}m ${task.timeSpent%60}s)</span>
      <div>
        <button onclick="toggleComplete(${index})">✔️</button>
        <button onclick="startTimer(${index})">▶️</button>
        <button onclick="stopTimer(${index})">⏹️</button>
        <button onclick="removeTask(${index})">❌</button>
      </div>
    `;

    taskList.appendChild(taskItem);
  });

  // Screen time input
  let screenInput = document.createElement('div');
  screenInput.innerHTML = `
    <label>Screen Time (min): </label>
    <input type="number" id="screenTimeInput" value="${screenTimeMinutes}" min="0" onchange="updateScreenTime(this.value)">
  `;
  taskList.appendChild(screenInput);
}

function updateScreenTime(value) {
  screenTimeMinutes = parseInt(value) || 0;
  updateChart();
}

function startTimer(index) {
  if(tasks[index].timer) return; // Prevent multiple timers

  tasks[index].startTime = Date.now();

  tasks[index].timer = setInterval(() => {
    let elapsed = Math.floor((Date.now() - tasks[index].startTime) / 1000);
    tasks[index].timeSpent += elapsed;
    tasks[index].startTime = Date.now();
    updateTaskList();
    updateChart();
  }, 1000);
}

function stopTimer(index) {
  clearInterval(tasks[index].timer);
  tasks[index].timer = null;
  tasks[index].startTime = null;
  updateTaskList();
  updateChart();
}

// Chart.js Visualization
let ctx = document.getElementById('taskChart').getContext('2d');
let taskChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: [],
    datasets: [{
      label: 'Minutes Spent per Task',
      data: [],
      backgroundColor: '#007bff'
    }]
  },
  options: {
    responsive: true,
    scales: { 
      y: { beginAtZero: true, max: 5 }
    }
  }
});

function updateChart() {
  const taskTimes = tasks.map(task => Math.round(task.timeSpent / 60));
  const labels = tasks.map(task => task.name);
  const data = [...taskTimes];

  labels.push("Screen Time");
  data.push(screenTimeMinutes);

  taskChart.data.labels = labels;
  taskChart.data.datasets[0].data = data;

  // Dynamic scaling
  let currentMax = Math.max(...data, 5);
  if (currentMax >= taskChart.options.scales.y.max) {
    taskChart.options.scales.y.max = Math.ceil(currentMax * 1.1);
  }

  taskChart.update();
}