import React, {useState, useEffect} from 'react';
import axios from 'axios/dist/axios';
import logo from './logo.svg';
/*import './App.css';
import  HumansList from './HumansList'
*/
function App() {
const axios = require('axios');

    resd = useEffect( effect: () => {
        axios.get("http://localhost:8000/api/0.1/humans",
            ).then(res => {
      console.log(res.data);
      });
/*  then(response => {
            setPeople(response.data);
*/        });
    })
/*    , deps: [])*/

  return (
    <div className="App">
    <h1>Hello react</h1>

    </div>
  );
}

export default App;
