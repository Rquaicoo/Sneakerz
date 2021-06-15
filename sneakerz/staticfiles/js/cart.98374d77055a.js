var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log('productId :', productId, 'action :', action)

    console.log('USER :', user)
    if(user == 'AnonymousUser'){
        console.log('User is not authenticated')
    }
    else{
        updateUserOrder(productId, action)//checks whether a user is anonymous or not
    }

    })
}
//function for updating user order
function updateUserOrder(productId, action){
    console.log('User is authenticated, sending data...')

    
    var url = '/update_item/'  //data will be sent to this new view
        
    //sending the product iD to the new view created(update_items)
    
    //uisng fetch to send POST data
        fetch(url, {
        method: 'POST',
        headers: { //parsing header
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,  //adding the csrf token
        },
        
        //body is the data that will be sent to the backend sent as an object
        //stringify converts the objects to a string
        body: JSON.stringify({'productId' : productId, 'action': action})
    })
    .then((response) => {
            return response.json()
        })//returning response
        .then((data) =>{
            console.log('data: ', data) //consoling the data out
            location.reload() //reload the page once new data is passed
        })
}