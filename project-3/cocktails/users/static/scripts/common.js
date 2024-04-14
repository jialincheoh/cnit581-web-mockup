const nextBtn = document.getElementById('next-btn');
if (nextBtn) {
    nextBtn.addEventListener('click', () => {
        const targetUrl = nextBtn.dataset.target
        if (targetUrl) {
            window.location.href = targetUrl;
        }
    })
}
