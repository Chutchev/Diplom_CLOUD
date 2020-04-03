import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router);

const ifAuthenticated = (to, from, next) => {
    let is_autorised = localStorage.getItem('TOKEN');
    if (is_autorised) {
        next();
        return
    }
    next('/login')
};

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/files',
            beforeEnter: ifAuthenticated,
            component: () => import("@/components/FilesMenu/MainPage")
        },
        {
            path: '/home',
            beforeEnter: ifAuthenticated,
            component: () => import("@/components/Home")
        },
        {
            path: '/login',
            component: () => import("@/components/LoginPage")
        },
    ]
})