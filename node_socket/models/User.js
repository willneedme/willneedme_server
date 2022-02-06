const { Sequelize, DataTypes } = require("sequelize");
const { sequelize } = require("../mariadb/database");

const User = sequelize.define("users", {
  uid: {
    type: DataTypes.STRING,
    allowNull: false,
    primaryKey : true
  },
  displayName: {
    type : DataTypes.STRING,
  },
  email: {
    type : DataTypes.STRING,
  },
  emailVerified: {
    type: DataTypes.BOOLEAN,
    defaultValue : false
  },
  phoneNumber: {
    type : DataTypes.STRING,
  },
  deviceToken: {
    type : DataTypes.TEXT,
  },
  receiveFcm: {
    type: DataTypes.BOOLEAN,
    defaultValue:false
  },
  isAdmin: {
    type: DataTypes.BOOLEAN,
    defaultValue:false
  },
  loginType: {
    type : DataTypes.STRING,
  },
  createdAt: {
    type:DataTypes.DATE
  },
  updatedAt: {
    type:DataTypes.DATE
  }
}, {
  timestamps: true,
})

// (async () => {
//   await sequelize.sync({force : true})
// })

module.exports = User;