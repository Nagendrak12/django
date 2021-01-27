import { BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import Loginpage from './Loginpage';
import Register from './Register';
import Buynow from './Buynow';
import {Button,Navbar,Nav,Form,FormControl } from 'react-bootstrap';
import Products from './Products';
import MyOrderhistory from './MyOrderhistory';
import Cart from './Cart';
import { MDBIcon} from "mdbreact";


const Navbarmain = () => {

    return (
        
        <Router>
            <div> 
                
    <Navbar bg="dark" variant="dark">
    <Navbar.Brand >K12Kart</Navbar.Brand>
    <Nav className="mr-auto">
      <Nav.Link href="/">Home</Nav.Link>
      <Nav.Link href="/orders">Order History</Nav.Link>
      <Nav.Link href="/login">Login</Nav.Link>
     <Nav.Link href="/cart" > <MDBIcon icon="shopping-cart" /> Cart </Nav.Link>
    </Nav>
    <Form inline>
      <FormControl type="text" placeholder="Search" className="mr-sm-2" />
      <Button variant="outline-info">Search</Button>
    </Form>
  </Navbar>

                <Switch>
                    <Route exact path="/"><Products /></Route>
                    <Route path="/login"><Loginpage /></Route>
                    <Route path="/register"><Register /></Route>
                    <Route path="/orders"><MyOrderhistory /></Route>
                    <Route path="/buynow"><Buynow /></Route>
                     <Route path="/cart"><Cart /></Route>
                    <Route path="/*"><PageNotFound/></Route>

                   
                </Switch>
            </div>

        </Router>
    );
}

function PageNotFound() {
    return(
        <div className="fusion-column col-lg-12 col-md-4 col-sm-4">
       Oops, This Page Could Not Be Found!
        <div className="error-message display-4">
        404
        </div>
       </div>
    )

}

export default Navbarmain; 


























