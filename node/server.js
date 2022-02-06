const express = require('express');
const app = express();
const http = require('http');

const PORT = 3333;

app.use(express.json({ limit: "50mb" }));
app.use(express.urlencoded({ limit: "50mb", extended: true }));

app.use('/api/user', require('./routes/user'));
app.use("/api/article", require("./routes/article"));
const server = http.createServer(app);
server.listen(PORT  , () => {})