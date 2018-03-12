/*
  Autor: Luis Alfredo León Villapún
  Fecha de creación: 9/3/2018
*/

function SkillObject(myTechnology, myExpertise) {

    this.technology = myTechnology;
    this.expertise_level = myExpertise;

    this.toJsonString = function () { return JSON.stringify(this); }; //Parsear a JSON el objeto

};


//Usa una peticion GET para listar todos los comentarios
function getSkillList()
{
  try
  {
     $("#skills").empty();
     //Peticion ajax al backend
     jQuery.ajax({
           type: "GET", //List all the comments
           url: "http://18.217.204.145/skills/",
           success: function (response) {
             skills = response;
             //Create table headers
             var table ="<h2>Tecnologías</h2><br><center><table class ='info-box'>" +
             "<tr>" +
             "<th class='tg-yw4l'>Tecnología</th>" +
             "<th class='tg-yw4l'>Nivel</th>" +
             "</tr>";
             //$("#skills").append(tableHeader);

             //Append the rows of the response
             skills.forEach(function(skill){
               table = table + "<tr>" +
               "<td>"+ skill.technology +"</td>" +
               "<td>"+ skill.expertise_level +"</a></td>" +
               "</tr>";
             });

             //Close the table
             table = table + "</table></center>";

             $("#skills").append(table);

             $("#skills").show(1000);
             $("#menu").hide(1000);
             $("#menu2").hide(1000);
           },

           error: function(xhr, status, error) {
              alert(xhr.responseText);
           }

       });

   }
   catch(error)
   {
    alert(error);
   }

}
