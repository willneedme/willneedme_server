const { Sequelize, DataTypes } = require("sequelize");
const { sequelize } = require("../mariadb/database");

const Ticker = sequelize.define("tickers", {
    symbol: {
        type: DataTypes.STRING,
        primaryKey :true,
    },
    country: {
        type : DataTypes.STRING
    },
    industry: {
        type : DataTypes.STRING
    },
    ipoYear: {
        type : DataTypes.STRING
    },
    sector: {
        type : DataTypes.STRING
    },
    marketCap: {
        type : DataTypes.DOUBLE
    },
    name: {
        type : DataTypes.STRING
    },
    netChange: {
        type : DataTypes.DOUBLE
    },
    logoUrl: {
        type : DataTypes.STRING
    },
})

module.exports = Ticker;