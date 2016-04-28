$('#controller button').on('click', function(){
  var class_name = $(this).attr('id');
  $(this).addClass('selected').siblings().removeClass();
  $('#container').attr('class', class_name);
});