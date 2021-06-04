import React, { Component } from "react";
import { render } from "react-dom";
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    };
  }

  componentDidMount() {
    fetch("/api/v0.1/humans")
      .then(response => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then(data => {
        this.setState(() => {
          return {
            data,
            loaded: true
          };
        });
      });
  }

  render() {
    console.log(this.state.data);
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
                    <th>Phone</th>
                    <th>Email</th>
                    <th>Email_first</th>
                    <th>Description</th>
                </tr>
                </thead>
                <tbody>
                    {this.state.data.map(c =>
                    <tr  key={c.pk}>
                        <td>{c.pk}  </td>
                        <td>{c.nickname}</td>
                        <td>{c.name}</td>
                        <td>{c.surname}</td>
                        <td>{c.middle_name}</td>
                        <td>{c.phone}</td>
                        <td>{c.email}</td>
                        <td>{c.email_first}</td>
                        <td>{c.description}</td>
                        <td>
                        <button> Delete</button>
                        <a  href={"/human/" + c.pk}> Update</a>
                        </td>
                    </tr>)}
                </tbody>
            </table>
            <button  className="btn btn-primary" >Next</button>
        </div>
        );
    }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
