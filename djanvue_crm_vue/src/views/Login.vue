<template>
  <div class="container">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Login</h1>

        <form @submit.prevent="submitForm">
          <div class="field">
            <label for="email">Email</label>
            <div class="control">
              <input
                type="email"
                name="email"
                class="input"
                v-model="username"
              />
            </div>
          </div>

          <div class="field">
            <label for="password">Password</label>
            <div class="control">
              <input
                type="password"
                name="password1"
                class="input"
                v-model="password"
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
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    name: "Login",
    data() {
      return {
        username: "",
        password: "",
        errors: [],
      };
    },
    methods: {
      async submitForm() {
        this.$store.commit("setIsLoading", true);

        axios.defaults.headers.common["Authorization"] = "";
        localStorage.removeItem("token");
        this.errors = [];

        let formData = {};
        if (!this.errors.length) {
          formData = {
            username: this.username,
            password: this.password,
          };
        }

        await axios
          .post("/api/v1/token/login/", formData)
          .then((response) => {
            const token = response.data.auth_token;
            this.$store.commit("setToken", token);
            axios.defaults.headers.common["Authorization"] = "Token " + token;
            localStorage.setItem("token", token);
          })
          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}: ${error.response.data[property]}`
                );
              }
            } else if (error.message) {
              this.errors.push("Something went wrong, please try again");
            }
          });

        await axios
          .get("/api/v1/users/me/")
          .then((response) => {
            this.$store.commit("setUser", {
              id: response.data.id,
              username: response.data.username,
            });

            localStorage.setItem("username", response.data.username);
            localStorage.setItem("user_id", response.data.id);
          })
          .catch((error) => {
            if (this.$store.state.debugMode) {
              console.log(error);
            }
          });

        await axios
          .get("/api/v1/teams/get_my_team/")
          .then((response) => {
            this.$store.commit("setTeam", {
              id: response.data.id,
              name: response.data.name,
              plan: response.data?.plan?.name ?? "Free Plan",
              max_leads: response.data?.plan?.max_leads ?? 5,
              max_clients: response.data?.plan?.max_clients ?? 5,
              plan_end_date: response.data?.plan_end_date ?? "",
              created_by_id: response.data?.created_by?.id ?? "",
            });

            if (response.data.name == "") {
              this.$router.push({ name: "AddTeam" });
            } else {
              this.$router.push("/dashboard/my-account");
            }
          })

          .catch((error) => console.log(error));

        this.$store.commit("setIsLoading", false);
      },
    },
  };
</script>
