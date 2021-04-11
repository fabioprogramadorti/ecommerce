import { useState } from "react"
import Link from "next/link"
import styles from "../../styles/Home.module.css"
import { getProductsData } from '../../lib/products'
import { Card, Button } from "react-bootstrap"

export default function ProductList({ allProducts }) {

  const [products, setProducts] = useState(allProducts)

  return (
    <div className='container'>
      <h1 className="text-center">
        My Products
      </h1>

      <div className={styles.grid}>
          {
          products.map(product => (

            <Card style={{ width: '18rem' }} key={product.id}>
              <Card.Img width="150px" variant="top" src={product.images[0]} />
              <Card.Body>
                <Card.Title>{product.name}</Card.Title>
                <Card.Text>
                 {product.description}
                </Card.Text>
                <Card.Text>
                  ${product.price}
                </Card.Text>
                <Button variant="primary">
                  <Link key={product.id} href={{
                    pathname: "/product/" + product.id,
                  }}>
                  <a className="text-light">Edit</a>
                  </Link>
                </Button>
              </Card.Body>
            </Card>
            ))
          }
      </div>
      </div>
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