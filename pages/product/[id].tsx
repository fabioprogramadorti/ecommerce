import Head from 'next/head'
import styles from '../../styles/Home.module.css'
import { useState } from 'react'
import { getProductsDetail } from '../../lib/products'
import { Form, Button, Row, Col, InputGroup } from 'react-bootstrap'

export default function ProductDetail({ product }) {

  const [name, setName] = useState(product.name)
  const [description, setDescription] = useState(product.description)
  const [price, setPrice] = useState(product.price)
  const [published_at, setPublished_at] = useState(product.published_at)
  const [images, setImages] = useState(product.images)

  return (
    <div>
      <Head>
        <title>Product Detail</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <div className='container'>
        <h1 className='text-center'>
          Product Detail
        </h1>
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
                }}/>
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
                  }}/>
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

          <Button variant="success" type="submit">
            Save
          </Button>
          <Button variant="danger" type="submit" className="mx-2" >
            Cancel
          </Button>
        </Form>
        <div className={styles.grid}>

          <div className={styles.card}>
            <h3>
              Photos
            </h3>
           { images.map(image => (
            <img src={image} alt="" width="150px"/>
            ))}
          </div>

        </div>
      </div>
    </div>
  )
}

export async function getServerSideProps({ params }) {
  // Get external data from the file system, API, DB, etc.
  const product =  await getProductsDetail(params.id)

  // The value of the `props` key will be
  //  passed to the `Home` component
  return {
    props: {
      product
    }
  }
}
