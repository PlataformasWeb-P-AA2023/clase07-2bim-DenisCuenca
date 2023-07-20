<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">

            <div class="form-group">
                <label for="ciudad">Ciudad</label>
                <input
                    type="text"
                    class="form-control"
                    id="ciudad"
                    v-model="edificio.ciudad"
                    v-validate="'required'"
                    name="ciudad"
                    placeholder="Ingres la ciudad"
                    :class="{'is-invalid': errors.has('edificio.ciudad') && submitted}">
                <div class="invalid-feedback">
                    Ciudad no valida.
                </div>
            </div>


          <div class="form-group">
                <label for="nombre">Nombre</label>
                <input
                    type="text"
                    class="form-control"
                    id="nombre"
                    v-model="edificio.nombre"
                    v-validate="'required'"
                    name="nombre"
                    placeholder="Ingres su nombre"
                    :class="{'is-invalid': errors.has('edificio.nombre') && submitted}">
                <div class="invalid-feedback">
                    nombre no valida.
                </div>
            </div>
  <div class="form-group">
                <label for="direccion">Dirección</label>
                <input
                    type="text"
                    class="form-control"
                    id="direccion"
                    v-model="edificio.direccion"
                    v-validate="'required'"
                    name="direccion"
                    placeholder="Ingres la dirección"
                    :class="{'is-invalid': errors.has('edificio.direccion') && submitted}">
                <div class="invalid-feedback">
                    direccion no valida.
                </div>
            </div>
          <div class="form-group">
                <label for="tipo">Tipo</label>
                <input
                    type="text"
                    class="form-control"
                    id="tipo"
                    v-model="edificio.tipo"
                    v-validate="'required'"
                    name="tipo"
                    placeholder="Ingres el tipo"
                    :class="{'is-invalid': errors.has('edificio.tipo') && submitted}">
                <div class="invalid-feedback">
                    tipo valido.
                </div>
            </div>




            <button type="submit" class="btn btn-primary">Crear</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            edificio: {
                nombre: '',
                direccion: '',
                ciudad: '',
                tipo: '',
                // url: '',
            },
            submitted: false
        }
    },
    mounted() {
        // this.getEdificio(),
        axios.get('http://localhost:8000/edificios/' + this.$route.params.id + '/')
            .then( response => {
                console.log(response.data)
                this.edificio = response.data
        });
    },
    methods: {


        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios.put(`http://localhost:8000/edificios/${this.$route.params.id}/`,
                        this.edificio
                    )
                    .then(response => {
                        this.$router.push('/');
                    })
            });
        }
    },
}
</script>
