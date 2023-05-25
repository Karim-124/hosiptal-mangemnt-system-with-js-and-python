let trash = document.querySelectorAll('.fa-trash');

// trash
for(i = 0;i<trash.length;i++)
{

  trash[i].addEventListener('click',(event)=>{
    let table = event.target;
    table = table.parentElement.parentElement
    console.log(table);
    table.remove();

  });



}







const search = document.querySelector('.search-bar');

let rows = document.querySelectorAll('table tr');
console.log(rows);
search.addEventListener('keyup',(event)=>{


let value = search.value.toLowerCase();
value = new String(value.toString());
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





})