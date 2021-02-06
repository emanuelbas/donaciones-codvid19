<template>
  <div>
  <div class="container">
    <div class="row">
      <div tabindex="30">
               <div class="col-sm-12">
                 <h2><b>¡Bienvenidos!</b></h2>
                 <h3>En ésta página web encontraras toda la informacion referente a los centros de ayuda
                  de la provincia de Buenos Aires. Ver centro de ayuda social en el mapa. 
                  Crear una solicitud de carga de un nuevo centro de ayuda social. Sección de
                  estadísticas en base a información de los centros de ayuda social.</h3>
              </div>
      </div>
                
      <div tabindex="31">
               <div class="col-sm-12 text-center"> 
                    <figure>
                        <img src="../assets/img22.jpg" alt="Imagen de una mujer blanca usando una mascarilla de protección. Un texto que dice, nuestro principal propósito es ayudar a quien mas lo necesita. Juntos somos más">
                     </figure>
                   </div>
                </div>


                </div>
      </div>
      <div tabindex="32">

               <div class="col-sm-12">
            
                <h3 style="font-family: 'Monoton'"><b>Ver Centro mas cercano</b></h3>
                <img src="../assets/mapas.png" alt="Icono que denota ubicación" style='height:100px'>
                <p>Dirección: Calle 12 286 - La PLata - Buenos Aires - Argentina <br>
                <a title="Abrir" href="https://caritaslaplata.org/">Haz click aquí para ver más información de este centro</a></p>
                <br><br>
                </div>

      </div>
      <div tabindex="33">

               <div class="col-sm-12">
            
                <h3 style="font-family: 'Monoton'"><b>Crear un nuevo centro de ayuda</b></h3>
                <img src="../assets/asistencia.png" alt="Icono que denota un centro de ayuda" style='height:100px'>
                <div>
                <router-link to="/alta_centro" class="btn btn-primary">Crear Centro</router-link>
                <br><br>
                </div>
                </div>

      </div>
    <footer id="footer">
    <div class="container">
        <div class="row">
            <div class="col-sm-12 text-center bottom-separator">
                  <div class="col-md-12 col-sm-12">
                    <div id="contacto" class="contact-form bottom">
                       <h2>Ponete en contacto con nosotros</h2>
                       <form id="main-contact-form" name="contact-form" method="" action="">
                        <div class="form-group">
                            <input tabindex="41" id="nombre" type="text" name="name"  class="form-control" required="required" placeholder="Nombre">
                        </div>
                        <div class="form-group">
                            <input tabindex="42" id="email" type="email" name="email"  class="form-control" required="required" placeholder="E-mail">
                        </div>
                        <div class="form-group">
                            <textarea tabindex="43" id="mensaje"  name="message" required="required" class="form-control" rows="8" placeholder="Escribe aquí tu mensaje..."></textarea>
                        </div>            
                        <div style="display:none"> 
                            <input id="correo" value="mayrukia@gmail.com" placeholder="E-mail"> 
                        </div>             
                        <div class="form-group">
                            <button tabindex="44" id="send-button" name="submit" class="btn btn-primary"> Enviar mensaje</button>
                        </div>
                    </form>
                    </div>
                </div>
            </div>
            <div class="col-sm-12">
                <p>@Grupo22</p>
            </div>
        </div>
    </div>
</footer>

    </div>
 

</template>