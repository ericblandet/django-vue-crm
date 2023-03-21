<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Add Team</h1>
      </div>
      <div class="column is-12">
        <form>
          <div class="field">
            <label for="teamName">Team name</label>
            <div class="control">
              <input type="text" name="teamName" class="input" v-model="name" />
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
    name: "AddTeam",
    data() {
      return {
        name: "",
      };
    },
    methods: {
      async submitForm() {
        this.$store.commit("setIsLoading", true);

        const team = {
          name: this.name,
        };

        await axios
          .post("/api/v1/teams/", team)
          .then((response) => {
            toast({
              message: "The team was added !",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });

            localStorage.removeItem("team_max_leads");
            localStorage.removeItem("team_max_clients");
            localStorage.removeItem("team_plan_end_date");
            localStorage.removeItem("team_plan");

            this.$store.commit("setTeam", {
              id: response.data.id,
              name: response.data.name,
              plan: response.data.plan.name,
              max_leads: response.data.plan.max_leads,
              max_clients: response.data.plan.max_clients,
              plan_end_date: response.data.plan_end_date,
              created_by_id: response.data.created_by.id,
            });

            if (!response.data.plan_end_date) {
              this.$router.push({ name: "Plans" });
            } else {
              this.$router.push("/dashboard/leads");
            }
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
