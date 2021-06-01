import {Link,} from "react-router-dom";
import React, {useState, useEffect} from 'react';
import GlobalState from "../Singleton"

const gs = new GlobalState(0);

function CityList(effect, deps){
    const [city, setCity] = useState('');
    const [country, setCountry] = useState('');
    const [timezone, setTimezone] = useState('');
    const [isLoadedCity, setIsLoadedCity] = useState(false);
    const [isLoadedCountry, setIsLoadedCountry] = useState(false);
    const [isLoadedTimezone, setIsLoadedTimezone] = useState(false);
    const [errorCity, setErrorCity] = useState(null);
    const [errorCountry, setErrorCountry] = useState(null);
    const [errorTimezone, setErrorTimezone] = useState(null);
    const [result, setResult] = useState();
    const [alert, setAlert] = useState(false);
    const host = gs.getHost();

    const submit = e => {
        e.preventDefault()
        fetch(`${host}/api/v0.1/city/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                title: city,
                country: country,
                timezone: timezone,})
        })
        .then(res => res.json())
        .then(json => setResult(json.title))
        setAlert(true);
    }

    useEffect( () => {
        fetch(`${host}/api/v0.1/city/`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
        })
        .then(res => res.json())
        .then(
            (result) => {
                setIsLoadedCity(true);
                setCity(result.results);
            },
            (error) => {
                setIsLoadedCity(true);
                setErrorCity(error);
            }
        )
        fetch(`${host}/api/v0.1/country/`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
        })
        .then(res => res.json())
        .then(
            (result) => {
                setIsLoadedCountry(true);
                setCountry(result.results);
            },
            (error) => {
                setIsLoadedCountry(true);
                setErrorCountry(error);
            }
        )
        fetch(`${host}/api/v0.1/timezoneresidence/`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
        })
        .then(res => res.json())
        .then(
            (result) => {
                setIsLoadedTimezone(true);
                setTimezone(result.results);
            },
            (error) => {
                setIsLoadedTimezone(true);
                setErrorTimezone(error);
            }
        )


    }, [alert, host])

    console.log("city -> ", city);
    console.log("country -> ", country);
    console.log("timezone -> ", timezone);

    if (errorCity) {
        return <div>ОшибкаCity: {errorCity.message} </div>;
    } else if (errorCountry) {
        return <div>ОшибкаCountry: {errorCountry.message} </div>;
    } else if (errorTimezone) {
        return <div>ОшибкаTimezone: {errorTimezone.message} </div>;
    } else if (!isLoadedCity) {
        return <div>Загрузка City...</div>;
    } else if (!isLoadedCountry) {
        return <div>Загрузка Country...</div>;
    } else if (!isLoadedTimezone) {
        return <div>Загрузка TimeZoneResidence...</div>;
    } else if (!city.length) {
        return <div>City...</div>;
    } else if (!country.length) {
        return <div>Country...</div>;
    } else if (!timezone.length) {
        return <div>Timezone...</div>;
    } else {
    return (
        <div className="city--list">
           <table className="table">
               <thead key="thead">
               <tr>
                   <th>#</th>
                   <th>Title</th>
                   <th>TimeZone</th>
                   <th>Description</th>
               </tr>
               </thead>
               <tbody>
                   {city.map( g  =>
                   <tr  key={g.pk}>
                       <td>{g.pk}  </td>
                       <td>{g.title}</td>
                       <td>{g.timezone.timezone}</td>
                       <td>{g.description}</td>
                       <td>
                           <Link className="btn btn-outline-info"
                                 to={{pathname: `/city/${g.pk}/`,
                                     fromDashboard: false}}>Info</Link>
                       </td>
                   </tr>)}
               </tbody>
           </table>
            { result && <div> Result: <br /><h3> { result }</h3></div> }
            <form onSubmit={submit}>
                Title: <input />
                <br /><br />
                Country:
                <select id="ddlViewBy" onSelect={() =>{
                    var e = document.getElementById("ddlViewBy");
                    var as = document.forms[0].ddlViewBy.value;
                    var strUser = e.options[e.selectedIndex].value;
                    console.log(as, strUser);}
                }>
                     {country.map( c  =>
                      <option>{c.domen} - {c.title}</option>
                     )}
                </select>
                <br /><br />
                TimeZoneResidence:
                <select>
                     {timezone.map( t  =>
                      <option>{t.timezone}</option>
                     )}
                </select>
                <br /><br />
                <input type="submit" value="Add city" onClick={() => setCity(city)}/>
            </form>
        </div>
    )
    }
}

export default CityList;
