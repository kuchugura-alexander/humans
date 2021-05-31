import React from 'react';
import { BrowserRouter, Link, Route, Switch } from 'react-router-dom';

import MenuList from "./MenuList";
import HumanList from './human/human/HumanList'
import HumanDetail from './human/human/HumanDetail'
import GenderList from "./human/gender/GenderList";
import GenderDetail from "./human/gender/GenderDetail";

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
const Main = () => (
  // <main>
          <Switch>
            <Route exact path="/">
              <h1>HOME</h1>
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
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/menu/">Menu</Link></li>
            <li><Link to="/human/">Humans</Link></li>
            {/*<li><Link to="/createHuman">createHuman</Link></li>*/}
            <li><Link to="/gender/">Genders</Link></li>
          </ul>
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
