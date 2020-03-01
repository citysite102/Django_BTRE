const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


// 每次修改都要 run python manage.py collectstatic
setTimeout(() => {
  $('#message').fadeOut('slow');
}, 3000);