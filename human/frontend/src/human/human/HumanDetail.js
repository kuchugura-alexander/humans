import React, {useState, useEffect} from 'react';
import axios from 'axios';

function HumanDetail({match}){
  const [human, setHuman]=useState([]);
  const [city, setCity]=useState([]);
  const id = match.params.id

  useEffect( () => {
    axios({
      method: "GET",
      url: `http://localhost:8000/api/v0.1/human/${id}/`
    }).then(response => {
      setHuman(response.data);
      setCity(response.data.city)
      console.log(response.data.city)
    })
  }, [id])

// console.log(human)
  return(
      <div>
          <h1> Human: {human.nickname} </h1>
          <h2> {human.surname} {human.name} {human.middle_name} </h2>
          {/*Gender : {human.gender.title}*/}
          {/*<br />*/}
          City: {city.title}
        {/*{city.country.domen}*/}
        {/*{city.country.title} -*/}
        {/*  {city.timezone.timezone}*/}
        {/*({city.timezone.hours})*/}
          {/*LevelLanguage: {human.level_english.CEFR} - {human.level_english.knowledge.title} -*/}
          {/*{human.level_english.level.suffix} - {human.level_english.level.title}*/}
          {/*<br />*/}
          {/*LanguageProgramming:*/}
          {/*<br />*/}
          {/*FrameworkProgramming:*/}
          {/*<br />*/}
          {/*SkillProgramming:*/}
          {/*<br />*/}
          {/*IntervalWork:*/}
          {/*<br />*/}
          {/*RateWork:*/}
          <br />
          Description: {human.description}
          {/*<br />*/}
      </div>
  )
}

export default HumanDetail;