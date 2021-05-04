function log(msg) {
    var element = document.getElementById('console');
    element.insertAdjacentHTML('beforeend', '<samp>' + msg + '</samp>');
}

async function pipeline() {
    log('Start');
}

log('Turned on!');

pipeline();