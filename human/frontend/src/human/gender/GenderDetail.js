import {Link} from "react-router-dom";
import React, {useState, useEffect} from 'react';
import axios from 'axios';
import GlobalState from "../Singleton"

const gs = new GlobalState(0);


function GenderDetail({match}){
  const [genders, setGenders]=useState([]);
  const id = match.params.id
  const host = gs.getHost();

  useEffect( () => {
    axios({
      method: "GET",
      url: `${host}/api/v0.1/gender/${id}/`
    }).then(response => {
      setGenders(response.data);
    })
  }, [id])
// console.log(genders)
  return(
    <div>
        <h1>Gender with ID: {genders.id}</h1>
        <h2>{genders.title}</h2>
        <p>
        {genders.description}
        </p>
        <Link className="btn btn-outline-info"
              to={{pathname: `/gender/`,
             fromDashboard: false}}>Return to GenderList.</Link>
    </div>
  )
}

export default GenderDetail;
