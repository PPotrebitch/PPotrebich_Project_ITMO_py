function updateTask(el){
    task_id = el.value
    fetch('/read/' + task_id, {
        method: 'patch',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'read': el.checked})
    })
}

function createTask(){
    console.log('Create')
    let author = document.getElementById('author').value
    let name_book = document.getElementById('name_book').value
    fetch('/task', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'author': author || "Пустое", 'name_book': name_book || "Пустое", 'read': false})
    })
}