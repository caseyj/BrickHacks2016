var crypro = require('crypto');
var mongoose = require('mongoose');

var AccountModel;
var iterations = 10000;
var saltLength = 64;
var keyLength = 64;

var AccountSchema = new mongoose.Schema({
  username: {
    type: String,
    required: true,
    trim: true,
    unique: true,
    match: /^[A-Za-z0-9_\-\.]{1,16}$/
  },

  salt: {
    type: Buffer,
    required: true
  },

  FacebookUID: {
    type: Number,
    required: true,
    unique: true
  },

  createdData: {
    type: Date,
    default: Date.now
  }
});

AccountSchema.methods.toAPI = function(){
  return {
    username: this.username,
    _id: this._id
  };
};

AccountSchema.statics.findByUsername = function(name, callback){
  var search = {
    username: name
  };

  return AccountModel.findOne(search, callback);
};

AccountSchema.statics.findByFacebookUID = function(UID, callback){
  var search = {
    FacebookUID: UID
  };

  return AccountModel.findOne(search, callback);
}

/*
// TODO: NEEDS SOME PASSWORD INPUT
AccountSchema.statics.generateHash = function(something, callback){
  var salt = crypto.randomBytes(saltLength);

  crypto.pdkdf2(something, salt, iterations, keyLength, function(err, hash){
    return callback(salt, hash.toString('hex'));
  });
}
*/

AccountModel = mongoose.model('Account', AccountSchema);

module.exports.AccountModel = AccountModel;
module.exports.AccountSchema = AccountSchema;
