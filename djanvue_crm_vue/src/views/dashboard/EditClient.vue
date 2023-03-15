<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">{{ client.company }}</h1>
      </div>

      <div class="column is-12">
        <form>
          <div class="field">
            <label for="name">Name</label>
            <div class="control">
              <input
                type="text"
                name="name"
                class="input"
                v-model="client.name"
              />
            </div>
          </div>
          <div class="field">
            <label for="contact_person">Contact Person</label>
            <div class="control">
              <input
                type="text"
                name="contact_person"
                class="input"
                v-model="client.contact_person"
              />
            </div>
          </div>
          <div class="field">
            <label for="email">Email</label>
            <div class="control">
              <input
                type="email"
                name="email"
                class="input"
                v-model="client.email"
              />
            </div>
          </div>
          <div class="field">
            <label for="phone">Phone</label>
            <div class="control">
              <input
                type="text"
                name="phone"
                class="input"
                v-model="client.phone"
              />
            </div>
          </div>
          <div class="field">
            <label for="website">Website</label>
            <div class="control">
              <input
                type="text"
                name="website"
                class="input"
                v-model="client.website"
              />
            </div>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-success" @click.prevent="submitForm()">
                Update
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from "axios";
  import { toast } from "bulma-toast";

  export default {
    name: "EditClient",
    data() {
      return {
        client: {},
      };
    },
    mounted() {
      this.getClient();
    },
    methods: {
      async getClient() {
        this.$store.commit("setIsLoading", true);

        const clientId = this.$route.params.id;
        axios
          .get(`/api/v1/clients/${clientId}`)
          .then((response) => {
            this.client = response.data;
          })
          .catch((error) => {
            if (this.$store.state.debugMode) {
              console.log(error);
            }
          });

        this.$store.commit("setIsLoading", false);
      },
      async submitForm() {
        this.$store.commit("setIsLoading", true);

        const clientId = this.$route.params.id;
        axios
          .patch(`/api/v1/clients/${clientId}/`, this.client)
          .then((response) => {
            toast({
              message: "The client was updated !",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });

            this.$router.push(`/dashboard/clients/${clientId}`);
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
