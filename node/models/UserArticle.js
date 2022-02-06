const { Sequelize, DataTypes } = require("sequelize");
const { sequelize } = require("../mariadb/database");
const Ticker = require("./Ticker");
const User = require("./User");

const UserArticle = sequelize.define("user_articles", {
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement : true
    },
    uid: {
        type: DataTypes.STRING,
        references: {
            model: User,
            key : "uid"
        }
    },
    displayName: {
        type: DataTypes.STRING,
    },
    description: {
        type: DataTypes.TEXT,
    },
    symbol: {
        type: DataTypes.STRING,
        references: {
            model: Ticker,
            key : "symbol"
        }
    },
},{
    timestamps: true,
});


module.exports = UserArticle;