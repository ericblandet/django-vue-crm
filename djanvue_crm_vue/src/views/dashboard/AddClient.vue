<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Add Client</h1>
      </div>
      <div class="column is-12">
        <form>
          <div class="field">
            <label for="name">Name</label>
            <div class="control">
              <input type="text" name="name" class="input" v-model="name" />
            </div>
          </div>
          <div class="field">
            <label for="contact_person">Contact Person</label>
            <div class="control">
              <input
                type="text"
                name="contact_person"
                class="input"
                v-model="contact_person"
              />
            </div>
          </div>
          <div class="field">
            <label for="email">Email</label>
            <div class="control">
              <input type="email" name="email" class="input" v-model="email" />
            </div>
          </div>
          <div class="field">
            <label for="phone">Phone</label>
            <div class="control">
              <input type="text" name="phone" class="input" v-model="phone" />
            </div>
          </div>
          <div class="field">
            <label for="website">Website</label>
            <div class="control">
              <input
                type="text"
                name="website"
                class="input"
                v-model="website"
              />
            </div>
          </div>
          <div class="field">
            <div class="control">
              <button class="button is-success" @click.prevent="submitForm()">
                Submit
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
    name: "AddClient",
    data() {
      return {
        name: "",
        contact_person: "",
        email: "",
        phone: "",
        website: "",
      };
    },
    methods: {
      async submitForm() {
        this.$store.commit("setIsLoading", true);

        const client = {
          name: this.name,
          contact_person: this.contact_person,
          email: this.email,
          phone: this.phone,
          website: this.website,
        };

        await axios
          .post("/api/v1/clients/", client)
          .then((response) => {
            toast({
              message: "The client was added !",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });

            this.$router.push("/dashboard/clients");
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
