<template>
  <div class="home">
    <h1 class="title">DjangVue CRM !</h1>
    <img
      alt="Vue logo"
      src="https://rare-gallery.com/uploads/posts/989618-LEGO-Star-Wars-humor-toys-sand-depth-of-field.jpg"
    />
    <p><em>This picture has nothing to do with the app !</em></p>
    <hr />
    <p>
      DjangVue CRM is a simple webapp to track yourleads, manage your clients
      and organize your commercial team work !
    </p>
    <br />
    <p><strong>The app includes the following features:</strong></p>
    <ul>
      <li>Manage your sales team</li>
      <li>Create, Edit, Delete your leads</li>
      <li>Create, Edit, Delete your clients</li>
      <li>Add relevant notes on the clients' accounts</li>
      <li>Choose your plan today and pay by credit card !</li>
    </ul>
  </div>
</template>

<script>
  // @ is an alias to /src
  import HelloWorld from "@/components/HelloWorld.vue";

  export default {
    name: "HomeView",
    components: {
      HelloWorld,
    },
  };
</script>

<style scoped>
  .home {
    width: 1200px;
    margin: 0 auto;
    text-align: center;
  }

  .home img {
    width: 60%;
  }
</style>
