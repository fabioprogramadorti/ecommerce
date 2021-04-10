export async function getProductsData() {

  const response = await fetch('https://ecommerce.free.beeceptor.com/product/list')
  const data = await response.json()
  return data.products
}
export async function getProductsDetail(id) {

  const response = await fetch(`https://ecommerce.free.beeceptor.com/product/${id}`)
  const data = await response.json()
  return data.product
}