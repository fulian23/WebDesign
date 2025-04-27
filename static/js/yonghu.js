// 初始化Three.js场景
let scene, camera, renderer, particles;

function init() {
    // 创建场景
    scene = new THREE.Scene();

    // 创建相机
    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    camera.position.z = 5;

    // 创建渲染器
    renderer = new THREE.WebGLRenderer({
        canvas: document.querySelector('#bg'),
        antialias: true
    });
    renderer.setPixelRatio(window.devicePixelRatio);
    renderer.setSize(window.innerWidth, window.innerHeight);
    camera.position.setZ(30);

    // 创建粒子系统
    const particlesGeometry = new THREE.BufferGeometry();
    const particlesCount = 5000;
    const posArray = new Float32Array(particlesCount * 3);

    for(let i = 0; i < particlesCount * 3; i++) {
        posArray[i] = (Math.random() - 0.5) * 5;
    }

    particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));

    const particlesMaterial = new THREE.PointsMaterial({
        size: 0.005,
        color: '#ffffff'
    });

    particles = new THREE.Points(particlesGeometry, particlesMaterial);
    scene.add(particles);

    // 添加环境光
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);

    // 添加点光源
    const pointLight = new THREE.PointLight(0xffffff, 1);
    pointLight.position.set(25, 25, 25);
    scene.add(pointLight);

    // 开始动画循环
    animate();
}

// 动画循环
function animate() {
    requestAnimationFrame(animate);

    particles.rotation.x += 0.0001;
    particles.rotation.y += 0.0001;

    renderer.render(scene, camera);
}

// 窗口大小改变时调整渲染器大小
window.addEventListener('resize', onWindowResize, false);

function onWindowResize() {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
}

// 初始化场景
init();

// DOM元素
const editUsernameBtn = document.getElementById('edit-username');
const usernameEdit = document.querySelector('.username-edit');
const usernameInput = document.getElementById('username-input');
const confirmUsernameBtn = document.getElementById('confirm-username');
const cancelUsernameBtn = document.getElementById('cancel-username');
const currentUsername = document.getElementById('current-username');
const changePasswordBtn = document.getElementById('change-password');
const newPasswordInput = document.getElementById('new-password');
const togglePasswordBtn = document.querySelector('.toggle-password');
const avatarUpload = document.getElementById('avatar-upload');
const currentAvatar = document.getElementById('current-avatar');
const saveBtn = document.querySelector('[data-action="save"]');
const resetBtn = document.querySelector('[data-action="reset"]');

// 用户名编辑功能
editUsernameBtn.addEventListener('click', () => {
    usernameEdit.classList.remove('hidden');
    usernameInput.value = currentUsername.textContent;
    usernameInput.focus();
});

confirmUsernameBtn.addEventListener('click', () => {
    const newUsername = usernameInput.value.trim();
    if (newUsername) {
        currentUsername.textContent = newUsername;
        usernameEdit.classList.add('hidden');
        showNotification('用户名已更新', 'success');
    } else {
        showNotification('用户名不能为空', 'error');
    }
});

cancelUsernameBtn.addEventListener('click', () => {
    usernameEdit.classList.add('hidden');
});

// 密码修改功能
changePasswordBtn.addEventListener('click', () => {
    const newPassword = newPasswordInput.value.trim();
    if (newPassword) {
        // 这里应该添加密码验证和更新逻辑
        showNotification('密码已更新', 'success');
        newPasswordInput.value = '';
    } else {
        showNotification('密码不能为空', 'error');
    }
});

// 密码显示切换
togglePasswordBtn.addEventListener('click', () => {
    const type = newPasswordInput.type === 'password' ? 'text' : 'password';
    newPasswordInput.type = type;
    togglePasswordBtn.textContent = type === 'password' ? '👁️' : '👁️‍🗨️';
});

// 头像上传功能
avatarUpload.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            currentAvatar.src = e.target.result;
            showNotification('头像已更新', 'success');
        };
        reader.readAsDataURL(file);
    }
});

// 保存更改
saveBtn.addEventListener('click', () => {
    // 这里应该添加保存到后端的逻辑
    showNotification('更改已保存', 'success');
});

// 重置更改
resetBtn.addEventListener('click', () => {
    usernameInput.value = currentUsername.textContent;
    newPasswordInput.value = '';
    usernameEdit.classList.add('hidden');
    showNotification('已重置所有更改', 'info');
});

// 通知系统
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = 'notification';
    
    const icon = document.createElement('span');
    icon.className = 'notification-icon';
    switch(type) {
        case 'success':
            icon.textContent = '✅';
            break;
        case 'error':
            icon.textContent = '❌';
            break;
        case 'warning':
            icon.textContent = '⚠️';
            break;
        default:
            icon.textContent = 'ℹ️';
    }
    
    const text = document.createElement('span');
    text.textContent = message;
    
    notification.appendChild(icon);
    notification.appendChild(text);
    
    document.getElementById('notification-container').appendChild(notification);
    
    setTimeout(() => {
        notification.style.opacity = '0';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 3000);
} 