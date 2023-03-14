<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Plans</h1>
      </div>

      <div class="column is-4">
        <div class="box">
          <h2 class="subtitle">Free</h2>
          <h4 class="is-size-3">0 CHF</h4>
          <p>Max 5 leads</p>
          <p>Max 5 clients</p>
          <button class="button is-primary" @click="subscribe('free')">
            Subscribe
          </button>
        </div>
      </div>
      <div class="column is-4">
        <div class="box">
          <h2 class="subtitle">Small team</h2>
          <h4 class="is-size-3">10 CHF</h4>
          <p>Max 25 leads</p>
          <p>Max 25 clients</p>
          <button class="button is-primary" @click="subscribe('smallTeam')">
            Subscribe
          </button>
        </div>
      </div>
      <div class="column is-4">
        <div class="box">
          <h2 class="subtitle">Large team</h2>
          <h4 class="is-size-3">25 CHF</h4>
          <p>Max 50 leads</p>
          <p>Max 50 clients</p>
          <button class="button is-primary" @click="subscribe('largeTeam')">
            Subscribe
          </button>
        </div>
      </div>
    </div>
    <hr />
    <div class="column is-12">
      <button class="button is-danger" @click="cancelPlan()">
        Cancel plan
      </button>
    </div>
  </div>
</template>

<script>
  import axios from "axios";
  import { toast } from "bulma-toast";

  export default {
    name: "Plans",
    data() {
      return {
        pub_key: "",
        stripe: null,
      };
    },
    async mounted() {
      await this.getPubKey();
      this.stripe = Stripe(this.pub_key);
    },
    methods: {
      async getPubKey() {
        this.$store.commit("setIsLoading", true);
        await axios
          .get(`api/v1/stripe/get_stripe_pub_key/`)
          .then((response) => {
            this.pub_key = response.data.pub_key;
          })
          .catch((error) => {
            console.log(error);
          });
        this.$store.commit("setIsLoading", false);
      },
      async cancelPlan() {
        this.$store.commit("setIsLoading", true);
        axios
          .post(`/api/v1/teams/cancel_plan/`, {})
          .then((response) => {
            this.$store.commit("setTeam", {
              id: response.data.id,
              name: response.data.name,
              plan: response.data.plan.name,
              max_leads: response.data.plan.max_leads,
              max_clients: response.data.plan.max_clients,
              plan_end_date: response.data.plan_end_date,
            });

            toast({
              message: "The plan was cancelled",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });
          })
          .catch((error) => {
            console.log("Error:", error);
            toast({
              message: "Something went wrong",
              type: "is-danger",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });
          });

        this.$store.commit("setIsLoading", false);
      },
      async subscribe(plan) {
        this.$store.commit("setIsLoading", true);

        const data = {
          plan: plan,
        };

        axios
          .post(`/api/v1/stripe/create_checkout_session/`, data)
          .then((response) => {
            console.log(response);

            return this.stripe.redirectToCheckout({
              sessionId: response.data.sessionId,
            });
          })
          .catch((error) => {
            console.log("Error:", error);
          });

        this.$store.commit("setIsLoading", false);
      },
    },
  };
</script>
