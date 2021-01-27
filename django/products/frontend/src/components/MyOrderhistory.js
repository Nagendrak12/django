import React, { useState, useEffect} from 'react';

const MyOrderhistory = () =>{
const [myorders,setOrders] = useState([]);
useEffect( () => {
    fetch('http://127.0.0.1:8000/api/orders/',{
        method: 'GET',
        headers : {
            'content-Type': 'application/json',
            'Authorization':'Token f4d5007d07ec1e4c62bdfcfa847d44b27bd1a5e9'
        }
    })
    .then(data => data.json())
    .then(data => setOrders(data))
    .catch(error => console.log(error))
    

},[])
return (
    <div>
    {myorders.map(order => {

        return(
        <div className="card" style={{width: '22rem',margin:'30px'}}>       
        <p key={order.id}>Order id:{order.id}</p>
        <p>Status:{order.Order_Status}</p>
         <p key={order.id}>Mode of Payment:{order.Mode_of_Payment}</p>
        

        </div>)
    }

    )}

    </div>
)
}
export default MyOrderhistory;

