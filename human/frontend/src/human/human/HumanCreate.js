import {Link,} from "react-router-dom";
import React, {useState, useEffect} from 'react';
import axios from 'axios';
import GlobalState from "../Singleton"

const gs = new GlobalState(0);

function HumanCreate(effect, deps){
    const [genders, setGenders]=useState([]);
    const [gender, setGender] = useState('');
    const [desc, setDesc] = useState('');
    const [result, setResult] = useState();
    const [alert, setAlert] = useState(false);
    const host = gs.getHost();

    const submit = e => {
        e.preventDefault()
        fetch(`${host}/api/v0.1/gender/`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ title: gender, description: desc })
        })
        .then(res => res.json())
        .then(json => setResult(json.title))
        setAlert(true);
    }

    // useEffect( () => {
    //         axios({
    //             method: "GET",
    //             url: `${host}/api/v0.1/gender/`
    //             }).then(response => {
    //                 setGenders(response.data.results);
    //             });
    //         setAlert(false);
    //         }, [alert, host])
    // // console.log(genders);

    return (
        <div className="gender--list">
            { result && <div> Result: <br /><h3> { result }</h3></div> }
            <form onSubmit={submit}>
                Nickname: <input onChange={t => setGender(t.target.value)}/>
                <br /><br />
                Phone: <input onChange={t => setGender(t.target.value)}/>
                <br /><br />
                Email: <input onChange={t => setGender(t.target.value)}/>
                <br /><br />
                Email: <input onChange={t => setGender(t.target.value)}/>
                <br /><br />
                surname: <input onChange={t => setGender(t.target.value)}/>
                <br /><br />
                name: <input onChange={t => setGender(t.target.value)}/>
                <br /><br />
                middle_name: <input onChange={t => setGender(t.target.value)}/>
                <br /><br />
                gender: <input onChange={t => setGender(t.target.value)}/>
                <br /><br />
                city: <input onChange={t => setGender(t.target.value)}/>
                <br /><br />
                level_english: <input onChange={t => setGender(t.target.value)}/>
                <br /><br />
                language_programming: <input onChange={t => setGender(t.target.value)}/>
                <br /><br />
                framework_programming: <input onChange={t => setGender(t.target.value)}/>
                <br /><br />
                skills_programming: <input onChange={t => setGender(t.target.value)}/>
                <br /><br />
                interval_works: <input onChange={t => setGender(t.target.value)}/>
                <br /><br />
                rate_works: <input onChange={t => setGender(t.target.value)}/>
                <br /><br />
                <input type="submit" value="Add gender" onClick={() => setGender(gender)}/>
            </form>
        </div>
    )
}

export default HumanCreate;
