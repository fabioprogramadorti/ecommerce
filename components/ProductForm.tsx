import { Form, Button, Col, InputGroup } from 'react-bootstrap'
import { useState } from 'react'

export default function ProductForm(props) {

  const [name, setName] = useState(props.product.name)
  const [description, setDescription] = useState(props.product.description)
  const [price, setPrice] = useState(props.product.price)
  const [published_at, setPublished_at] = useState(props.product.published_at)
  const [images, setImages] = useState(props.product.images)

  return (
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
      </Form.Group>

      <div>
        <h3>
          Photos
        </h3>
        {images.map(image => (
          <img src={image} alt="" width="150px" />
        ))}
      </div>

      <Button variant="success" type="submit" className="my-2">
        Save
      </Button>
      <Button variant="danger" type="submit" className="mx-2" >
        Cancel
      </Button>
      
    </Form>
  )
}