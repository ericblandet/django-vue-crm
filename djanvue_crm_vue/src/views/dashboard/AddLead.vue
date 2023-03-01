
<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add Lead</h1>
            </div>
            <div class="column is-12">
                <form>
                    <div class="field">
                        <label for="company">Company</label>
                        <div class="control">
                            <input type="text" name="company" class="input" v-model="company">
                        </div>
                    </div>
                    <div class="field">
                        <label for="contact_person">Contact Person</label>
                        <div class="control">
                            <input type="text" name="contact_person" class="input" v-model="contact_person">
                        </div>
                    </div>
                    <div class="field">
                        <label for="email">Email</label>
                        <div class="control">
                            <input type="email" name="email" class="input" v-model="email">
                        </div>
                    </div>
                    <div class="field">
                        <label for="phone">Phone</label>
                        <div class="control">
                            <input type="text" name="phone" class="input" v-model="phone">
                        </div>
                    </div>
                    <div class="field">
                        <label for="website">Website</label>
                        <div class="control">
                            <input type="text" name="website" class="input" v-model="website">
                        </div>
                    </div>
                    <div class="field">
                        <label for="confidence">confidence</label>
                        <div class="control">
                            <input type="number" name="confidence" class="input" v-model="confidence">
                        </div>
                    </div>
                    <div class="field">
                        <label for="estimated_value">Estimated Value</label>
                        <div class="control">
                            <input type="number" name="estimated_value" class="input" v-model="estimated_value">
                        </div>
                    </div>
                    <div class="field">
                        <label for="status">status</label>
                        <div class="control">
                            <div class="select">

                                <select name="status" v-model="status">
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
                        <label for="priority">priority</label>
                        <div class="control">
                            <div class="select">
                                <select name="priority" v-model="priority">
                                    <option value="low">Low</option>
                                    <option value="medium">Medium</option>
                                    <option value="high">High</option>
                                </select>
                            </div>
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
export default {
    name: 'AddLead',
    data() {
        return {
            company: '',
            contact_person: '',
            email: '',
            phone: '',
            website: '',
            confidence: 0,
            estimated_value: 0,
            status: 'new',
            priority: 'medium',
        }
    },
    methods: {
        async submitForm() {

            this.$store.commit('setIsLoading', true)
            const lead = {
                company: this.company,
                contact_person: this.contact_person,
                email: this.email,
                phone: this.phone,
                website: this.website,
                confidence: this.confidence,
                estimated_value: this.estimated_value,
                status: this.status,
                priority: this.priority,
            }

            await axios
                .post('/api/v1/leads/', lead)
                .then(response => {
                    console.log(response)

                    this.$router.push('/dashboard/leads')
                })
                .catch(error => console.log(error))


            this.$store.commit('setIsLoading', false)
        }
    }

}
</script>
  