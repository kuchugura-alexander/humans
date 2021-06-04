import {Link} from "react-router-dom";
import React, {useState, useEffect} from 'react';
import GlobalState from "../Singleton"

const gs = new GlobalState(0);


function CityDetail({match}){
  const [city, setCity]=useState([]);
  const [isLoaded, setIsLoaded] = useState(false);
  const [error, setError] = useState(null);
  const id = match.params.id;
  const host = gs.getHost();

  useEffect( () => {
            fetch(`${host}/api/v0.1/city/${id}/`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
        })
    .then(res => res.json())
      .then(
        (result) => {
          setIsLoaded(true);
          setCity(result);
        },
        (error) => {
          setIsLoaded(true);
          setError(error);
        }
      )
  }, [id, host])

    console.log(city)
      if (error) {
      return <div>Ошибка: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Загрузка...</div>;
    } else if (!city.title) {
      return <div>Загрузка...</div>;
    } else {
          return (
              <div>
                  <h1>City with ID: {city.id}</h1>
                  <h2>{city.title}</h2>
                  <br/><br/>
                  Country: {city.country.domen} -
                      {city.country.title} -
                      {city.country.description}
                  <br/><br/>
                  TimeZone: {city.timezone.timezone}
                    ({city.timezone.hours})
                  <br/><br/>
                  {city.description}
                  <br/><br/>
                  <Link className="btn btn-outline-info"
                        to={{
                            pathname: `/city/`,
                            fromDashboard: false
                        }}>Return to CityList.</Link>
              </div>
          )
      }
}

export default CityDetail;
