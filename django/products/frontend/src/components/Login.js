import React, { Component } from 'react';
import {Link} from 'react-router-dom';

class Login extends Component {
  

    state ={
        credentials:{username:'',password:''}
    }
     
  login = event => {
    fetch('http://127.0.0.1:8000/account/login/', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(this.state.credentials)
    })
    .then( data => data.json())
    .then(
      data => {
        //   console.log(data.token);
         this.props.userLogin(data.token);
    }
    )
    .catch( error => console.error(error))
  }
  
    inputChanged = event => {
    const cred = this.state.credentials;
    cred[event.target.name] = event.target.value;
    this.setState({credentials: cred});
  }



    render(){
  return (
    <div className="App">
    <h1>Login User Form</h1>
    <label>
        UserName:
        <input type="text" name="username"
        value={this.state.credentials.username}
        onChange={this.inputChanged} />
    </label>
    <br/>
    <label>
       Password:
        <input type="password" name="password"
        value={this.state.credentials.password}
        onChange={this.inputChanged}
        />
    </label>
    <br/>
  
    <button onClick={this.login} className="btn btn-info">Login</button>
   
     <Link to='/register'>
      <button type="button" className="btn btn-info" style={{margin:'10px'}}>Register</button>
      </Link> 
    </div>
  );
}
}



export default Login;
