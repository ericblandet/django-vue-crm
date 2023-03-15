<template>
  <div class="container">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Edit note</h1>
      </div>
      <div class="column is-12">
        <form>
          <div class="field">
            <label for="name">Name</label>
            <div class="control">
              <input
                type="text"
                name="name"
                class="input"
                v-model="note.name"
              />
            </div>
          </div>
          <div class="field">
            <label for="body">Body</label>
            <div class="control">
              <textarea class="textarea" v-model="note.body"></textarea>
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
    name: "EditMember",
    data() {
      return {
        note: {
          name: "",
          body: "",
        },
      };
    },
    mounted() {
      this.getNote();
    },
    methods: {
      async submitForm() {
        this.$store.commit("setIsLoading", true);

        await axios
          .patch(
            `/api/v1/notes/${this.note.id}/?client_id=${this.$route.params.id}`,
            this.note
          )
          .then((response) => {
            toast({
              message: "The note was updated !",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });

            this.$router.push({
              name: "Client",
              params: { id: this.$route.params.id },
            });
          })
          .catch((error) => {
            if (this.$store.state.debugMode) {
              console.log(error);
            }
          });

        this.$store.commit("setIsLoading", false);
      },
      async getNote() {
        this.$store.commit("setIsLoading", true);

        await axios
          .get(
            `/api/v1/notes/${this.$route.params.note_id}/?client_id=${this.$route.params.id}`
          )
          .then((response) => {
            this.note = response.data;
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
