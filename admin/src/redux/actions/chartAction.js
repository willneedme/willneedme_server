import axios from 'axios';

import { 
    DOWJONES_CHART,
    KOSDAQ_CHART,
    KOSPI_CHART,
    NASDAQ_CHART
} from '../actions/types';

const url = "localhost"

export const getNasdaq = () => async (dispatch, getState) => {
    const config = {
        header: {
            "Content-Type": "application/json",
        }
    }
    
    axios
        .get(`http://${url}/flask/api/finance/index/nasdaq`, config)
        .then((res) => {
            dispatch({
                type: NASDAQ_CHART,
                payload: res.data
            })
        })
        .catch((err) => {
            console.log("error", err)
        });
    
}

export const getDowjones = () => async (dispatch, getState) => {
    const config = {
        header: {
            "Content-Type": "application/json",
        }
    }
    
    axios
        .get(`http://${url}/flask/api/finance/index/dowjones`, config)
        .then((res) => {
            dispatch({
                type: DOWJONES_CHART,
                payload: res.data
            })
        })
        .catch((err) => {
            console.log("error", err)
        });
    
}

export const getKospi = () => async (dispatch, getState) => {
    const config = {
        header: {
            "Content-Type": "application/json",
        }
    }
    
    axios
        .get(`http://${url}/flask/api/finance/index/kospi`, config)
        .then((res) => {
            dispatch({
                type: KOSPI_CHART,
                payload: res.data
            })
        })
        .catch((err) => {
            console.log("error", err)
        });
    
}

export const getKosdaq = () => async (dispatch, getState) => {
    const config = {
        header: {
            "Content-Type": "application/json",
        }
    }
    
    axios
        .get(`http://${url}/flask/api/finance/index/kosdaq`, config)
        .then((res) => {
            dispatch({
                type: KOSDAQ_CHART,
                payload: res.data
            })
        })
        .catch((err) => {
            console.log("error", err)
        });
    
}