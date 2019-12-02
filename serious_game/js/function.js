function optimize() {
  var optimization_url = "/optim";
  var input_data = [];
  var i;
  for (i = 0; i < nb_hour; i++) { 
    input_data[i] = $('#H' + i + '-R1').val();
  }

  console.log(input_data);

  $.ajax( {
    type: "POST",
    url: optimization_url, 
    data: JSON.stringify({ input_data: input_data }),
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    success: function (data) {
      var i;
      for (i = 0; i < data.length; i++) { 
        $('#H' + i + '-R1').val(data[i]);
      }
    }
  });
}
