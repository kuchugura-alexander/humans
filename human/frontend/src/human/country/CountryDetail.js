import {Link} from "react-router-dom";
import React, {useState, useEffect} from 'react';
import axios from 'axios';
import GlobalState from "../Singleton"

const gs = new GlobalState(0);


function CountryDetail({match}){
  const [countries, setCountries]=useState([]);
  const id = match.params.id;
  const host = gs.getHost();

  useEffect( () => {
    axios({
      method: "GET",
      url: `${host}/api/v0.1/country/${id}/`
    }).then(response => {
      setCountries(response.data);
    })
  }, [id, host])
// console.log(genders)
  return(
    <div>
        <h1>Country with ID: {countries.id}</h1>
        <h2>{countries.domen} - {countries.title}</h2>
        <p>
        {countries.description}
        </p>
        <Link className="btn btn-outline-info"
              to={{pathname: `/country/`,
             fromDashboard: false}}>Return to CountryList.</Link>
    </div>
  )
}

export default CountryDetail;
