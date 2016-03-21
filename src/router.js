var controllers = require('./controllers');
var router = function(app, passport){
  app.get('/login', controllers.Account.loginPage);
  app.post('/login', controllers.Account.login);
  app.get('/userpage', ensureAuthenticated, controllers.Account.userPage);
  app.get('/auth/facebook',
    passport.authenticate('facebook'),
    function(req, res){});
  app.get('/auth/facebook/callback',
    passport.authenticate('facebook',
    {failureRedirect: '/'}),
    function(req, res){ res.redirect('/userpage')});
  app.get('/', controllers.Account.loginPage);
};

function ensureAuthenticated(req, res, next) {
  if (req.isAuthenticated()) { return next(); }
  res.redirect('/login')
}

module.exports = router;
