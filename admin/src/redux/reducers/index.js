import {combineReducers} from 'redux';
import authReducer from './authReducer';
import chartReducer from './chartReducer';
import symbolReducer from './symbolReducer';

const rootReducer = combineReducers({
  auth: authReducer,
  chart: chartReducer,
  symbol : symbolReducer
})

export default rootReducer;