<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">My Account</h1>
      </div>
      <div class="column is-12">
        <div class="buttons">
          <router-link
            :to="{ name: 'EditMember', params: { id: $store.state.user.id } }"
            class="button is-light"
            >Edit</router-link
          >
          <button @click="logout()" class="button is-danger">Logout</button>
        </div>
        <div class="">
          <span>Application administrator ?</span>
          <a :href="`${$store.state.apiUrl}admin`" target="_blank" no>
            Go to Admin dashboard</a
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    name: "MyAccount",
    methods: {
      async logout() {
        await axios
          .post("/api/v1/token/logout/")
          .then((response) => {
            if (this.$store.state.debugMode) {
              console.log("logged out");
            }
          })
          .catch((error) => {
            if (this.$store.state.debugMode) {
              console.log(JSON.stringify(error));
            }
          });

        axios.defaults.headers.common["Authorization"] = "";
        localStorage.removeItem("token");
        localStorage.removeItem("username");
        localStorage.removeItem("user_id");
        localStorage.removeItem("team_name");
        localStorage.removeItem("team_id");
        localStorage.removeItem("team_max_leads");
        localStorage.removeItem("team_max_clients");
        localStorage.removeItem("team_plan_end_date");
        localStorage.removeItem("team_plan");
        this.$store.commit("removeToken");

        this.$router.push("/");
      },
    },
  };
</script>
