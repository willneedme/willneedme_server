import axios from 'axios';

import {AUTH_CHECK} from '../actions/types'

export const authCheck = () => async (dispatch, getState) => {
  // const token = getState().auth.token;

  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };
  // if (token) {
  //   config.headers["authorization"] = `Bearer ${token}`;
  // }

  axios
    .get("http://localhost/flask/api/finance/test", config)
    .then((res) => {
      dispatch({
        type: AUTH_CHECK,
        payload: res.data,
      });
    })
    .catch((err) => {
      console.log("error", err);
    });
};