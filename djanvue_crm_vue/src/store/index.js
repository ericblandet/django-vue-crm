import { createStore } from "vuex";

export default createStore({
  state: {
    isLoading: false,
    isAuthenticated: false,
    token: "",
    user: {
      id: 0,
      username: "",
    },
    team: {
      id: 0,
      name: "",
      plan: "",
      max_leads: 0,
      max_clients: 0,
    },
  },
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("token")) {
        state.token = localStorage.getItem("token");
        state.isAuthenticated = true;
        state.user.username = localStorage.getItem("username");
        state.user.id = localStorage.getItem("user_id");
        state.team.name = localStorage.getItem("team_name");
        state.team.plan = localStorage.getItem("team_plan");
        state.team.max_leads = localStorage.getItem("team_max_leads");
        state.team.max_clients = localStorage.getItem("team_max_clients");
        state.team.id = localStorage.getItem("team_id");
        state.team.created_by_id = localStorage.getItem("team_created_by_id");
      } else {
        state.token = "";
        state.isAuthenticated = false;
        state.user.id = 0;
        state.user.username = "";
        state.team.id = "";
        state.team.name = "";
        state.team.plan = "";
        state.team.max_leads = 0;
        state.team.max_clients = 0;
        state.team.created_by_id = "";
      }
      state.debugMode = process?.env?.VUE_APP_DEBUG == "true";
      state.apiUrl = process.env.VUE_APP_BASE_SERVER_URL;
    },
    setIsLoading(state, status) {
      state.isLoading = status;
    },
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = "";
      state.isAuthenticated = false;
    },
    setUser(state, user) {
      state.user = user;
    },
    setTeam(state, team) {
      state.team = team;

      localStorage.setItem("team_id", team.id);
      localStorage.setItem("team_name", team.name);
      localStorage.setItem("team_plan", team.plan);
      localStorage.setItem("team_max_leads", team.max_leads);
      localStorage.setItem("team_max_clients", team.max_clients);
      localStorage.setItem("team_plan_end_date", team.plan_end_date);
      localStorage.setItem("team_created_by_id", team.created_by_id);
    },
  },
  getters: {},
  actions: {},
  modules: {},
});
