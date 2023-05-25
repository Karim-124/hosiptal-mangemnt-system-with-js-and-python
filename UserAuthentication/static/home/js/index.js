let password = document.getElementById('password');
let container = document.querySelector('.eye');
let eye = ['fa-regular fa-eye','fa-regular fa-eye-slash']
let i = 0;

let change = ()=>{

    defaultEye.classList.toggle('fa-eye-slash');

};


container.addEventListener('click',(event)=>{
        // 'use strict';
    // event.preventDefault();
        
//    defaultEye.classList.toggle('fa-eye');
   
    const showHideEye = container.firstElementChild;
    if(showHideEye.classList.contains('fa-eye'))
        {
            showHideEye.classList.remove('fa-eye');
            showHideEye.classList.add('fa-eye-slash');
        }
        else{
            showHideEye.classList.remove('fa-eye-slash');
            showHideEye.classList.add('fa-eye');
        
        }

    if(password.type === 'password')
    {
        password.type = 'text';
    }else{
        password.type = 'password';
    }


});