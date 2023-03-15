<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">{{ lead.company }}</h1>
      </div>

      <div class="column is-12">
        <form>
          <div class="field">
            <label for="company">Company</label>
            <div class="control">
              <input
                type="text"
                name="company"
                class="input"
                v-model="lead.company"
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
                v-model="lead.contact_person"
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
                v-model="lead.email"
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
                v-model="lead.phone"
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
                v-model="lead.website"
              />
            </div>
          </div>
          <div class="field">
            <label for="confidence">Confidence</label>
            <div class="control">
              <input
                type="number"
                name="confidence"
                class="input"
                v-model="lead.confidence"
              />
            </div>
          </div>
          <div class="field">
            <label for="estimated_value">Estimated Value</label>
            <div class="control">
              <input
                type="number"
                name="estimated_value"
                class="input"
                v-model="lead.estimated_value"
              />
            </div>
          </div>
          <div class="field">
            <label for="status">Status</label>
            <div class="control">
              <div class="select">
                <select name="status" v-model="lead.status">
                  <option value="new">New</option>
                  <option value="contacted">Contacted</option>
                  <option value="inprogress">In Progress</option>
                  <option value="lost">Lost</option>
                  <option value="won">Won</option>
                </select>
              </div>
            </div>
          </div>
          <div class="field">
            <label for="priority">Priority</label>
            <div class="control">
              <div class="select">
                <select name="priority" v-model="lead.priority">
                  <option value="low">Low</option>
                  <option value="medium">Medium</option>
                  <option value="high">High</option>
                </select>
              </div>
            </div>
          </div>
          <div class="field">
            <label for="assigned_to">Assigned to</label>
            <div class="control">
              <div class="select">
                <select name="assigned_to" v-model="lead.assigned_to">
                  <option value="" selected>Select member</option>
                  <option
                    v-for="member in team.members"
                    :key="member.id"
                    :value="member.id"
                  >
                    {{ member.username }}
                  </option>
                </select>
              </div>
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
    name: "EditLead",
    data() {
      return {
        lead: {},
        team: {
          members: {},
        },
      };
    },
    mounted() {
      this.getLead();
      this.getTeam();
    },
    methods: {
      async getLead() {
        this.$store.commit("setIsLoading", true);
        const leadId = this.$route.params.id;

        axios
          .get(`/api/v1/leads/${leadId}`)
          .then((response) => {
            this.lead = response.data;
          })
          .catch((error) => {
            if (this.$store.state.debugMode) {
              {
                if (this.$store.state.debugMode) {
                  console.log(error);
                }
              }
            }
          });

        this.$store.commit("setIsLoading", false);
      },
      async submitForm() {
        this.$store.commit("setIsLoading", true);
        const leadId = this.$route.params.id;

        axios
          .patch(`/api/v1/leads/${leadId}/`, this.lead)
          .then((response) => {
            toast({
              message: "The lead was updated !",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });

            this.$router.push(`/dashboard/leads/${leadId}`);
          })
          .catch((error) => {
            if (this.$store.state.debugMode) {
              console.log(error);
            }
          });

        this.$store.commit("setIsLoading", false);
      },
      async getTeam() {
        this.$store.commit("setIsLoading", true);
        await axios
          .get("/api/v1/teams/get_my_team/")
          .then((response) => {
            this.team = response.data;
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
