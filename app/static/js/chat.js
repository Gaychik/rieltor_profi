let ws= io();





function sendMessage()
{
   let msg_input = document.getElementById('msg');
   let chat = document.getElementById('chat');
   let current_msg = msg_input.value;
   ws.emit('send_msg', {
      message: current_msg, 
      id : document.getElementById('target_client').innerText, 
      chat_id: document.getElementById('chat_id').innerText}
   );
   msg_input.value='';
   let div_msg=document.createElement('div');
   let now = new Date();
   div_msg.innerHTML= `<p class="msg">${current_msg}</p> <p class="date-msg">${now.getHours()}:${now.getMinutes()}</p>`;
   chat.appendChild(div_msg);
}


ws.on('recv_msg',data =>
{
   let chat = document.getElementById('chat');
   let div_msg=document.createElement('div');
   let now = new Date();
   let current_msg=data["message"];
   div_msg.innerHTML= `<p class="msg">${current_msg}</p> <p class="date-msg">${now.getHours()}:${now.getMinutes()}</p>`;
   chat.appendChild(div_msg);
}
 );
