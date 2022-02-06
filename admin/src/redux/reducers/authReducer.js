import {
  AUTH_CHECK
} from '../actions/types';

const initialState = {
  auth : ""
}

export default function authReducer (state = initialState, action) {
  switch(action.type) {
    case AUTH_CHECK :
      return {
        ...state,
        auth : action.payload
      }
    default :
      return state
  }
}
