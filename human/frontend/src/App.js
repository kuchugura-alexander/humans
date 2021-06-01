import React from 'react';
import { BrowserRouter, Link, Route, Switch } from 'react-router-dom';

import MenuList from "./MenuList";
import HumanList from './human/human/HumanList'
import HumanDetail from './human/human/HumanDetail'
import GenderList from "./human/gender/GenderList";
import GenderDetail from "./human/gender/GenderDetail";
// import GlobalState from "../Singleton"

// const gs = new GlobalState(0);


// const HumanNotFind = () => (
//   <div>
//     <h1>Human Not Find!</h1>
//   </div>
// )

// The Main component renders one of the three provided
// Routes (provided that one matches). Both the /roster
// and /schedule routes will match any pathname that starts
// with /roster or /schedule. The / route will only match
// when the pathname is exactly the string "/"
// const host = gs.getHost();

const Main = () => (

  // <main>
          <Switch>
            <Route exact path="/">
                <a href={`https://seven-scale.com`}><h1>Seven-Scale</h1></a>

            </Route>
            <Route path="/menu/" exact component={MenuList} />
            <Route path="/human/" exact component={HumanList} />
            <Route path="/human/:id" exact component={HumanDetail} />
            {/*<Route path="/createHuman" exact component={HumansList} />*/}
            <Route path="/gender/" exact component={GenderList} />
            <Route path="/gender/:id" exact component={GenderDetail} />
            {/*  <GenderCreate />*/}
            {/*</Route>*/}
          </Switch>
  //  </main> 
)

// The Header creates links that can be used to navigate
// between routes.
const Navigate = () => (
  // <header>
    <nav className="nav nav-pills nav-justified">
        <Link className="nav-item nav-link active" to="/">Home</Link>
        <Link className="nav-item nav-link" to="/menu">Menu</Link>
        <Link className="nav-item nav-link disabled" to="/humanCreate">HumanCreate</Link>
    </nav>
  // </header>
)


// class App extends Component{
function App() {
  
    // render(){
    return (
      <div>
        <BrowserRouter>
          <Navigate />
          <Main />
        </BrowserRouter>
      </div>
    );
  // }
}

export default App;
