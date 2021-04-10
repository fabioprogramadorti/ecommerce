import Head from 'next/head'
import styles from '../../styles/Home.module.css'
import { useState } from 'react'
// As a user, I want to create a product with at least these fields: name, description, price and published_at
// As a user, I want to upload one or more images to the product.

export default function NewProduct() {
  const [name, setName] = useState("")
  const [description, setDescription] = useState("")
  const [price, setPrice] = useState(0.0)
  const [published_at, setPublished_at] = useState("")
  const [images, setImages] = useState([])
  
  const newProduct = {
    name,
    description,
    price,
    published_at,
    images
  }

  return (
    <div className={styles.container}>
      <Head>
        <title>Create New Product</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          New Product
        </h1>

        <div className={styles.grid}>
          <div className={styles.card}>
            <h3>
              Name
            </h3>
            <input
              type="text"
              placeholder="Name"
              onChange={async (e) => {
                const { value } = e.currentTarget
                setName(value)
              }}
            />
          </div>

          <div className={styles.card}>
            <h3>
              Description
            </h3>
            <textarea
              placeholder="description"
              onChange={async (e) => {
                const { value } = e.currentTarget
                setDescription(value)
              }}
            />
          </div>

          <div className={styles.card}>
            <h3>
              Price
            </h3>
            <input
              type="number"
              placeholder="Price"
              onChange={async (e) => {
                const { value } = e.currentTarget
                setPrice(parseFloat(value))
              }}
            />
          </div>
          <div className={styles.card}>
            <h3>
              Published At
            </h3>
            <input
              type="date"
              placeholder="Published At"
              onChange={async (e) => {
                const { value } = e.currentTarget
                setPublished_at(value)
              }}
            />
          </div>

        </div>
      </main>

     <button type="submit">Submit</button>
    </div>
  )
}
