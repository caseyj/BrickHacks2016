var http = require('http');
var fs = require('fs');
var socketio = require('socket.io');
var indexPort = process.env.PORT || process.env.NODE_PORT || 3011;
var index = fs.readFileSync(__dirname + '/../client/index.html');

var server = http.createServer(function(request, response)
  response.writeHead(200, {"Content-type" : "text/html"});
  response.write(index);
  response.end();
}
/*
var server = http.createServer(function(request, response) {
  var filePath = false;
  if (request.url == '/') {
    filePath = __dirname + '/../client/index.html';
  } else {
    filePath = __dirname + '/../client/' + request.url;
  }

  var absPath = "./" + filePath;
  serverWorking(response, absPath);
});

function serverWorking(response, absPath){
  fs.exists(absPath, function(exists){
    if(exists) {
      fs.readFile(absPath, function(error, data){
        if(error){
          send404(response);
        } else {
          sendPage(response, absPath, data);
        }
      });
    } else {
      send404(response);
    }
  });
}

function sendPage(response, filePath, fileContents) {
  console.log("Sendpage");
  response.writeHead(200, {"Content-type" : mime.lookup(path.basename(filePath))});
  response.write( mime.lookup(path.basename(filePath)));
  response.end(fileContents);
}

function send404(response) {
  console.log("Send404");
  response.writeHead(404, {"Content-type" : "text/plain"});
  response.write("Error 404: resource not found");
  response.end();
}
*/

var io = socketio(server);
var users = [];

io.sockets.on('connection', function(socket){
	socket.join('main'); // There's only one room
  socket.on('loginToServer', function(data){
    var userNotLoggedIntoServer = true;
    for(var i = 0; i < users.length; i++){
      if(users[i] == data){
        userNotLoggedIntoServer = true;
      }
    }
    if(!userNotLoggedIntoServer){
      users.push(data);
    }
    console.log(users);
  });
});
