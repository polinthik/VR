
    function glitchNumber(element, newValue, suffix = '') {
        let iterations = 0;
        const interval = setInterval(() => {
            if (iterations < 6) {
                const fakeVal = Math.floor(Math.random() * 9999);
                element.innerText = fakeVal + (suffix ? suffix : '');
                iterations++;
            } else {
                clearInterval(interval);
                element.innerText = newValue + (suffix ? suffix : '');
            }
        }, 60);
    }

    glitchNumber(nodeSpan, newNodes, '');
    glitchNumber(threatSpan, newThreat, '%');
    
    // Глитч-эффект на body
    document.body.style.transform = 'skew(0.5deg, 0.2deg)';
    setTimeout(() => { document.body.style.transform = ''; }, 150);


// Открыть модальное окно
function openModal() {
    modal.style.display = 'flex';
    const modalContent = modal.querySelector('.modal-content');
    modalContent.style.transform = 'translateX(2px)';
    setTimeout(() => { modalContent.style.transform = ''; }, 100);
    if (navigator.vibrate) navigator.vibrate(50);


// Закрыть модальное окно
function closeModal() {
    modal.style.display = 'none';
}

// Обработчики событий
hackButton.addEventListener('click', () => {
    cyberHackEffect();
    setTimeout(() => {
        openModal();
    }, 600);
});

closeModalBtn.addEventListener('click', closeModal);
modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
});

// Обратный отсчет
function updateCountdown() {
    const countdownElem = document.getElementById('countdownMessage');
    if (!countdownElem) return;
    
    const now = new Date();
    const target = new Date();
    target.setMinutes(target.getMinutes() + 15);
    target.setSeconds(target.getSeconds() + 30);
    
    let diff = target - now;
    if (diff < 0) {
        const resetTarget = new Date();
        resetTarget.setSeconds(resetTarget.getSeconds() + 900);
        diff = resetTarget - now;
    }
    
    const minutes = Math.floor(diff / 60000);
    const seconds = Math.floor((diff % 60000) / 1000);
    countdownElem.innerHTML = `<i class="fas fa-hourglass-half"></i> До сброса протокола: ${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

updateCountdown();
setInterval(updateCountdown, 1000);

// Динамическое изменение статистики угрозы
setInterval(() => {
    const threatSpan = document.getElementById('threatLvl');
    if (threatSpan && !hackButton.disabled) {
        let current = parseInt(threatSpan.innerText);
        if (isNaN(current)) current = 70;
        let delta = (Math.random() - 0.5) * 8;
        let newThreat = Math.min(99, Math.max(20, Math.floor(current + delta)));
        threatSpan.innerText = newThreat + '%';
        
        threatSpan.style.textShadow = '0 0 6px magenta';
        setTimeout(() => { threatSpan.style.textShadow = ''; }, 200);
    }
}, 5000);

// Анимированный глитч на заголовке при движении мыши
const neonTitle = document.querySelector('.neon-title');
if (neonTitle) {
    document.addEventListener('mousemove', (e) => {
        let x = (e.clientX / window.innerWidth) * 4 - 2;
        let y = (e.clientY / window.innerHeight) * 2 - 1;
        neonTitle.style.transform = `translate(${x * 0.8}px, ${y * 0.5}px)`;
    });
}

// Эффект свечения для карточек при скролле
const cards = document.querySelectorAll('.cyber-card');
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.transition = '0.3s';
            entry.target.style.boxShadow = '0 0 25px rgba(0,255,255,0.6)';
            setTimeout(() => {
                entry.target.style.boxShadow = '';
            }, 500);
        }
    });
}, { threshold: 0.2 });

cards.forEach(c => observer.observe(c));
const initHash = '0x' + Math.floor(Math.random() * 65535).toString(16).toUpperCase();
document.getElementById('netHash').innerText = initHash;
}