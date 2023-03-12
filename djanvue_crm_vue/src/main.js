import axios from "axios";
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

axios.defaults.baseURL = process.env.VUE_APP_BASE_SERVER_URL;

createApp(App).use(store).use(router, axios).mount("#app");
