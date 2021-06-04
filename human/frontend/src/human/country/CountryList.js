import {Link,} from "react-router-dom";
import React, {useState, useEffect} from 'react';
import axios from 'axios';
import GlobalState from "../Singleton"

const gs = new GlobalState(0);

function CountryList(effect, deps){
    const [countries, setCountries]=useState([]);
    const [domen, setDomen] = useState('');
    const [country, setCountry] = useState('');
    const [result, setResult] = useState();
    const [alert, setAlert] = useState(false);
    const host = gs.getHost();

    const submit = e => {
        e.preventDefault()
        fetch(`${host}/api/v0.1/countryCreate/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ domen: domen, title: country })
        })
        .then(res => res.json())
        .then(json => setResult(json.title))
        setAlert(true);
    }

    useEffect( () => {
            axios({
                method: "GET",
                url: `${host}/api/v0.1/country/`
                }).then(response => {
                    setCountries(response.data.results);
                });
            setAlert(false);
            }, [alert, host])
    console.log(countries);
    // console.log(result);

    return (
        <div className="country--list">
           <table className="table">
               <thead key="thead">
               <tr>
                   <th>#</th>
                   <th>Domen</th>
                   <th>Title</th>
                   <th>Description</th>
               </tr>
               </thead>
               <tbody>
                   {countries.map( g  =>
                   <tr  key={g.pk}>
                       <td>{g.pk}  </td>
                       <td>{g.domen}</td>
                       <td>{g.title}</td>
                       <td>{g.description}</td>
                       <td>
                           <Link className="btn btn-outline-info"
                                 to={{pathname: `/country/${g.pk}/`,
                                     fromDashboard: false}}>Info</Link>
                       </td>
                   </tr>)}
               </tbody>
           </table>
            { result && <div> Result: <br /><h3> { result }</h3></div> }
            <form onSubmit={submit}>
                Domen: <input onChange={t => setDomen(t.target.value)}/>
                <br /><br />
                Title: <input onChange={t => setCountry(t.target.value)}/>
                <br /><br />
                <input type="submit" value="Add country" onClick={() => setCountry(country)}/>
            </form>
        </div>
    )
}

export default CountryList;
