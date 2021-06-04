import {Link,} from "react-router-dom";
import React, {useState, useEffect} from 'react';
import axios from 'axios';
import GlobalState from "../Singleton"

const gs = new GlobalState(0);

function GenderList(effect, deps){
    const [genders, setGenders]=useState([]);
    const [gender, setGender] = useState('');
    const [desc, setDesc] = useState('');
    const [result, setResult] = useState();
    const [alert, setAlert] = useState(false);
    const host = gs.getHost();

    const submit = e => {
        e.preventDefault()
        fetch(`${host}/api/v0.1/genderCreate/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: gender, description: desc })
        })
        .then(res => res.json())
        .then(json => setResult(json.title))
        setAlert(true);
    }

    useEffect( () => {
            axios({
                method: "GET",
                url: `${host}/api/v0.1/gender/`
                }).then(response => {
                    setGenders(response.data.results);
                });
            setAlert(false);
            }, [alert, host])
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
            { result && <div> Result: <br /><h3> { result }</h3></div> }
            <form onSubmit={submit}>
                Title: <input onChange={t => setGender(t.target.value)}/>
                <br /><br />
                Description: <input onChange={d => setDesc(d.target.value)}/>
                <br /><br />
                <input type="submit" value="Add gender" onClick={() => setGender(gender)}/>
            </form>
        </div>
    )
}

export default GenderList;
