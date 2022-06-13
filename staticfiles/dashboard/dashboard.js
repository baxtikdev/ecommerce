function delete_category(id){
    console.log(id)
    url=`/dashboard/delete_category/`
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            'id':id
        })
        })
        .then((response)=>{
        response.json().then((data) => {
        })
        document.getElementById('delete_category'+id).style.display = 'none'
    })
}

function delete_user(id){
    url=`/dashboard/delete_user/`
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            'id':id
        })
        })
        .then((response)=>{
        response.json().then((data) => {
            if(data['status']=='ok'){
                document.getElementById('delete_user'+id).style.display = 'none'
            }
            else {
                alert("Foydalanuvchi o'chirilmadi")
            }
        })
    })
}