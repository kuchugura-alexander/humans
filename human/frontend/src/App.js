import React from 'react';
import { BrowserRouter, Link, Route, Switch } from 'react-router-dom';

import MenuList from "./MenuList";
import HumanList from './human/human/HumanList'
import HumanDetail from './human/human/HumanDetail'
import HumanCreate from './human/human/HumanCreate'
import GenderList from "./human/gender/GenderList";
import GenderDetail from "./human/gender/GenderDetail";
import CountryDetail from "./human/country/CountryDetail";
import CountryList from "./human/country/CountryList";
import CityList from "./human/city/CityList";
import CityDetail from "./human/city/CityDetail";


const Main = () => (
  // <main>
          <Switch>
            <Route exact path="/">
                <a href={`https://seven-scale.com`}><h1>Seven-Scale</h1></a>

            </Route>
            <Route path="/menu/" exact component={MenuList} />
            <Route path="/human/" exact component={HumanList} />
            <Route path="/human/:id" exact component={HumanDetail} />
            <Route path="/humanCreate" exact component={HumanCreate} />
            <Route path="/gender/" exact component={GenderList} />
            <Route path="/gender/:id" exact component={GenderDetail} />
            <Route path="/city/" exact component={CityList} />
            <Route path="/city/:id" exact component={CityDetail} />
            <Route path="/country/" exact component={CountryList} />
            <Route path="/country/:id" exact component={CountryDetail} />
            <Route path="/timezone/" exact component={CountryList} />
            <Route path="/timezone/:id" exact component={CountryDetail} />
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
        <Link className="nav-item nav-link" to="/humanCreate">HumanCreate</Link>
        {/*<Link className="nav-item nav-link disabled" to="/humanCreate">HumanCreate</Link>*/}
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
