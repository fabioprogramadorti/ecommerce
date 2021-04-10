import { useState } from 'react'
import Link from 'next/link'
import styles from '../../styles/Home.module.css'

const productList = [
  {
    id: 1,
    name: 'IPhone',
    description: 'Smarth Phone of Apple',
    price: 300.21,
    published_at: '11-11-2020',
    images: [
      'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQG3vHiKJOCNSbjXNuK-lN1H0ZvLy2ag40Jx7tceflpE9WOLZwkjkouMhIzooImpdmqXdVBMZFy&usqp=CAc',
      'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.gkBl7j0_GL3uZ9nODBTeDAHaKX%26pid%3DApi&f=1'
    ]
  },
  {
    id: 2,
    name: 'MacBook',
    description: 'Laptop of Apple',
    price: 1200.21,
    published_at: '11-11-2020',
    images: [
      'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.a3cTF2kZNwANt9pgP_19WgHaF3%26pid%3DApi&f=1',
      'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.gTOu29SWTKbsxU0qhzzhpgHaEK%26pid%3DApi&f=1'
    ]
  }
]

export default function ProductList() {
  
  const [products, setProducts] = useState(productList)

  return (
    <main className={styles.main}>
      <h1 className={styles.title}>
        All Products
      </h1>

      <div className={styles.grid}>
          {
          products.map(product => (
            <Link href={{
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