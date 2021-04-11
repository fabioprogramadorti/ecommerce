export async function getProductsData() {

  const response = await fetch('http://localhost/product/list')
  const data = await response.json()
  return data.products
}
export async function getProductsDetail(id) {

  const response = await fetch(`http://localhost/product/?id=${id}`)
  const data = await response.json()
  return data.product
}