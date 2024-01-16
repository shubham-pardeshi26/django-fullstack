import React, { Component } from "react";
import { render } from "react-dom";
import RoomJoinPage from "./RoomJoin";
import CreateRoomPage from "./CreateRoomPage";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";
export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/">
            <div>Hioi, this is for the Home page!</div>
          </Route>
          <Route path="/join" component={RoomJoinPage} />
          <Route path="/create" component={CreateRoomPage} />
        </Switch>
      </Router>
    );
  }
}
