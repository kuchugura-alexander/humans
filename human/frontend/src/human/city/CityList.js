import {Link,} from "react-router-dom";
import React, {useState, useEffect} from 'react';
import GlobalState from "../Singleton"

const gs = new GlobalState(0);

function CityList(effect, deps){
    const [city, setCity] = useState('');
    const [country, setCountry] = useState('');
    const [timezone, setTimezone] = useState('');
    const [cityNew, setCityNew] = useState('');
    const [countryNew, setCountryNew] = useState('');
    const [timezoneNew, setTimezoneNew] = useState('');
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
        console.log("===>", cityNew, countryNew, timezoneNew);
        fetch(`${host}/api/v0.1/cityCreate/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                title: cityNew,
                country: countryNew,
                timezone: timezoneNew,})
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
                setCountryNew(result.results[0].pk)
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
                setTimezoneNew(result.results[0].pk)
            },
            (error) => {
                setIsLoadedTimezone(true);
                setErrorTimezone(error);
            }
        )
        setAlert(false);

    }, [alert, host])

    console.log("city -> ", city);
    console.log("country -> ", country);
    console.log("timezone -> ", timezone);


    const handleChangeCity = (e) => {
        setCityNew(e.target.value);
        // console.log(e.target.value, e.label);
    }
    const handleChangeCountry = (e) => {
        setCountryNew(e.target.value);
        // console.log(e.target.value, e.label);
    }
    const handleChangeTimeZone = (e) => {
        setTimezoneNew(e.target.value);
        // console.log(e.target.value, e.label);
    }

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
                <label>
                    Title: <input type="text" name="city" placeholder="Input you city" onChange={handleChangeCity}/>
                </label>
                <br /><br />
                <label>
                    Country:
                    <select id="chCountry" value={countryNew} onChange={handleChangeCountry}>
                        {country.map( c  =>
                            <option key={c.pk} value={c.pk}>{c.pk} - {c.domen} - {c.title}</option>
                        )}
                    }
                </select>
                </label>
                <br /><br />
                <label>
                    TimeZoneResidence:
                    <select id="chTimezone" value={timezoneNew} onChange={handleChangeTimeZone}>
                        {/*<option key="-1" value="-1">Null</option>*/}
                         {timezone.map( t  =>
                          <option key={t.pk} value={t.pk}>{t.timezone}</option>
                         )}
                    </select>
                </label>
                <br /><br />
                <input type="submit" value="Add city"/>
            </form>
        </div>
    )
    }
}

export default CityList;

// <input type="submit" value="Add city" onClick={() => setCity(city)}/>
