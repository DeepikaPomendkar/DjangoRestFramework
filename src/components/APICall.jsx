import React, { Component } from "react";
import { Container, Button } from "react-bootstrap";
import { axiosGET } from "../utils/axiosClient";

class APICall extends Component {
  constructor(props) {
    super(props);
    this.state = {
      clicked: false
    }; // in case of need to set state variables
  }

  callAPI() {
    axiosGET("/empData").then(res => {
      console.log(res.data);
      this.setState({ clicked: true });
    });
  }

  render() {
    let Text;
    if (this.state.clicked) {
      Text = "Now check the browser console.";
    } else {
      Text = "Click on the button above^";
    }
    return (
      <Container>
        <Button
          variant={this.state.clicked ? "outline-success" : "outline-primary"}
          onClick={this.callAPI.bind(this)}
        >
          Click me to call the API!
        </Button>
        <hr />
        <h6>{Text}</h6>
      </Container>
    );
  }
}

export default APICall;
