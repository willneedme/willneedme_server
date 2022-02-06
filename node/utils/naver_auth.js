const admin = require('./firebase');
const Async = require('async');
const axios = require('axios');


const naverRequestMeUrl = 'https://openapi.naver.com/v1/nid/me'

function requestMe(naverAccessToken,callback) {
  return axios.get(naverRequestMeUrl,{
    method: 'GET',
    headers: {'Authorization': 'Bearer ' + naverAccessToken}
  }).then((result) => {
    callback(null,result.data,result);
  });
}


function updateOrCreateUser(userId, email, displayName, photoURL) {
  const updateParams = {
    provider: 'NAVER',
    displayName: displayName,
  };
  if (displayName) {
    updateParams['displayName'] = displayName;
  } else {
    updateParams['displayName'] = email;
  }
  if (photoURL) {
    updateParams['photoURL'] = photoURL;
  }
  return admin.auth().updateUser(userId, updateParams).then(function(userRecord) {
    // See the UserRecord reference doc for the contents of `userRecord`.
    console.log("Successfully updated user", userRecord.toJSON());
    userRecord['uid'] = userId;
    if (email) {
      userRecord['email'] = email;
    }
    return admin.auth().createUser(userRecord);
  });
}


function createFirebaseToken(naverAccessToken,callback) {
  Async.waterfall([
    (next)=>{
      requestMe(naverAccessToken, (error, response, params) => {
        const body =response.response // JSON.parse(response)
        const userId = body.id;
        if (!userId) {
          return response.status(404)
          .send({message: 'There was no user with the given access token.'})
        }

        const updateParams = {
          uid :userId,
          email :body.email,
          provider: 'NAVER',
          displayName: '',
        };
        if (body.nickname) {
          updateParams['displayName'] = body.nickname;
        } else {
          updateParams['displayName'] = body.email;
        }
        if (body.profile_image) {
          updateParams['photoURL'] = body.profile_image;
        }
        if (body.mobile_e164) {
          updateParams['phoneNumber'] = body.mobile_e164;
        }
        next(null,updateParams)
      });
    },
    (data, next) => {
      admin.auth().getUserByEmail(data.email).then((user) => {
        next(null,user);
      }).catch((error) => {
        // user doesnt exists
        admin.auth().createUser(data).then((user)=>{
          next(null,user)
        })  
      })
    },
    (data, next) => {
      const userId = data.uid
      admin.auth().createCustomToken(userId, { provider: 'NAVER' }).then((token) => {
        next(null, {
          user: data,
          customToken : token
        });
      });
    }
  ], (err, results) => {
      callback(results);
  });

}

module.exports={
  createFirebaseToken
}