var upudateBtns = document.getElementsByClassName('update-cart')

for(var i=0; i<upudateBtns.length; i++){
    upudateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('Item added: ', productId, 'Action: ', action)

        console.log('User: ',user)
        if(user == 'AnonymousUser'){
            console.log('User is not autheticated')
        }else{
            updateUserOrder(productId, action)
        }
    })
}
async function updateUserOrder(productId, action){
    console.log('User is authenticated, sending data...')
    var url = '/update_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
    // .catch((err) => {
    //     console.error(err)
    // })
}