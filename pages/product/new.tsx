import Head from 'next/head'
import ProductForm from '../../components/ProductForm'

export default function NewProduct() {

  
  const newProduct = {
    name:"",
    description:"",
    price:0,
    published_at:"",
    images:[]
  }

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
        <ProductForm product={newProduct} new/>
      </div>
    </div>
  )
}
