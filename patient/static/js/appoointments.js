const search = document.querySelector('.search-bar');

let rows = document.querySelectorAll('table tr');
console.log(rows);
search.addEventListener('keyup',(event)=>{


let value = search.value.toLowerCase();
value = new String(value);
console.log(value);
for(i=1;i<rows.length;i++)
{
    let Target = rows[i].firstElementChild.innerText.toLowerCase();
    console.log('target = ' + Target)
    if(Target.startsWith(value))
    {
        rows[i].style.display = 'table-row';
    }else{
        rows[i].style.display = 'none';
    }
}
for(i=1;i<rows.length;i++)
{
    let Target = rows[i].firstElementChild.nextElementSibling.innerText.toLowerCase();
    console.log('target = ' + Target)
    if(Target.startsWith(value))
    {
        rows[i].style.display = 'table-row';
    }else{
        // rows[i].style.display = 'none';
    }
}





})