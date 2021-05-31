import {
  Link,
  // useRouteMatch,
} from "react-router-dom";
import React, {useState, useEffect} from 'react';
import axios from 'axios';


function GenderList(){
    // let match = useRouteMatch();
    const [genders, setGenders]=useState([]);

    useEffect( () => {
            axios({
                method: "GET",
                url: "http://localhost:8000/api/v0.1/gender/"
                }).then(response => {
                    setGenders(response.data.results);
                })
            }, [])
            // console.log(genders);

        return (
            <div className="gender--list">
               <table className="table">
                   <thead key="thead">
                   <tr>
                       <th>#</th>
                       <th>Title</th>
                       <th>Description</th>
                   </tr>
                   </thead>
                   <tbody>
                       {genders.map( g  =>
                       <tr  key={g.pk}>
                           <td>{g.pk}  </td>
                           <td>{g.title}</td>
                           <td>{g.description}</td>
                           <td>
                               <Link className="btn btn-outline-info"
                                     to={{pathname: `/gender/${g.pk}/`,
                                         fromDashboard: false}}>Info</Link>
                           </td>
                       </tr>)}
                   </tbody>
               </table>
            </div>
        )
}
export default GenderList;
