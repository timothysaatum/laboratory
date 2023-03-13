//pop up login in form
//function openForm(){
//    document.getElementById("popup-form").style.display = 'block';
//}

const socket = new WebSocket('ws://localhost:8000/ws/database/');

socket.addEventListener('open', (event) => {
    console.log('WebSocket connected');
});

socket.addEventListener('message', (event) => {
    console.log('New database created:', event.data);
    // Update the UI to display the new database notification
});
