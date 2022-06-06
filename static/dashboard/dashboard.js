function delete_category(id){
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