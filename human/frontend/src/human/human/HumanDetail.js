import {Link} from "react-router-dom";
import React, {useState, useEffect} from 'react';
import GlobalState from "../Singleton"

const gs = new GlobalState(0);


function HumanDetail({match}){
  const [human, setHuman]=useState({});
  const [isLoaded, setIsLoaded] = useState(false);
  const [error, setError] = useState(null);
  const id = match.params.id
  const host = gs.getHost();

  useEffect( () => {
      fetch(`${host}/api/v0.1/human/${id}/`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
        })
    .then(res => res.json())
      .then(
        (result) => {
          setIsLoaded(true);
          setHuman(result);
        },
        (error) => {
          setIsLoaded(true);
          setError(error);
        }
      )
  }, [id])

  console.log(human)
  // console.log(error)

  if (error) {
      return <div>Ошибка: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Загрузка...</div>;
    } else if (!human.nickname) {
      return <div>Загрузка...</div>;
    } else {
    return (
      <div>
        <Link className="btn btn-outline-info"
              to={{pathname: `/human/`,
             fromDashboard: false}}>Return to HumanList.</Link>

          <h1> Human: {human.nickname} </h1>
          <h2> {human.name} {human.middle_name} </h2>
          Gender : {human.gender.title}
          <br /><br />
          City: {human.city.title} -
                {human.city.country.domen} -
                {human.city.country.title} -
                {human.city.timezone.timezone} -
                ({human.city.timezone.hours})
          <br /><br />
          LevelLanguage: {human.level_english.CEFR} - {human.level_english.knowledge.title} -
          {human.level_english.level.suffix} - {human.level_english.level.title}
          <br /><br />
          LanguageProgramming:
          {human.language_programming.map(h =>
                          <tr key={h.pk}>
                              <td>{h.pk} - </td>
                              <td>{h.title}</td>
                          </tr>)}
          <br />
          FrameworkProgramming:
          {human.framework_programming.map(h =>
                          <tr key={h.pk}>
                              <td>{h.pk} -</td>
                              <td>{h.title}</td>
                          </tr>)}
          <br /><br />
          SkillProgramming:
            {human.skills_programming.map(h =>
                  <tr key={h.pk}>
                      <td>{h.pk} - </td>
                      <td>{h.title}</td>
                  </tr>)}

          <br /><br />
          IntervalWork:
            {human.interval_works.map(h =>
                  <tr key={h.pk}>
                      <td>{h.pk} - </td>
                      <td>{h.title}</td>
                      <td>( {h.timeFrom} - {h.timeTo} )</td>
                      <td>{h.description}</td>
                  </tr>)}

          <br /><br />
          RateWork:
          {human.rate_works.map(h =>
                  <tr key={h.pk}>
                      <td>{h.pk} - </td>
                      <td>{h.title} - </td>
                      <td>{h.price_dollar} $ ( {h.price_rub} RUB)</td>
                  </tr>)}

          <br /><br />
          {/*Description: {human.description}*/}
          {/*<br />*/}

        <Link className="btn btn-outline-info"
              to={{pathname: `/human/`,
             fromDashboard: false}}>Return to HumanList.</Link>
      </div>

    );
  }

}

export default HumanDetail;
