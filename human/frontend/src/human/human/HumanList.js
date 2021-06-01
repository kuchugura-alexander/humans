import {Link,} from "react-router-dom";
import React, { useState, useEffect} from 'react';
import GlobalState from "../Singleton"

const gs = new GlobalState(0);

function HumanList(){
    const [humans, setHumans]=useState([]);
    const [humans_count, setHumans_count]=useState([]);
    const [isLoaded, setIsLoaded] = useState(false);
    const [error, setError] = useState(null);
    const host = gs.getHost();

    useEffect( () => {
              fetch(`${host}/api/v0.1/human/`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
        })
        .then(res => res.json())
          .then(
            (result) => {
              setIsLoaded(true);
              setHumans(result.results);
              setHumans_count(result.count)
            },
            (error) => {
              setIsLoaded(true);
              setError(error);
            }
          )
            //
            // axios({
            //     method: "GET",
            //     url: "http://localhost:8000/api/v0.1/human/"
            //     }).then(response => {
            //         setHumans(response.data.results);
            //     })
            }, [])
            // console.log("--->>", humans);

      if (error) {
      return <div>Ошибка: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Загрузка...</div>;
    } else if (!humans_count) {
      return <div>Загрузка...</div>;
    } else {
          return (
              <div className="humans--list">
                  <table className="table">
                      <thead key="thead">
                      <tr>
                          <th>#</th>
                          <th>Nickname</th>
                          <th>Name</th>
                          <th>MiddleName</th>
                          <th>gender</th>
                          <th>Domen</th>
                      </tr>
                      </thead>
                      <tbody>
                      {humans.map(h =>
                          <tr key={h.pk}>
                              <td>{h.pk}  </td>
                              <td>{h.nickname}</td>
                              <td>{h.name}</td>
                              <td>{h.middle_name}</td>
                              <td>{h.gender.gender}</td>
                              <td>{h.city.country.domen}</td>
                              <td>
                                  <Link className="btn btn-outline-info"
                                        to={{
                                            pathname: `/human/${h.pk}/`,
                                            fromDashboard: false
                                        }}>Info</Link>
                              </td>
                          </tr>)}
                      </tbody>
                  </table>
                  {/* <button  className="btn btn-primary"  onClick=  {  this.nextPage  }>Next</button> */}
                  {/* <button  className="btn btn-primary"  >Next</button> */}
              </div>
          )
      }
}
export default HumanList;
