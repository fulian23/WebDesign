// 使用防抖函数优化性能
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// 创建鼠标跟随线条
const createLines = () => {
    const numSpans = 20;
    const spans = [];
    const fragment = document.createDocumentFragment();
    
    for (let i = 0; i < numSpans; i++) {
        const span = document.createElement('span');
        span.className = 'line';
        fragment.appendChild(span);
        spans.push(span);
    }
    
    document.body.appendChild(fragment);
    return spans;
};

// 更新线条位置
const updateLines = (spans, mouseX, mouseY) => {
    spans.forEach((span, index) => {
        const delay = Math.random() * 500;
        setTimeout(() => {
            requestAnimationFrame(() => {
                span.style.transform = `translate(${mouseX + 30}px, ${mouseY + index * 2}px)`;
            });
        }, delay);
    });
};

// 初始屏幕动画
const initInitialScreen = () => {
    const initialScreen = document.getElementById('initialScreen');
    const siteTitle = document.querySelector('.site-title');
    const initialTitle = document.querySelector('.initial-title');
    
    // 点击事件处理
    const handleClick = () => {
        // 获取初始标题和目标标题的位置信息
        const initialRect = initialTitle.getBoundingClientRect();
        const targetRect = siteTitle.getBoundingClientRect();
        
        // 计算缩放比例和位移
        const scaleX = targetRect.width / initialRect.width;
        const scaleY = targetRect.height / initialRect.height;
        const translateX = targetRect.left - initialRect.left;
        const translateY = targetRect.top - initialRect.top;
        
        // 添加动画类
        initialScreen.classList.add('fade-out');
        initialTitle.style.transform = `scale(${scaleX}) translate(${translateX}px, ${translateY}px)`;
        
        // 延迟显示目标标题
        setTimeout(() => {
            initialScreen.style.display = 'none';
            siteTitle.classList.add('visible');
        }, 1500);
        
        // 移除点击事件监听器
        document.removeEventListener('click', handleClick);
    };
    
    // 添加点击事件监听
    document.addEventListener('click', handleClick);
};

// 初始化
const init = () => {
    initInitialScreen();
    const spans = createLines();
    let lastMouseX = 0;
    let lastMouseY = 0;
    let isAnimating = false;
    
    // 使用防抖处理鼠标移动事件
    const handleMouseMove = debounce((event) => {
        if (isAnimating) return;
        
        const { clientX, clientY } = event;
        
        // 只在鼠标位置变化较大时更新
        if (Math.abs(clientX - lastMouseX) > 5 || Math.abs(clientY - lastMouseY) > 5) {
            isAnimating = true;
            lastMouseX = clientX;
            lastMouseY = clientY;
            
            requestAnimationFrame(() => {
                updateLines(spans, clientX, clientY);
                isAnimating = false;
            });
        }
    }, 16); // 约60fps
    
    document.addEventListener('mousemove', handleMouseMove);
    
    // 清理函数
    return () => {
        document.removeEventListener('mousemove', handleMouseMove);
        spans.forEach(span => {
            if (span.parentNode) {
                span.parentNode.removeChild(span);
            }
        });
    };
};

// 页面加载完成后初始化
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}

document.addEventListener('DOMContentLoaded', function() {
    // 初始屏幕淡出效果
    const initialScreen = document.getElementById('initialScreen');
    const siteTitle = document.querySelector('.site-title');
    
    setTimeout(() => {
        initialScreen.classList.add('fade-out');
        siteTitle.classList.add('visible');
        
        setTimeout(() => {
            initialScreen.style.display = 'none';
        }, 1500);
    }, 1000);

    // 导航栏滚动效果
    const navbar = document.querySelector('.navbar');
    let lastScrollTop = 0;

    window.addEventListener('scroll', function() {
        let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        
        if (scrollTop > lastScrollTop) {
            // 向下滚动
            navbar.style.transform = 'translateY(-100%)';
        } else {
            // 向上滚动
            navbar.style.transform = 'translateY(0)';
        }
        
        lastScrollTop = scrollTop;
    });

    // 平滑滚动
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
}); 