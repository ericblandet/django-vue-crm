<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">{{ client.name }}</h1>
        <div class="buttons">
          <router-link
            :to="{ name: 'EditClient', params: client.id }"
            class="button is-light"
            >Edit</router-link
          >
          <button @click="deleteClient()" class="button is-danger">
            Delete client
          </button>
        </div>
      </div>

      <div class="column is-6">
        <div class="box">
          <h2 class="subtitle">Details</h2>

          <p><strong>Created at:</strong> {{ client.created_at }}</p>
          <p><strong>Updated at:</strong> {{ client.updated_at }}</p>
        </div>
      </div>
      <div class="column is-6">
        <div class="box">
          <h2 class="subtitle">Contact information</h2>

          <p><strong>Contact Person:</strong> {{ client.contact_person }}</p>
          <p><strong>Email:</strong> {{ client.email }}</p>
          <p><strong>Phone:</strong> {{ client.phone }}</p>
          <p><strong>Website:</strong> {{ client.website }}</p>
        </div>
      </div>
      <hr />
      <div class="column is-12">
        <h2 class="subtitle">Notes</h2>
        <router-link
          :to="{ name: 'AddNote', params: client.id }"
          class="button is-success mb-6"
          >Add Note</router-link
        >
        <div class="box" v-for="note in notes" :key="note.id">
          <h3 class="is-size-4">{{ note.name }}</h3>

          <p>{{ note.body }}</p>
          <router-link
            :to="{
              name: 'EditNote',
              params: { id: client.id, note_id: note.id },
            }"
            >Edit note</router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from "axios";
  import { toast } from "bulma-toast";

  export default {
    name: "Client",
    data() {
      return {
        client: {},
        notes: [],
      };
    },
    mounted() {
      this.getClient();
    },
    methods: {
      async getClient() {
        this.$store.commit("setIsLoading", true);
        const clientId = this.$route.params.id;

        await axios
          .get(`/api/v1/clients/${clientId}/`)
          .then((response) => {
            this.client = response.data;
          })
          .catch((error) => {
            if (this.$store.state.debugMode) {
              console.log(error);
            }
          });

        await axios
          .get(`/api/v1/notes/?client_id=${clientId}`)
          .then((response) => {
            this.notes = response.data;
          })
          .catch((error) => {
            if (this.$store.state.debugMode) {
              console.log(error);
            }
          });

        this.$store.commit("setIsLoading", false);
      },
      async deleteClient() {
        this.$store.commit("setIsLoading", true);
        const clientId = this.$route.params.id;

        await axios
          .post(`/api/v1/clients/delete_client/${clientId}/`)
          .then((response) => {
            toast({
              message: "The client has been deleted",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });
            this.$router.push({ name: "Clients" });
          })
          .catch((error) => {
            if (this.$store.state.debugMode) {
              console.log(error);
            }
          });

        this.$store.commit("setIsLoading", false);
      },
    },
  };
</script>
