import React, { useEffect } from 'react';
import { connect } from "react-redux";
import {authCheck} from '../redux/actions/authAction';
import {Form , Input , Button} from 'antd';
import "antd/dist/antd.css";
import "../css/login.css";

const Login = (props) => {


  const handleSubmit = (data) => {
    console.log(data);
  }

  return (
    <>
      <div className="loginWrap">
      <p className="title">Willneedme</p>
      <Form layout="vertical" onFinish={handleSubmit}>
        <Form.Item label="email" name="email">
          <Input />
        </Form.Item>
        <Form.Item label="password" name="password">
          <Input type="password" />
        </Form.Item>
        <Form.Item>
          <Button type="primary" htmlType="submit" style={{ width: "100%" }}>
            Login
          </Button>
        </Form.Item>
      </Form>
    </div>
    </>
  );
}

const stateToProps = (state) => {
  return {
    test : state.auth.auth
  }
}

const dispatchToProps = (dispatch) => {
  return {
    authCheck : () => dispatch(authCheck())
  }
}

export default connect(stateToProps , dispatchToProps)(Login);