import { useState } from "react"
import Link from "next/link"
import styles from "../../styles/Home.module.css"
import { getProductsData } from '../../lib/products'

export default function ProductList({ allProducts }) {

  const [products, setProducts] = useState(allProducts)

  return (
    <main className={styles.main}>
      <h1 className={styles.title}>
        All Products
      </h1>

      <div className={styles.grid}>
          {
          products.map(product => (
            <Link key={product.id} href={{
              pathname: "/product/" + product.id,
            }}>
                <a className={styles.card}>
                  <h3>{product.name}</h3>
                  <p>Description: {product.description}</p>
                  <p>Price: {product.price}</p>
                  <p>Published At: {product.published_at}</p>
                  {product.images.map(image => (
                    <img src={image} width="120px" height="100px"/>
                    ))}
              </a>
              </Link>
            ))
          }
      </div>
      </main>
  )
}

export async function getServerSideProps({ params }) {
  // Fetch necessary data for the repos using params.lang
  const allProducts = await getProductsData()

  return {
    props: {
      allProducts
    }
  }
}