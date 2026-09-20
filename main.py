#Working with Float
from pyscript import display, document

#Calculate the subtotal items
def create_order (e):
        prod1 = document.getElementById("item1")
        prod2 = document.getElementById("item2")
        prod3 = document.getElementById("item3")
        prod4 = document.getElementById("item4")
        prod5 = document.getElementById("item5")
        prod6 = document.getElementById("item6")
        prod7 = document.getElementById("item7")

        subtotal = float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked + float(prod5.value) * prod5.checked + float(prod6.value) * prod6.checked +  float(prod7.value) * prod7.checked

        #Input the value of VAT
        VAT= subtotal * 0.12
        display('VAT', target='result')

        #Calculate the subtotal and the value of VAT; compute for the total
        document.getElementById('result').innerHTML = " "
        Total = subtotal + VAT
        display(Total, target='result')

#Generating SKU
def generate_sku (e):

        category = document.getElementById('category').value
        product = document.getElementById('product').value

        # Get first 3 letters of product
        product= product[0:3]

        # Get first 3 letters of category
        category= category[0:3]

        # Convert to uppercase
        product= product.upper()
        category = category.upper()

        #Generate sku
        sku = category + '-' + product + '-001'

        # Display the SKU
        document.getElementById("result").innerHTML = sku