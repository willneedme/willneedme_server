import React from 'react';
import { useEffect } from 'react';
import { connect } from 'react-redux';
import { getNasdaq , getDowjones , getKosdaq , getKospi } from '../../redux/actions/chartAction';
import MarketChart from './MarketChart';
import '../../css/marketchart.css';

const IndexChart = (props) => {

    useEffect(() => {
        props.getNasdaq();
        props.getDowjones();
        props.getKosdaq();
        props.getKospi();
    }, [])

    return (
        <div className={"chart"}>
            {props.kospi.length !== 0 ? <MarketChart data={props.kospi} name={"코스피"} /> : <></>}
            {props.kosdaq.length !== 0 ? <MarketChart data={props.kosdaq} name={"코스닥"} /> : <></>}
            {props.nasdaq.length !== 0 ? <MarketChart data={props.nasdaq} name={"Nasdaq"} /> : <></>}
            {props.dowjones.length !== 0 ? <MarketChart data={props.dowjones} name = {"Dow"}/> : <></>}
        </div>
    )
}

const stateToProps = (state) => {
    console.log(state)
    return {
        nasdaq: state.chart.nasdaq,
        dowjones: state.chart.dowjones,
        kospi : state.chart.kospi,
        kosdaq : state.chart.kosdaq,
    }
}

const dispatchToProps = (dispatch) => {
    return {
        getNasdaq: () => dispatch(getNasdaq()),
        getDowjones: () => dispatch(getDowjones()),
        getKospi: () => dispatch(getKospi()),
        getKosdaq: () => dispatch(getKosdaq()),
    }
}

export default connect(stateToProps, dispatchToProps)(IndexChart);