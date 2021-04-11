import { Form, Button, Col, InputGroup, Container, Row, Image } from 'react-bootstrap'
import { useState } from 'react'
import Link from 'next/link'

function createProduct(product) {
  fetch('http://localhost/product/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify(product)
  })
}

function updateProduct(product) {
  fetch('http://localhost/product/', {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json;charset=utf-8'
    },
    body: JSON.stringify(product)
  })
}

export default function ProductForm(props) {

  const [name, setName] = useState(props.product.name)
  const [description, setDescription] = useState(props.product.description)
  const [price, setPrice] = useState(props.product.price)
  const [published_at, setPublished_at] = useState(props.product.published_at)
  const [images, setImages] = useState(props.product.images)
  const product = {
    name, description, price, published_at, images
  }
  return (
    <Container>
      <Form>
        <Form.Row>
          <Form.Group as={Col} controlId="formGridName">
            <Form.Label>Name</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter Name"
              value={name}
              onChange={async (e) => {
                const { value } = e.currentTarget
                setName(value)
              }} />
          </Form.Group>

          <Form.Group as={Col} controlId="formGridPrice">
              <Form.Label>Price</Form.Label>
              <InputGroup hasValidation>
                <InputGroup.Prepend>
                  <InputGroup.Text id="inputGroupPrepend">$</InputGroup.Text>
                </InputGroup.Prepend>
                <Form.Control
                  type="number"
                  placeholder="Price"
                  min='0'
                  value={price}
                  onChange={async (e) => {
                    const { value } = e.currentTarget
                    setPrice(parseFloat(value))
                  }} />
              </InputGroup>
            </Form.Group>
          <Form.Group as={Col} controlId="formGridCity">
            <Form.Label>Published At</Form.Label>
            <Form.Control
              type='date'
              value={published_at}
              onChange={async (e) => {
                const { value } = e.currentTarget
                setPublished_at(value)
              }}
            />
          </Form.Group>
        </Form.Row>

        <Form.Group controlId="formGridDescription1">
          <Form.Label>Description</Form.Label>
          <Form.Control
              as="textarea"
              rows={3}
              value={description}
              onChange={async (e) => {
                const { value } = e.currentTarget
                setDescription(value)
              }}
          />

          <Form.Group className="my-2">
            <Form.File id="FormControlFile1" label="Escolha uma Foto" custom multiple />
          </Form.Group>

        </Form.Group>

        <Button variant="success" type="submit" className="my-2"
          onClick={_ => {
            props.new ?
              createProduct(product)
            : updateProduct(product)
          }}>
          Save
        </Button>
        
        <Link href='/'>
          <a >
            <Button variant="danger" type="submit" className="mx-2" >
              Cancel
            </Button>
          </a>
        </Link>
      
      </Form>
      
        <h4 className="my-3">
          Photos
        </h4>
      <Row>
        {images.map(image => (
          <Col xs={6} md={4}>
            <Image src={image} thumbnail  width={120}/>
          </Col>
          
        ))}
      </Row>
    </Container>

      )
}