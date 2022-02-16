const { sequelize } =require("../mariadb/database");

const Ticker = require("./Ticker");
const User = require("./User");
const UserArticle = require("./UserArticle");

UserArticle.hasMany(Ticker, {
    constraints : false,
    foreignKey: "symbol",
    sourceKey : "symbol"
});
UserArticle.hasMany(User, {
    constraints : false,
    foreignKey: "uid",
    sourceKey : "uid"
}); 
// }
Ticker.belongsTo(UserArticle, {
    constraints: false,
    foreignKey: "symbol",
    sourceKey:"symbol"
});

User.belongsTo(UserArticle, {
    constraints: false,
    foreignKey: "uid",
    sourceKey:"uid"
});


// (async () => {
//     try {
//         await sequelize.sync();
//     } catch (e) {
//         console.log(e);
//     }
// })();

module.exports = {
    Ticker,
    User,
    UserArticle
}