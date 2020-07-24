import React, { Component } from "react";
import { Redirect } from "react-router";
import '../styles/App.css'
import Loginbox from './Loginbox'
import Signupbox from './Signupbox'

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
          <div class='logindiv'>
              <Loginbox />
          </div>
          <div class='logindiv'>
              <Signupbox />
          </div>
      </div> 
  )
  }
}

export default Login;
