const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();


// 每次修改都要 run python manage.py collectstatic 然後重啟 server
setTimeout(() => {
  $('#message').fadeOut('slow');
}, 3000);