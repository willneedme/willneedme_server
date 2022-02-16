const { DataTypes } = require("sequelize");
const { sequelize } = require("../mariadb/database");

const UserArticle = sequelize.define("user_articles", {
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement : true
    },
    uid: {
        type: DataTypes.STRING,
        references: {
            model: "users",
            key : "uid"
        },
        allowNull: false,
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
            model: "tickers",
            key : "symbol"
        },
        allowNull: false,
    },
},{
    timestamps: true,
});


module.exports = UserArticle;