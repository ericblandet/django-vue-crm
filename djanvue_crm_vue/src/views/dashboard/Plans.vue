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
                    <button class="button is-primary" @click="subscribe('free')">Subscribe</button>
                </div>

            </div>
            <div class="column is-4">
                <div class="box">
                    <h2 class="subtitle">Small team</h2>
                    <h4 class="is-size-3">10 CHF</h4>
                    <p>Max 10 leads</p>
                    <p>Max 10 clients</p>
                    <button class="button is-primary" @click="subscribe('smallTeam')">Subscribe</button>
                </div>
            </div>
            <div class="column is-4">
                <div class="box">
                    <h2 class="subtitle">Large team</h2>
                    <h4 class="is-size-3">25 CHF</h4>
                    <p>Max 25 leads</p>
                    <p>Max 25 clients</p>
                    <button class="button is-primary" @click="subscribe('largeTeam')">Subscribe</button>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
import axios from "axios";
import { toast } from 'bulma-toast'


export default {
    name: "Plans",
    data() {
        return {

        };
    },
    mounted() {
    },
    methods: {
        async subscribe(plan) {
            this.$store.commit('setIsLoading', true)

            const data = {
                plan: plan
            }

            await axios
                .post(`/api/v1/teams/upgrade_plan/`, data)
                .then(response => {
                    console.log(response)
                    this.$store.commit('setTeam', {
                        id: response.data.id,
                        name: response.data.name,
                        plan: response.data.plan.name,
                        max_leads: response.data.plan.max_leads,
                        max_clients: response.data.plan.max_clients,
                    })
                    this.$router.push('/dashboard/team/plans/thankyou')

                    toast({
                        message: 'The plan has changed',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
};
</script>
