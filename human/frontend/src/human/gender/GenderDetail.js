import React, {useState, useEffect} from 'react';
import axios from 'axios';

function GenderDetail({match}){
  const [genders, setGenders]=useState([]);
  const id = match.params.id

  useEffect( () => {
    axios({
      method: "GET",
      url: `http://localhost:8000/api/v0.1/gender/${id}/`
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
      </div>
  )
}

export default GenderDetail;