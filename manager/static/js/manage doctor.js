const doctors = document.querySelector('.fa-user-doctor').parentElement;
console.log(doctors);

doctors.addEventListener('click',()=>{

  const list = document.querySelectorAll('.fa-user-doctor');
  Array.from(list).forEach((element,index)=>{
    if(index > 0 && element.parentElement.style.display === 'none')
    {
      console.log(element);
      element.parentElement.style.display = 'block';
      console.log('hello world');
      element.parentElement.style.transition= '5s display';  
      
    }
    else if(index > 0 && element.parentElement.style.display === 'block')
    {
      element.parentElement.style.display = 'none';
      element.parentElement.style.transition= '5s display';  
    }
   console.log('NONE');
  })



})