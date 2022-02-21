import axios from 'axios';

import {
    MOST_ACTIVE
} from "../actions/types";

const url = "localhost"

export const getMostActive = () => (dispatch, getState) => {
    const config = {
        header: {
            "Content-Type": "application/json",
        }
    }

    axios
        .get(`http://${url}/flask/api/analyze/most/active`, config)
        .then((res) => {
            dispatch({
                type: MOST_ACTIVE,
                payload: res.data
            })
        })
        .catch((err) => {
            console.log("error", err)
        });
}