import Head from 'next/head'
import styles from '../../styles/Home.module.css'
import { useState } from 'react'
// As a user, I want to create a product with at least these fields: name, description, price and published_at
// As a user, I want to upload one or more images to the product.
const product = {
  id: 1,
  name: 'MacBook',
  description: 'Laptop of Apple',
  price: 1200.21,
  published_at: '2020-11-11',
  images: [
    'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.a3cTF2kZNwANt9pgP_19WgHaF3%26pid%3DApi&f=1',
    'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.gTOu29SWTKbsxU0qhzzhpgHaEK%26pid%3DApi&f=1'
  ]
}


export default function ProductDetail() {

  const [name, setName] = useState(product.name)
  const [description, setDescription] = useState(product.description)
  const [price, setPrice] = useState(product.price)
  const [published_at, setPublished_at] = useState(product.published_at)
  const [images, setImages] = useState(product.images)

  return (
    <div className={styles.container}>
      <Head>
        <title>Product Detail</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          Product Detail
        </h1>

        <div className={styles.grid}>
          <div className={styles.card}>
            <h3>
              Name
            </h3>
            <input
              type="text"
              placeholder="Name"
              value={name}
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
              value={description}
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
              value={price}
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
              value={published_at}
              onChange={async (e) => {
                const { value } = e.currentTarget
                setPublished_at(value)
              }}
            />
          </div>

        </div>
      </main>

      <button type="submit">Save</button>
      <button type="submit">Cancel</button>
    </div>
  )
}
