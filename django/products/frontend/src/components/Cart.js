import React, { useState, useEffect} from 'react';
import {Button} from 'react-bootstrap';
import {Link} from 'react-router-dom';

const Cart = () =>{
const [orderitems,setOrderitems] = useState([]);
useEffect( () => {
    fetch('http://localhost:8000/api/orders_items/',{
        method: 'GET',
        headers : {
            'content-Type': 'application/json',
            'Authorization':'Token d4d4fbc4676732a12004a93661fc2d9ed9a611a7'
        }
    })
    .then(resp => resp.json())
    .then(resp => setOrderitems(resp))
    .catch(error => console.log(error))
    // console.log(resp.json())

},[])
return (
    <div className="container">
        <br></br>
        <br></br>
        <br></br>
        <br></br>
        <h1 className="display">My Cart</h1>
        <br></br>
        <div className="row">
          
          
        {orderitems.map(order=> (
            
            <div className="col-md-4" key={order.id}>
            <div className="card" style={{marginBottom:"30px"}} >
                
              <img className="card-img-top" src={order.Product_Id.Image_Link} alt="Card image cap" style={{ height: '300px',width: 'auto'}} ></img>
              <div className="card-body">
               <h1 className="card-text text-dark text-center " style={{fontSize:"23px",fontWeight:"600"}}>{order.Product_Id.Title}</h1>
               <p className="card-text display-1 " style={{fontSize:"19px",fontWeight:"550"}}>qty:{order.Quantity}</p>
               <p className="card-text display-1 " style={{fontSize:"19px",fontWeight:"550"}}>Price:₹{order.Price}  </p>
           
                {/* <span className="lead"><span className="badge badge-primary float-right">Total:₹{order.final_price}</span>< /span> */}
              </div>
            </div>
            </div>
          ))}
        </div>
              <Link to='/buynow'>

   <Button variant="danger" size="md">
    Checkout
  </Button> </Link> 
      </div>
   
    );
  }

   
export default Cart;