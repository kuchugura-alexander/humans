import {
  // BrowserRouter as Router,
  // Switch,
  // Route,
  Link,
  // useRouteMatch,
  // useParams
} from "react-router-dom";
import React, {
    // Component,
    useState, useEffect} from 'react';
import axios from 'axios';


function HumanList(){
    // let match = useRouteMatch();
    const [humans, setHumans]=useState([]);

    useEffect( () => {
            axios({
                method: "GET",
                url: "http://localhost:8000/api/v0.1/human/"
                }).then(response => {
                    setHumans(response.data.results);
                })
            }, [])
            // console.log(humans);

        return (
       <div  className="humans--list">
           <table  className="table">
               <thead  key="thead">
               <tr>
                   <th>#</th>
                   <th>Nickname</th>
                   <th>Name</th>
                   <th>SurName</th>
                   <th>MiddleName</th>
                   <th>gender</th>
                   <th>Domen</th>
               </tr>
               </thead>
               <tbody>
                   {humans.map( h  =>
                   <tr  key={h.pk}>
                       <td>{h.pk}  </td>
                       <td>{h.nickname}</td>
                       <td>{h.name}</td>
                       <td>{h.surname}</td>
                       <td>{h.middle_name}</td>
                       <td>{h.gender.gender}</td>
                       <td>{h.city.country.domen}</td>
                       <td>
                           <Link className="btn btn-outline-info"
                                 to={{pathname: `/human/${h.pk}/`,
                                     fromDashboard: false}}>Info</Link>
                       </td>
                   </tr>)}
               </tbody>
           </table>
           {/* <button  className="btn btn-primary"  onClick=  {  this.nextPage  }>Next</button> */}
           {/* <button  className="btn btn-primary"  >Next</button> */}
       </div>
        )
}
export default HumanList;
