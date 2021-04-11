import Head from 'next/head'
import styles from '../../styles/Home.module.css'
import { useState } from 'react'
import { getProductsDetail } from '../../lib/products'


export default function ProductDetail({ product }) {

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
          <div className={styles.card}>
            <h3>
              Photos
            </h3>
           { images.map(image => (
            <img src={image} alt="" width="150px"/>
            ))}
          </div>

        </div>
      </main>

      <button type="submit">Save</button>
      <button type="submit">Cancel</button>
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
