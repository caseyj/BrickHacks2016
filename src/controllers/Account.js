var models = require('../models');
var Account = models.Account;

var loginPage = function(req, res){
  res.render('login');
};

var login = function(req, res){
  res.redirect('userPage');
};

var logout = function(req, res){
  //res.session.destroy();
  req.logout();
  res.redirect('/');
};

var userPage = function(req, res){
  res.render('userPage')
};

module.exports.loginPage = loginPage;
module.exports.login = login;
module.exports.logout = logout;
module.exports.userPage = userPage;
