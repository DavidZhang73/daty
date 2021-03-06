import Vue from 'vue'
import VueClipboard from 'vue-clipboard2'
import App from './App.vue'
import router from './router'
import store from './store'

import VueLS from 'vue-ls'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

let options = {
    namespace: 'vuejs__',
    name: 'ls',
    storage: 'local',
};

Vue.config.productionTip = false;

Vue.use(ElementUI);
Vue.use(VueLS, options);
Vue.use(VueClipboard);

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');
