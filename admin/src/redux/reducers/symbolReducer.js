import { MOST_ACTIVE } from '../actions/types';

const initialState = { 
    mostActive: []
}

export default function symbolReducer(state = initialState, action) {
    switch (action.type) {
        case MOST_ACTIVE:
            return {
                ...state,
                mostActive : action.payload
            }
        default:
            return state
    }
}