const websocket = require("websocket");
const WebSocket = websocket.w3cwebsocket;

const ws = new WebSocket("ws://10.255.255.254:2026/api");
ws.onmessage = (event) => {
  console.log("server <- client: " + event.data);
};
ws.onopen = () => {
  console.log("connected");
  {
    const data = { source: "Artemis Station", msg: [1, 2, 3, 4] };
    console.log("client -> server: " + JSON.stringify(data));
    ws.send(JSON.stringify(data));
  }
};