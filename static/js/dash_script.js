// 3D背景设置
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({
    canvas: document.querySelector('#bg'),
    antialias: true,
    alpha: true
});

renderer.setPixelRatio(window.devicePixelRatio);
renderer.setSize(window.innerWidth, window.innerHeight);
camera.position.setZ(30);

// 创建粒子系统
const particlesGeometry = new THREE.BufferGeometry();
const particlesCount = 5000;
const posArray = new Float32Array(particlesCount * 3);

for(let i = 0; i < particlesCount * 3; i++) {
    posArray[i] = (Math.random() - 0.5) * 100;
}

particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));

const particlesMaterial = new THREE.PointsMaterial({
    size: 0.05,
    color: '#000000',
    transparent: true,
    opacity: 0.8,
    blending: THREE.AdditiveBlending
});

const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
scene.add(particlesMesh);

// 动画循环
function animate() {
    requestAnimationFrame(animate);
    particlesMesh.rotation.y += 0.0005;
    particlesMesh.rotation.x += 0.0002;
    renderer.render(scene, camera);
}

animate();

// 窗口大小调整
window.addEventListener('resize', () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
});

// 用户交互功能
document.addEventListener('DOMContentLoaded', () => {
    // 创建走动的小人和气泡容器
    const container = document.createElement('div');
    container.className = 'walking-container';
    
    const walkingMan = document.createElement('div');
    walkingMan.className = 'walking-man';
    walkingMan.innerHTML = `
        <img src="../static/image/ren.jpg" alt="walking character">
    `;

    const speechBubble = document.createElement('div');
    speechBubble.className = 'speech-bubble';
    speechBubble.textContent = '欢迎访问我们的网站';

    container.appendChild(walkingMan);
    container.appendChild(speechBubble);
    document.body.appendChild(container);

    // 监听动画进度，在中间位置显示气泡
    let bubbleShown = false;
    walkingMan.addEventListener('animationiteration', () => {
        bubbleShown = false;
    });

    function checkPosition() {
        const rect = walkingMan.getBoundingClientRect();
        const centerX = window.innerWidth / 2;
        const manCenterX = rect.left + rect.width / 2;
        
        if (Math.abs(manCenterX - centerX) < 50 && !bubbleShown) {
            speechBubble.classList.add('show-bubble');
            bubbleShown = true;
        } else if (Math.abs(manCenterX - centerX) >= 50) {
            speechBubble.classList.remove('show-bubble');
        }
    }

    // 持续检查位置
    setInterval(checkPosition, 100);

    // 元素获取
    const editUsernameBtn = document.getElementById('edit-username');
    const usernameInput = document.getElementById('username-input');
    const confirmUsernameBtn = document.getElementById('confirm-username');
    const cancelUsernameBtn = document.getElementById('cancel-username');
    const currentUsername = document.getElementById('current-username');
    const usernameEdit = document.querySelector('.username-edit');
    const avatarUpload = document.getElementById('avatar-upload');
    const currentAvatar = document.getElementById('current-avatar');
    const passwordInput = document.getElementById('new-password');
    const togglePasswordBtn = document.querySelector('.toggle-password');
    const changePasswordBtn = document.getElementById('change-password');

    // 用户名编辑
    editUsernameBtn.addEventListener('click', () => {
        usernameEdit.classList.remove('hidden');
        usernameInput.value = currentUsername.textContent;
        usernameInput.focus();
    });
    cancelUsernameBtn.addEventListener('click', () => {
        usernameEdit.classList.add('hidden');
    });




    // 密码可见性切换
    togglePasswordBtn.addEventListener('click', () => {
        const type = passwordInput.type === 'password' ? 'text' : 'password';
        passwordInput.type = type;
        togglePasswordBtn.textContent = type === 'password' ? '👁️' : '👁️‍🗨️';
    });


});

// 通知系统
function showNotification(message, type = 'success') {
    const container = document.getElementById('notification-container');
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;

    container.appendChild(notification);

    // 动画效果
    notification.style.animation = 'slideIn 0.3s ease forwards';

    // 3秒后移除通知
    setTimeout(() => {
        notification.style.animation = 'slideIn 0.3s ease reverse';
        setTimeout(() => {
            container.removeChild(notification);
        }, 300);
    }, 3000);
}

// 鼠标移动视差效果
document.addEventListener('mousemove', (e) => {
    const mouseX = e.clientX / window.innerWidth - 0.5;
    const mouseY = e.clientY / window.innerHeight - 0.5;

    particlesMesh.rotation.y = mouseX * 0.3;
    particlesMesh.rotation.x = mouseY * 0.3;
}); 