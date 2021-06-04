import logo from './logo.svg';
import React, { Component } from 'react'
import { Router, Route, IndexRoute, Link, browserHistory } from 'react-router'

class List extends Component {

   state = {
       articles: []
   };

   async loadArticles() {
       this.setState({
           articles: await fetch("/api/v0.1/humans/").then(response =>response.json())
       })
   }


   componentDidMount() {
       this.loadArticles();
   }

   render(){
   console.log(this.state.articles);
       return(
           <ul className="content-list">
               {this.state.articles.map((article, index) => (
                   <li className="content-list__item" key={index}>
                   </li>
               ))}
           </ul>
       );
   }
}

//export default List

class App extends Component {
    render(){
        return (
            <div className="App">
            <Router history={ browserHistory }>


            </Router>
            </div>
        );
    }
}

export default App;
