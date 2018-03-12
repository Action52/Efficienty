/*
  Autor: Luis Alfredo León Villapún
  Fecha de creación: 9/3/2018
*/

var urlRest = "http://18.217.204.145/comments/";

function CommentObject(myNickname, myComment) {

    this.nickname = myNickname;
    this.comment = myComment;
    this.toJsonString = function () { return JSON.stringify(this); }; //Parsear a JSON el objeto

};

function goToComments(){
  window.location = "/#comentarios";
}

function goToMenu(){
  $("#menu").show();
  $("#menu2").show();
  $("#experiences").hide(1000);
  $("#projects").hide(1000);
  $("#skills").hide(1000);
  $("#leaderships").hide(1000);
}


function addComment()
{
	try
  {
  	var myData = new CommentObject(
      $("#nickname").val(),
      $("#comment").val(),
    );
  	alert(myData.toJsonString());

  	 jQuery.ajax({
           type: "POST",
           url: urlRest,
           data: myData.toJsonString(), //Lo convertimos a json para que el back lo reciba así
           success: function (response) {
                $("#listaComentarios").empty();
                getCommentList();
           },

           error: function (error) {
                // error handler
                alert("error :" + error.message)
           }

       });

   }
   catch(error)
   {
    alert(error);
   }

}



//Usa una peticion GET para listar todos los comentarios
function getCommentList()
{
  try
  {
     $("#listaComentarios").empty();
     //Peticion ajax al backend
     jQuery.ajax({
           type: "GET", //List all the comments
           url: urlRest,
           success: function (response) {

             comments = response;
             //Create table headers
             var table ="<h3><br><center><table class ='info-box'>" +
             "<tr>" +
             "<th class='tg-yw4l'>Usuario</th>" +
             "<th class='tg-yw4l'>Comentario</th>" +
             "<th class='tg-yw4l'>Fecha</th>" +
             "</tr>";
             //$("#comments").append(tableHeader);

             //Append the rows of the response
             comments.forEach(function(comment){
               table = table + "<tr>" +
               "<td>"+ comment.nickname +"</td>" +
               "<td>"+ comment.comment +"</td>" +
               "<td>"+ comment.date +"</td>" +
               "</tr>";
             });

             //Close the table
             table = table + "</table></center></h3>";

             $("#listaComentarios").append(table);
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
