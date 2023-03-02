
<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Edit member</h1>
            </div>
            <div class="column is-12">
                <form>
                    <div class="field">
                        <label for="first_name">First Name</label>
                        <div class="control">
                            <input type="text" name="first_name" class="input" v-model="user.first_name">
                        </div>
                    </div>
                    <div class="field">
                        <label for="last_name">Last Name</label>
                        <div class="control">
                            <input type="text" name="last_name" class="input" v-model="user.last_name">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control"><button class="button is-success" @click.prevent="submitForm()">
                                Submit
                            </button></div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'EditMember',
    data() {
        return {
            user: {},
        }
    },
    mounted() {
        this.getUser()
    },
    methods: {
        async submitForm() {
            this.$store.commit('setIsLoading', true)

            await axios
                .put(`/api/v1/teams/member/${this.$route.params.id}/`, this.user)
                .then(response => {
                    toast({
                        message: 'The user was updated !',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })

                    this.$router.push({ name: 'MyAccount' })
                })
                .catch(error => console.log(error))


            this.$store.commit('setIsLoading', false)
        },
        async getUser() {
            this.$store.commit('setIsLoading', true)

            await axios.
                get(`/api/v1/teams/member/${this.$route.params.id}/`)
                .then(response => {
                    this.user = response.data
                })
                .catch(error => console.log(error))

            this.$store.commit('setIsLoading', false)
        },
    }

}
</script>
