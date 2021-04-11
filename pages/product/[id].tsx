import Head from 'next/head'
import { getProductsDetail } from '../../lib/products'
import ProductForm from '../../components/ProductForm'

export default function ProductDetail({ product }) {

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
        <ProductForm product={product} />
      </div>
    </div>
  )
}

export async function getServerSideProps({ params }) {

  const product = await getProductsDetail(params.id)

  return {
    props: {
      product
    }
  }
}
