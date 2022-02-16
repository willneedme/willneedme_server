const express = require("express");
const router = express.Router();
const { auth } = require("../middleware/auth");
const { Ticker , User , UserArticle} = require("../models/index");
// const Ticker = require("../models/Ticker");
// const User = require("../models/User");
// const UserArticle = require("../models/UserArticle");
// const Test = require("../models/Test");
// const TestB = require("../models/TestB");

router.post("/",auth, async (req, res, next) => {
    try {
        const article = await UserArticle.create(req.body);
        await article.save();
        const articles = await UserArticle.findAll({
            include: [
                {
                    model: Ticker,
                    attributes : ["name"]
                },
            ],
            where: {
                symbol : req.body.symbol
            },
            order : [['createdAt' , 'desc']]
        })
        if (articles != null) {
            let result = articles.map(item => {
                return {
                    ...item.dataValues,
                    "name": item.tickers[0].dataValues.name
                };
            });
            return res.status(200).json(result);    
        } else {
            return res.json([]);
        }
        
    } catch (e) {
        return res.json(null);
    }
});

router.get("/:symbol", auth, async (req, res, next) => {
    try {
        const articles = await UserArticle.findAll({
            include: [
                {
                    model: Ticker,
                    attributes : ["name"]
                },
            ],
            where: {
                symbol : req.params.symbol
            },
            order : [['createdAt' , 'desc']]
        }) 
        if (articles != null) {
            let result = articles.map(item => {
                return {
                    ...item.dataValues,
                    "name": item.tickers[0].dataValues.name
                };
            });
            return res.status(200).json(result);    
        } else {
            return res.json([]);
        }
    } catch (e) {
        next(e);
    }
});

router.get("/", async (req, res, next) => {
    try {
        const articles = await UserArticle.findAll({
            include: [
                {
                    model: Ticker,
                    attributes : ["name"]
                },
            ],
            order: [['createdAt', 'desc']]
        }); 
        if (articles != null) {
            let result = articles.map(item => {
                return {
                    ...item.dataValues,
                    "name": item.tickers[0].dataValues.name
                };
            });
            return res.status(200).json(result);
        } else {
            return res.json([]);
        }
    } catch (e) {
        next(e);
    }
});

router.delete("/", auth, async (req, res, next) => {
    try {
        if (req.body) {
            await UserArticle.destroy({
                where: {
                    id : req.body.id
                }
            })    
        }
        return res.end();
    } catch (e) {
        next(e);
    }
});

module.exports = router