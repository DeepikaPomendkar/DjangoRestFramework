import React, { Component } from "react";
import { Redirect } from "react-router";

class Login extends Component {
  constructor(props) {
    super(props);

    this.state = {
      authenticated: true // if in future need to setup some kind of authentication (user/admin login)
    };
  }

  render() {
    if (this.state.authenticated) {
      return <Redirect to="/" />;
    } else {
      return (
        <div style={{ fontFamily: "'Josefin Sans', sans-serif" }}>
          Reached /login! 
        </div>
      );
    }
  }
}

export default Login;
