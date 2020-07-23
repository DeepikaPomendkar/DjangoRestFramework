import React, { Component } from "react";
import APICall from "../components/APICall";
import { Jumbotron, Container } from "react-bootstrap";
class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <Container>
        <Jumbotron>
          <h1>Code For Good - Team 17</h1>

          <h2>This is a test web app using Django and React.js</h2>
        </Jumbotron>
        <APICall />
      </Container>
    );
  }
}

export default Home;
