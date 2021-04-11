import '../styles/globals.css'
import Link from 'next/link'
import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import { Navbar, Nav, NavDropdown, Form, Button, FormControl } from 'react-bootstrap';
function MyApp({ Component, pageProps }) {
  return (
    <div>
      <Navbar bg="light" expand="lg">
        <Navbar.Brand href="/">Ecommerce</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="mr-auto">
            <Nav.Link href="/">Home</Nav.Link>
            <Nav.Link href="/product/list">My Products</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Navbar>
      <Component {...pageProps} />
    </div>
      )
}

export default MyApp
