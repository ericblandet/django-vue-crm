<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Leads</h1>
        <router-link
          class="button is-info"
          to="/dashboard/leads/add"
          v-if="num_leads < $store.state.team.max_clients"
        >
          Add lead
        </router-link>
        <div class="notification is-danger" v-else>
          <span
            >You have reached the top of your limitations. Please upgrade your
            plan!
          </span>
          <router-link :to="{ name: 'Plans' }"> See our plans</router-link>
        </div>

        <hr />
        <form>
          <div class="field has-addons">
            <div class="control">
              <input
                type="text"
                class="input"
                v-model="query"
                @keyup="submitForm()"
                placeholder="Search"
              />
            </div>
          </div>
        </form>
      </div>

      <div class="column is-12">
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th>Company</th>
              <th>Contact person</th>
              <th>Assigned to</th>
              <th>Status</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="lead in leads" v-bind:key="lead.id">
              <td>{{ lead.company }}</td>
              <td>{{ lead.contact_person }}</td>
              <td>
                <template v-if="lead.assigned_to">
                  {{ lead.assigned_to.first_name }}
                  {{ lead.assigned_to.last_name }}
                </template>
              </td>
              <td>{{ lead.status }}</td>
              <td>
                <router-link
                  :to="{
                    name: 'Lead',
                    params: { id: lead.id },
                  }"
                  >Details</router-link
                >
              </td>
            </tr>
          </tbody>
        </table>
        <div class="level">
          <div class="level-left">
            <div class="buttons">
              <button
                class="button is-light"
                v-if="showPreviousButton"
                @click="goToPreviousPage()"
              >
                Previous
              </button>
              <button
                class="button is-light"
                v-if="showNextButton"
                @click="goToNextPage()"
              >
                Next
              </button>
            </div>
          </div>
          <div class="level-right">
            <div class="page-count">
              <span v-if="numberOfRecords > 0">
                <strong>Number of records:</strong> {{ numberOfRecords }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { throwStatement } from "@babel/types";
  import axios from "axios";
  export default {
    name: "Leads",
    data() {
      return {
        leads: [],
        showNextButton: false,
        showPreviousButton: false,
        currentPage: 1,
        numberOfRecords: 0,
        num_leads: 0,
        query: "",
      };
    },
    mounted() {
      this.getLeads();
    },
    methods: {
      goToNextPage() {
        this.currentPage += 1;
        this.getLeads();
      },
      goToPreviousPage() {
        this.currentPage -= 1;
        this.getLeads();
      },
      async getLeads() {
        this.$store.commit("setIsLoading", true);

        this.showNextButton = false;
        this.showPreviousButton = false;

        await axios.get(`/api/v1/leads`).then((response) => {
          this.num_leads = response.data.count;
        });

        await axios
          .get(`/api/v1/leads/?page=${this.currentPage}&search=${this.query}`)
          .then((response) => {
            this.leads = response.data.results;
            if (response.data.next) {
              this.showNextButton = true;
            }
            if (response.data.previous) {
              this.showPreviousButton = true;
            }
            this.numberOfRecords = response?.data?.count;
          })
          .catch((error) => {
            console.log(error);
          });

        this.$store.commit("setIsLoading", false);
      },
      submitForm() {
        this.currentPage = 1;
        this.getLeads();
      },
    },
  };
</script>
