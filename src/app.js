var path = require('path');
var express = require('express');
var compression = require('compression');
var favicon = require('serve-favicon');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
var session = require('express-session');
var passport = require('passport');
var FacebookStrategy = require('passport-facebook').Strategy;

var Account = require('./models/Account.js');

var dbURL = process.env.MONGOLAB_URI || "mongodb://localhost/BrickHacks2016";

var db = mongoose.connect(dbURL, function(err){
  if(err){
    console.log("Could not connect to database");
    throw err;
  }
});

var router = require('./router.js');
var port = process.env.PORT || process.env.NODE_PORT || 3000;
var app = express();
app.use('/assets', express.static(path.resolve(__dirname + '../../client/')));
app.use(compression());
app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(session({
  key: "Sessionid",
  secret: "FeedYoCrew",
  resave: true,
  saveUninitialized: true
}));
app.set('view engine', 'jade');
app.set('views', __dirname + '/views');
app.set(favicon(__dirname + '/../client/img/favicon.png'));
app.use(cookieParser());
app.use(passport.initialize());
app.use(passport.session());

passport.serializeUser(function(userAccount, done){
  done(null, userAccount);
});
passport.deserializeUser(function(obj,done){
  done(null, obj);
});

passport.use(new FacebookStrategy({
  clientID: '1577600392565490',
  clientSecret: 'f1828c4a64f769c352e71cde1f28ced5',
  callbackURL: 'http://127.0.0.1:3000/auth/facebook/callback'
},
  function(accessToken, refreshToken, userAccount, done){
    Account.AccountModel.findOne({FacebookUID: userAccount.id }, function(err, userAccount){
      if(err){
        throw err;
      }
      if(!err && usert !== null){
        done(null,userAccount);
      }
    });
  }));

router(app, passport);

app.listen(port, function(err){
  if(err){
    throw err;
  }
  console.log('Listening on port ' + port);
});
