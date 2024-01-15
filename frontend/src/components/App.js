import react,{Component} from "react";
import {render} from "react-dom";

export default class App extends Component{
    constructor(props){
        super(props);
    }
    render(){
        return (<h1>hii, there... </h1>)
    }
}

const appDiv = document.getElementById("app111");
render(<App/>,appDiv);