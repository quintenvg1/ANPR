const mongoose = require('mongoose');

const UserSchema = new mongoose.Schema({
  ID: { type:Number, required: false },
  naam: { type: String, required: true },
  paswoord: { type: String, required: true },
  nummerplaat: { type: Number, required: true },
});

const User = mongoose.model('User', UserSchema);

function getUserDocument(req, res, next) {
  User.findOne({ID: req.user.ID}, (err, user) => {
     if (err || !user) {
         res.status('400').json({status: 'user-missing'});
     }
     req.userDocument = user;
     next();
  });
}

module.exports = { UserSchema, User, getUserDocument };