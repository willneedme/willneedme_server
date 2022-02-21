import { 
    DOWJONES_CHART,
    KOSDAQ_CHART,
    KOSPI_CHART,
    NASDAQ_CHART,
} from '../actions/types'

const initialState = {
    kospi: [],
    kosdaq: [],
    nasdaq: [],
    dowjones: [],
}

export default function chartReducer(state = initialState, action) {
    switch (action.type) {
        case DOWJONES_CHART:
            return {
                ...state,
                dowjones : action.payload
            }
        case NASDAQ_CHART:
            return {
                ...state,
                nasdaq : action.payload
            }
        case KOSPI_CHART:
            return {
                ...state,
                kospi : action.payload
            }
        case KOSDAQ_CHART:
            return {
                ...state,
                kosdaq : action.payload
            }
        default:
            return state;
    }
}