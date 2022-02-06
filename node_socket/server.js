const app = require("express")();
const http = require("http");
const ws = require('ws'); 
const PORT = 3335

const server = http.createServer(app);
const wss = new ws.Server({ server:server });


wss.on('connection', function (ws, req) {
  let clients = [];
  console.log("connection???");
  clients.push(ws);
  let ip = req.headers['x-forwarded-for'] || req.connection.remoteAddress;
  console.log(ip + "아이피의 클라이언트로 부터 접속 요청이 있었습니다.");
  
  const sendAll = (message) => {
    for (var i=0; i<clients.length; i++) {
      clients[i].send("Message: " + message);
    }
  }

  ws.on('message', function( message ){
    console.log( ip + "로 부터 받은 메시지 : " + message );
    ws.send("echo:" + message);
    sendAll(message);
  });
  ws.on('error', function(error){
    console.log( ip + "클라이언트와 연결중 오류 발생:" + error );
  })

  ws.on('close', function(){
    console.log( ip + "클라이언트와 접속이 끊어 졌습니다." );
  })
});

app.get("/", (req , res , next) => {
  res.redirect("http://willneedme.com");
})

server.listen(PORT, () => {
  console.log("socket listening");
})