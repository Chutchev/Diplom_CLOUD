import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/main',
            component: () => import("@/components/MainPage")
        },
        {
            path: '/home',
            component: () => import("@/components/Home")
        },
        {
            path: '/login',
            component: () => import("@/components/LoginPage")
        },
    ]
})