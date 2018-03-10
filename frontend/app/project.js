/*
  Autor: Luis Alfredo León Villapún
  Fecha de creación: 9/3/2018
*/

function ProjectObject(myTitle, myRepo, myDescripcion, myFechaInicio, myFechaFin) {

    this.title = myTitle;
    this.repository_link = myRepo;
    this.descripcion = myDescripcion;
    this.fecha_inicio = myFechaInicio;
    this.fecha_fin = myFechaFin;

    this.toJsonString = function () { return JSON.stringify(this); }; //Parsear a JSON el objeto

};


//Usa una peticion GET para listar todos los comentarios
function getProjectList()
{
  try
  {
     //Peticion ajax al backend
     jQuery.ajax({
           type: "GET", //List all the comments
           url: "http://localhost:8000/projects/",
           success: function (response) {
             projects = response;
             //Create table headers
             var table ="<h2>Proyectos</h2><br><center><table class ='info-box'>" +
             "<tr>" +
             "<th class='tg-yw4l'>Proyecto</th>" +
             "<th class='tg-yw4l'>Link</th>" +
             "<th class='tg-yw4l'>Descripción</th>" +
             "<th class='tg-yw4l'>Fecha Inicio</th>" +
             "<th class='tg-yw4l'>Fecha Fin</th>" +
             "</tr>";
             //$("#projects").append(tableHeader);

             //Append the rows of the response
             projects.forEach(function(project){
               table = table + "<tr>" +
               "<td>"+ project.titulo +"</td>" +
               "<td><a href='"+ project.repository_link+"'>" + project.repository_link +"</a></td>" +
               "<td>"+ project.descripcion +"</td>" +
               "<td>"+ project.fecha_inicio +"</td>" +
               "<td>"+ project.fecha_fin +"</td>" +
               "</tr>";
             });

             //Close the table
             table = table + "</table></center>";

             $("#projects").append(table);

             $("#projects").show(1000);
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
