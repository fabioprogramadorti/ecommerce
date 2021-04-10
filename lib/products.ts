export async function getProductsData() {

  const response = await fetch('https://ecommerce.free.beeceptor.com/product/list')
  const data = await response.json()
  return data.products
}