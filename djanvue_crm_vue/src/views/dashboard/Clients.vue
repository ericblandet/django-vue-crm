<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Clients</h1>
        <router-link
          v-if="num_clients < $store.state.team.max_clients"
          to="/dashboard/clients/add"
          class="button is-primary"
          >Add client</router-link
        >
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
                placeholder="Search"
                class="input"
                v-model="query"
                @keyup="submitForm()"
              />
            </div>
          </div>
        </form>
      </div>

      <div class="column is-12">
        <template v-if="clients.length">
          <table class="table is-fullwidth">
            <thead>
              <tr>
                <th>Name</th>
                <th>Contact person</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="client in clients" :key="client.id">
                <td>{{ client.name }}</td>
                <td>{{ client.contact_person }}</td>
                <td>
                  <router-link
                    :to="{
                      name: 'Client',
                      params: { id: client.id },
                    }"
                    >Details</router-link
                  >
                </td>
              </tr>
            </tbody>
          </table>
        </template>
        <template v-else>
          <p>You don't have any client yet ...</p>
        </template>

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
  import axios from "axios";

  export default {
    name: "Clients",
    data() {
      return {
        clients: [],
        showNextButton: false,
        showPreviousButton: false,
        currentPage: 1,
        numberOfRecords: 0,
        query: "",
        num_clients: 0,
      };
    },
    mounted() {
      this.getClients();
    },
    methods: {
      goToNextPage() {
        this.currentPage += 1;
        this.getClients();
      },
      goToPreviousPage() {
        this.currentPage -= 1;
        this.getClients();
      },
      async getClients() {
        this.$store.commit("setIsLoading", true);

        axios
          .get(`/api/v1/clients/`)
          .then((response) => (this.num_clients = response.data.count));

        await axios
          .get(`/api/v1/clients/?page=${this.currentPage}&search=${this.query}`)
          .then((response) => {
            this.clients = response.data.results;
            if (response.data.next) {
              this.showNextButton = true;
            }
            if (response.data.previous) {
              this.showPreviousButton = true;
            }
            this.numberOfRecords = response?.data?.count;
          })
          .catch((error) => {
            if (this.$store.state.debugMode) {
              console.log(error);
            }
          });

        this.$store.commit("setIsLoading", false);
      },
      submitForm() {
        this.currentPage = 1;
        this.getClients();
      },
    },
  };
</script>
