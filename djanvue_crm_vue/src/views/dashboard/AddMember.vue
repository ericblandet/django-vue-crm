<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Add Member</h1>
      </div>

      <form @submit.prevent="submitForm">
        <div class="field">
          <label for="email">Email</label>
          <div class="control">
            <input type="email" name="email" class="input" v-model="username" />
          </div>
        </div>
        <div class="field">
          <label for="password1">Password</label>
          <div class="control">
            <input
              type="password"
              name="password1"
              class="input"
              v-model="password1"
            />
          </div>
        </div>
        <div class="field">
          <label for="password2">Repeat Password</label>
          <div class="control">
            <input
              type="password"
              name="password2"
              class="input"
              v-model="password2"
            />
          </div>
        </div>

        <div class="notification is-danger" v-if="errors.length">
          <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
        </div>

        <div class="field">
          <div class="control">
            <button class="button is-success">Submit</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
  import axios from "axios";
  import { toast } from "bulma-toast";

  export default {
    name: "AddMember",
    data() {
      return {
        username: "",
        password1: "",
        password2: "",
        errors: [],
      };
    },
    methods: {
      async submitForm() {
        this.$store.commit("setIsLoading", true);
        this.errors = [];
        if (this.username === "") {
          this.errors.push("The username is missing");
        }
        if (this.password1 === "") {
          this.errors.push("The password is too short");
        }
        if (this.password1 !== this.password2) {
          this.errors.push("The passwords do not match to each other");
        }

        let formData = {};
        if (!this.errors.length) {
          formData = {
            username: this.username,
            password: this.password1,
          };
        }

        await axios
          .post("/api/v1/users/", formData)
          .then((response) => {
            toast({
              message: "The user was created !",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });

            const emailData = { email: this.username };
            axios
              .post("/api/v1/teams/add_member/", emailData)
              .then((response) => {
                toast({
                  message: "The member was added !",
                  type: "is-success",
                  dismissible: true,
                  pauseOnHover: true,
                  duration: 2000,
                  position: "bottom-right",
                });
                this.$router.push({ name: "Team" });
              })
              .catch((error) => {
                if (error.response) {
                  if (this.$store.state.debugMode) {
                    console.log(error.response);
                  }
                  for (const property in error.response.data) {
                    this.errors.push(
                      `${property}: ${error.response.data[property]}`
                    );
                  }
                } else if (error.message) {
                  this.errors.push("Something went wrong, please try again");
                }
              });
          })
          .catch((error) => {
            if (error.response) {
              if (this.$store.state.debugMode) {
                console.log(error.response);
              }
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}: ${error.response.data[property]}`
                );
              }
            } else if (error.message) {
              this.errors.push("Something went wrong, please try again");
            }
          });

        this.$store.commit("setIsLoading", false);
      },
    },
  };
</script>
