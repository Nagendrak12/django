import React, { Component} from 'react';
import {CardDeck,Card,Button,Badge,Container} from 'react-bootstrap';
import {Link} from 'react-router-dom';
import './Styles.css';

class Products extends Component {

  state = {
    products: []
  }
  loadProducts = () => {
    fetch('http://127.0.0.1:8000/api/products/', {
      method: 'GET',
      body: JSON.stringify(this.state.credentials)
    })
    .then( data => data.json())
    .then(
      data => {
        // console.log(data);
        this.setState({products : data })
      }
    )
    .catch( error => console.error(error))
  }

  render() {
    return (

<Container  className='card-deck'>
    {this.loadProducts()}
   
    {this.state.products.map((items) => (
      
    <CardDeck  style={{ width: '22rem',marginLeft: '10px'}} >    
    <p key={items.id}></p>
    <Card style={{margin:'10px'}}>
    <Card.Img className="card-img-top" variant="top" src={items.Image_Link} />
    <Card.Body>
      <Card.Title>{items.Title}</Card.Title>        
      <Card.Text>
     Description:{items.Description}
     
      </Card.Text>
      <h3> <Badge pill variant="info">
    Price:₹{items.Product_Price}
  </Badge>{' '} </h3>
      
</Card.Body>
    <Card.Footer>
    <Link to='/buynow'>
    <Button variant="primary" size="md">
   Buy Now
  </Button></Link>  {' '}
  <Link to='/cart'>

   <Button variant="primary" size="md">
    Add to Cart
  </Button> </Link>  
    </Card.Footer>
</Card>
  </CardDeck>
    ))}
     </Container>



 );

  }
}

export default Products;









   {/* {this.loadProducts()}
    {this.state.products.map((item) => (
  <div className="card" key={item.id}>
                        <div className="card-image">
                            <img src={item.img} alt="Not Available"/>
                            <span className="card-title">{item.Title}</span>
                            <span to="/" className="btn-floating halfway-fab waves-effect waves-light red" onClick={()=>{this.handleClick(item.id)}}><i className="material-icons">add</i></span>
                        </div>

                        <div className="card-content">
                            <p>{item.Description}</p>
                            <p><b>Price: ₹{item.Product_Price}/-</b></p>
                        </div>
                 </div>
                 
    ))}

</div> */}