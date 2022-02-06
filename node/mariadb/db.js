const mariadb =require('mysql');


const config = {
    user : process.env.MARIADB_USER,
    host : process.env.MARIADB_HOST,
    database : process.env.MARIADB_DATABASE,
    password : process.env.MARIADB_ROOT_PASSWORD,
    charset : "utf8",
    port : process.env.MARIADB_PORT,
}

const connection = mariadb.createConnection(config);
const URL = `mysql://${config.user}:${config.password}@${config.host}:${config.port}/${config.database}?charset=utf8`
// const URL = `mysql+mysqlconnector://${process.env.MARIADB_USER}:${process.env.MARIADB_ROOT_PASSWORD}@${process.env.MARIADB_HOST}:${process.env.MARIADB_PORT}/${process.env.MARIADB_DATABASE}?charset=utf8`

module.exports = {connection , URL};