import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SignUp from "../views/SignUp.vue";
import Login from "../views/Login.vue";
import Dashboard from "../views/dashboard/Dashboard.vue";
import MyAccount from "../views/dashboard/MyAccount.vue";
import Leads from "../views/dashboard/Leads.vue";
import AddLead from "../views/dashboard/AddLead.vue";
import store from "../store";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/signup",
    name: "SignUp",
    component: SignUp,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
    meta: {
      requireLogin: true,
    },
  },
  {
    path: "/dashboard/my-account",
    name: "MyAccount",
    component: MyAccount,
    meta: {
      requireLogin: true,
    },
  },
  {
    path: "/dashboard/leads",
    name: "Leads",
    component: Leads,
    meta: {
      requireLogin: true,
    },
  },
  {
    path: "/dashboard/leads/add",
    name: "AddLead",
    component: AddLead,
    meta: {
      requireLogin: true,
    },
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if (
    to.matched.some((record) => record.meta.requireLogin) &&
    !store.state.isAuthenticated
  ) {
    next("/login");
  } else {
    next();
  }
});

export default router;
