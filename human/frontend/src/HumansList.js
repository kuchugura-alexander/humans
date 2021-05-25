import  React, { Component } from  'react';

import  HumansService  from  './HumansService';

const  humansService  =  new  HumansService();

class  HumansList  extends  Component {

    constructor(props) {
        super(props);
        this.state  = {
            humans: [],
            nextPageURL:  ''
        };
        this.nextPage  =  this.nextPage.bind(this);
        this.handleDelete  =  this.handleDelete.bind(this);
    }

    componentDidMount() {
        var  self  =  this;
        humansService.getHumans().then(function (result) {
            self.setState({ humans:  result.data, nextPageURL:  result.nextlink})
        });
    }

    handleDelete(e,pk){
        var  self  =  this;
        humansService.deleteHuman({pk :  pk}).then(()=>{
            var  newArr  =  self.state.humans.filter(function(obj) {
                return  obj.pk  !==  pk;
            });
            self.setState({humans:  newArr})
        });
    }

    nextPage(){
        var  self  =  this;
        humansService.getHumanrsByURL(this.state.nextPageURL).then((result) => {
            self.setState({ humans:  result.data, nextPageURL:  result.nextlink})
        });
    }

    render() {

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
                    {this.state.humans.map( c  =>
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
                            <button  onClick={(e)=>  this.handleDelete(e,c.pk) }> Delete</button>
                            <a  href={"/human/" + c.pk}> Update</a>
                        </td>
                    </tr>)}
                </tbody>
            </table>
            <button  className="btn btn-primary"  onClick=  {  this.nextPage  }>Next</button>
        </div>
        );
    }
}
export  default  HumansList;
