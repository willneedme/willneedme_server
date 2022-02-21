import React from 'react';
import Header from '../common/Header';
import IndexChart from '../charts/IndexChart';
import MostActive from '../list/MostActive';

const Main = (props) => {
    return (
        <>
            <Header/>
            <IndexChart />
            <MostActive/>
        </>
    );
}

export default Main;