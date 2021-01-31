const typeInput = document.getElementById("product_type")

typeInput.addEventListener('change', e=>{
    console.log(e.target.value)
    const selectedType = e.target.value
    console.log(selectedType)
    $.ajax({
        type: 'GET',
        url: `product-json/${selectedType}/`,
        success: function(response){
            console.log(response.data)
            const productData = response.data
        },
        error: function(error){
            console.log(error)
        }
    })
})

            
