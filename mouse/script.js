function documentMouseMoveHandler(event) {
    mouseX = event.clientX - (window.innerWidth - SCREEN_WIDTH) * .5;
    mouseY = event.clientY - (window.innerHeight - SCREEN_HEIGHT) * .5;
}
function createParticles() {
    particles = [];
    for (var i = 0; i < QUANTITY; i++) {
        var particle = {
            size: 1,
            position: {
                x: mouseX,
                y: mouseY
            },
            offset: {
                x: 0,
                y: 0
            },
            shift: {
                x: mouseX,
                y: mouseY
            },
            speed: 0.01 + Math.random() * 0.04,
            targetSize: 1,
            fillColor: '#' + (Math.random() * 0x404040 + 0xaaaaaa | 0).toString(16),
            orbit: RADIUS * .5 + (RADIUS * .5 * Math.random())
        };
        particles.push(particle);
    }
}
