const express = require("express");
const router = express.Router();
const { auth } = require("../middleware/auth");
const Ticker = require("../models/Ticker");
const User = require("../models/User");
const UserArticle = require("../models/UserArticle");

router.post("/",auth, async (req, res, next) => {
    try {
        const article = await UserArticle.create(req.body);
        const newArticle = await article.save();
        const result = await UserArticle.findAll({
            where: {
                symbol : req.body.symbol
            },
            order : [['createdAt' , 'desc']]
        })
        if (result != null) {
            return res.status(200).json(result);    
        } else {
            return res.json([]);
        }
        
    } catch (e) {
        next(e);
    }
});

router.get("/:symbol", auth, async (req, res, next) => {
    try {
        const result = await UserArticle.findAll({
            where: {
                symbol : req.params.symbol
            },
            order : [['createdAt' , 'desc']]
        }) 
        if (result != null) {
            return res.status(200).json(result);    
        } else {
            return res.json([]);
        }
    } catch (e) {
        next(e);
    }
});

router.get("/", auth, async (req, res, next) => {
    try {
        const result = await UserArticle.findAll({
            order : [['createdAt' , 'desc']]
        }) 
        if (result != null) {
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