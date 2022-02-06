const express = require('express');
const router = express.Router();
const { connection } = require('../mariadb/db');
const {sequelize } = require("../mariadb/database");
const { auth } = require("../middleware/auth");
const { createFirebaseToken } = require("../utils/naver_auth");
const User = require("../models/User");


router.get('/info',auth ,async (req, res, next) => {
    try {
        const user = await User.findByPk(req.user.uid);
        if (user) {
            res.status(200).json(user);    
        } else {
            res.status(200).json(null);
        }
        
    } catch (e) {
        next(e);
    }
});
router.post("/account", async (req, res, next) => {
    try {
        const findUser = await User.findByPk(req.body.uid);
        if (!findUser) {
            console.log("user is null")
            const user = await User.create(req.body);
            let newUser = await user.save();    
            if (newUser) {
                res.status(200).json(newUser.dataValues);
            } else {
                res.json(null);
            }
        } else {
            res.status(200).json(findUser);
        }
    } catch (e) {
        next(e);
    }
});

router.get("/naver/signin", async (req, res, next) => {
    try {
        //Authentication Code api
        const redirect = `webauthcallback://success?${new URLSearchParams(req.query).toString()}`;
        res.redirect(307, redirect);
    } catch (e) {
        next(e);
    }
});

router.post("/naver/token", async (req, res, next) => {
    try {
        createFirebaseToken(req.body["accessToken"], async (result) => {
            let snsUser = result.user;
            const findUser = await User.findByPk(snsUser.uid);
            if (!findUser) {
                const user = await User.create({
                    uid: snsUser.uid,
                    email: snsUser.email,
                    emailVerified: snsUser.emailVerified,
                    displayName: snsUser.displayName,
                    phoneNumber: snsUser.phoneNumber,
                    loginType : "naver"
                });
                let newUser = await user.save();    
                if (newUser) {
                    res.status(200).json({
                        user: newUser.dataValues,
                        customToken : result.customToken
                    });
                } else {
                    res.status(200).json({
                        user: null,
                        customToken: result.customToken
                    });
                }
            } else {
                res.status(200).json({
                    user: findUser,
                    customToken: result.customToken
                });
            }
        });
    } catch (e) {
        next(e);
    }
});


module.exports = router;