/*
  Autor: Luis Alfredo León Villapún
  Fecha de creación: 9/3/2018
*/

function ExperienciaLaboralObject(myTitle, myEmpresa, myDescripcion, myFechaInicio, myFechaFin) {

    this.title = myTitle;
    this.empresa = myEmpresa;
    this.descripcion = myDescripcion;
    this.fecha_inicio = myFechaInicio;
    this.fecha_fin = myFechaFin;

    this.toJsonString = function () { return JSON.stringify(this); }; //Parsear a JSON el objeto

};


//Usa una peticion GET para listar todos los comentarios
function getExperienciaList()
{
  try
  {
     $("#experiences").empty();
     //Peticion ajax al backend
     jQuery.ajax({
           type: "GET", //List all the comments
           url: "http://18.217.204.145/experience/",
           success: function (response) {
                experiences = response;
                //Create table headers
                var table ="<h2>Experiencia Laboral</h2><br><center><table class ='info-box'>" +
                "<tr>" +
                "<th class='tg-yw4l'>Trabajo</th>" +
                "<th class='tg-yw4l'>Empresa</th>" +
                "<th class='tg-yw4l'>Descripción</th>" +
                "<th class='tg-yw4l'>Fecha Inicio</th>" +
                "<th class='tg-yw4l'>Fecha Fin</th>" +
                "</tr>";
                //$("#experiences").append(tableHeader);

                //Append the rows of the response
                experiences.forEach(function(experience){
                  table = table + "<tr>" +
                  "<td>"+ experience.titulo +"</td>" +
                  "<td>"+ experience.empresa +"</td>" +
                  "<td>"+ experience.descripcion +"</td>" +
                  "<td>"+ experience.fecha_inicio +"</td>" +
                  "<td>"+ experience.fecha_fin +"</td>" +
                  "</tr>";
                });

                //Close the table
                table = table + "</table></center>";

                $("#experiences").append(table);

                $("#experiences").show(1000);
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
