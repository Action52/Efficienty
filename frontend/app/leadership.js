/*
  Autor: Luis Alfredo León Villapún
  Fecha de creación: 9/3/2018
*/

function LeadershipObject(myDate, myDescripcion) {

    this.date = myDate;
    this.descripcion = myDescripcion;

    this.toJsonString = function () { return JSON.stringify(this); }; //Parsear a JSON el objeto

};


//Usa una peticion GET para listar todos los comentarios
function getLeadershipList()
{
  try
  {
     //Peticion ajax al backend
     jQuery.ajax({
           type: "GET", //List all the comments
           url: "http://localhost:8000/leadership/",
           success: function (response) {
             leaderships = response;
             //Create table headers
             var table ="<h2>Liderazgo</h2><br><center><table class ='info-box'>" +
             "<tr>" +
             "<th class='tg-yw4l'>Fecha</th>" +
             "<th class='tg-yw4l'>Descripción</th>" +
             "</tr>";
             //$("#leaderships").append(tableHeader);

             //Append the rows of the response
             leaderships.forEach(function(leadership){
               table = table + "<tr>" +
               "<td>"+ leadership.date +"</td>" +
               "<td>"+ leadership.descripcion +"</a></td>" +
               "</tr>";
             });

             //Close the table
             table = table + "</table></center>";

             $("#leadership").append(table);

             $("#leadership").show(1000);
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
