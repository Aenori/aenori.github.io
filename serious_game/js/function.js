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

function postDecision(team_name, decision_id, json_data) {
  $.ajax( {
    type: "POST",
    url: "/team-decision",
    data: JSON.stringify(
      {
        team_name: team_name,
        decision_id: decision_id,
        decision_json: json_data
    }),
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    success: function( data ) {
      if('errors' in data)
      {
        alert('Oups, il y a un ou des problèmes avec vos décisions :' + data['errors'].join(', '));
      }
      else
      {
        alert('Votre choix a bien été enregistré');
      }
    }
  });
}

function nextStep(step_id) {
  $.get("/current_step", function(data, status){
    var current_step = data["current_step"];

    if(current_step <= step_id) {
      alert("Attendez d'avoir l'instruction de passer à l'étape suivante");
    }
    else
    {
      window.location.pathname = '/team-next-step';
    }
  });
}
