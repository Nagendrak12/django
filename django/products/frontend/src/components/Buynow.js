import {Button,Modal } from 'react-bootstrap';
import React, { useState } from 'react';
import {Link} from 'react-router-dom';



const Buynow = () => {
    const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  return (
    <div>
      <Button variant="primary" onClick={handleShow}>
        Are you Sure?
      </Button>

      <Modal
        show={show}
        onHide={handleClose}
        backdrop="static"
        keyboard={false}
      >
        <Modal.Header closeButton>
          <Modal.Title>K12 Orders</Modal.Title>
        </Modal.Header>
        <Modal.Body>
         Order placed successfully.....
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          <Link to='/'>
          <Button variant="primary" >Ok</Button>
          </Link>
        </Modal.Footer>
      </Modal>
    </div>
  );

}

export default Buynow

 
  


