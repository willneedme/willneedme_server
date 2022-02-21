import React, { useState } from 'react';
import { useEffect , useMemo} from 'react';
import { connect } from 'react-redux';
import { getMostActive } from '../../redux/actions/symbolAction';
import { useMediaQuery} from 'react-responsive';
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/dist/styles/ag-grid.css';
import 'ag-grid-community/dist/styles/ag-theme-alpine.css';
import '../../css/aggrid.css';

// import { AllCommunityModules } from '@ag-grid-community/all-modules';

const MostActive = (props) => {
    const isMobile = useMediaQuery({
        query : "(max-width:768px)"
    });
    const [gridApi, setGridApi] = useState(null);
    useEffect(() => {
        props.getMostActive();
    }, []);


    const onGridReady = (arg) => {
        setGridApi(arg.api);
    }
    const openModal = (arg) => {
        //detail symbol info
        console.log(arg);
    }

    useEffect(() => {
        if (gridApi) gridApi.paginationSetPageSize(10);
    }, [gridApi]);

    const precentRederer = (arg) => {
        return (
            <div style={{color : 0 < arg.value ? "red" : "blue" , fontWeight : "bold"} }>
                {arg?.value}
            </div>
        );
    }

    const columDef = [
        { field: "symbol", headerName: "코드" },
        { field: "name", headerName: "종목" },
        { field: "percent", headerName: "등락률" ,cellRenderer : precentRederer},
        { field: "price", headerName: "가격" },
        { field: "volume", headerName: "거래량" },
        { field: "avgThreeMonth", headerName: "3개월 평균 거래량" },
    ];

    const mobileColumnDef = [
        { field: "symbol", headerName: "코드" },
        { field: "percent", headerName: "등락률" },
        { field: "volume", headerName: "거래량" },
        { field: "avgThreeMonth", headerName: "3개월 평균 거래량" },
    ]

    const defaultColDef = useMemo(() => {
        return {
            sortable: true,
            resizable: true,
            flex: 1,
            minWidth: 100,
            paginationPageSize: 10
        };
      }, []);
    return (
        <div className="ag-theme-alpine">
            {props.mostActive.length != 0 ?<AgGridReact
                defaultColDef={defaultColDef}
                pagination={true}
                onRowClicked={openModal}
                rowSelection={"multiple"}
                columnDefs={isMobile ? mobileColumnDef : columDef}
                rowData = {props.mostActive}
                onGridReady = {onGridReady}
            >
            </AgGridReact> : <></>}
        </div>
    );
}

const stateToProps = (state) => {
    return {
        mostActive : state.symbol.mostActive
    }
}

const dispatchToProps = (dispatch) => {
    return {
        getMostActive : () => dispatch(getMostActive())
    }
}

export default connect(stateToProps, dispatchToProps)(MostActive);