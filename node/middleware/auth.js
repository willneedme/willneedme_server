const jwt = require("jsonwebtoken");
const mariadb = require("../mariadb/db");
const User = require("../models/User");
const auth = async (req, res, next) => {
  let token = req.headers["authorization"];
  if (!token) {
    res.status(401).json("Access denied[token]");
  }
  try {
    const bearer = String(token).split(" ");
    const bearerToken = bearer[1];
    jwt.verify(bearerToken, "heedonge" , async (err, user) => {
      if (err) return res.status(403).json("A Token exists, but unknown error send message to us");
      const accessUser = await User.findByPk(user.uid);
      if (accessUser) {
        req.user = accessUser;
        next();
      } else {
        return res.status(200).json("Access denied user is not exist" );
      }
    });
  } catch (e) {
    next(e);
  }
};

module.exports = {
  auth
}