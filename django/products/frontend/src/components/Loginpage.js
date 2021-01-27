import React, { useState } from 'react';
import Login from './Login';

const Loginpage = () => {

    const [token,setToken] = useState('')
    const userLogin = (tok) =>{
    setToken(tok);
    console.log(tok);
  }
    return (
    <div className="App">
   
    <Login userLogin={userLogin}/>
     {token}
        </div>
    )
}

export default Loginpage;
