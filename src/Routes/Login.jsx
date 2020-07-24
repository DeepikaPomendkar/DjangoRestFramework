import React, { Component } from "react";
import { Redirect } from "react-router";
import '../styles/App.css'
import Loginbox from '../components/Loginbox'
import Signupbox from '../components/Signupbox'

class Login extends Component {
  constructor(props) {
    super(props);

    this.state = {
      authenticated: true // if in future need to setup some kind of authentication (user/admin login)
    };
  }

  render() {
    return (
      <div>
          <div className='logindiv'>
              <Loginbox />
          </div>
          <div className='logindiv'>
              <Signupbox />
          </div>
      </div> 
  )
  }
}

export default Login;
