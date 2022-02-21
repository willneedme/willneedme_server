import React from 'react';
import Chart from 'react-apexcharts'
import moment from 'moment';
import { useMediaQuery} from 'react-responsive';
import "../../css/marketchart.css"

const MarketChart = (props) => {
    const isMobile = useMediaQuery({
        query : "(max-width:768px)"
    })
    const series = [{
        name: props.name,
        data: props.data.data
    }];
    const charts = props.data.data;
    const percent = ((charts[charts.length - 1] / charts[charts.length - 2] -1) * 100).toFixed(2)
    const options = {
        chart: {
            id: props.name,
            toolbar: {
                show:false
            }
        },
        title: {
            text: `${props.name} (${percent} %) `,
            style: {
                fontSize: "20px",
                fontWeight: "bold",
                color : 0 < percent ? "#FF3636" : "#4374D9"
            }
        },
        colors : [0 < percent ? "#F15F5F" : "#6799FF"],
        xaxis: {
            labels: {
                show : false
            },
            axisTicks: {
                show : false
            },
            categories : props.data.date?.map(d => moment(d).format("YYYY-MM-DD"))
        },
        yaxis: {
            labels: {
                show: false
            }
        },
        noData: {
            text : "Loading.."
        },
    };
    return (
        <div className={"index_chart"}>
            <Chart
                series={series}
                options={options}
                type={"line"}
                width={isMobile ?250 :300}
                height={isMobile ?250 :300}
            />
        </div>
    )
}

export default MarketChart;