const { Sequelize } = require("sequelize");
const {URL} = require("./db");
const sequelize = new Sequelize(URL);

module.exports = {sequelize}