console.log('it is me')

const socket = new WebSocket('ws://' + window.location.host + '/ws/notification/');

socket.onmessage = function(e){
    console.log('server ': + e.data);
};

socket.onopen = function(e){
    socket.send(JSON.stringify({
        'message': 'hello world',
    }));
};