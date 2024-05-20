window.onload=function(){
    const chatbox = document.getElementById("chat");
    const messageinput = document.getElementById("messageInput");
    const sendbutton = document.getElementById("sendButton");
    const loader = document.createElement("span");

    loader.classList.add("loader");

    sendbutton.addEventListener("click", async () => {
        const userMsg = messageinput.value.trim();
        if (!userMsg) return;

        const userMsgElement = document.createElement("div");
        userMsgElement.textContent = userMsg;
        userMsgElement.classList.add("message", "user-message");
        chatbox.appendChild(userMsgElement);

        messageinput.value = '';

        chatbox.appendChild(loader);

        try {
            const response = await fetch(`http://127.0.0.1:5000/get_answer?q=${userMsg}`);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();

            chatbox.removeChild(loader);

            const serverMsgElement = document.createElement("div");
            serverMsgElement.textContent = data.msg;
            serverMsgElement.classList.add("message", "server-message");
            chatbox.appendChild(serverMsgElement);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    });
}

