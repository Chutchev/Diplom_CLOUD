import Vue from 'vue'
import Router from 'vue-router'
import MainPage from "@/components/FilesMenu/MainPage";

Vue.use(Router);

const ifAuthenticated = (to, from, next) => {
    let ls_is_autorised = localStorage.getItem('TOKEN');
    let ss_is_autorised = sessionStorage.getItem('TOKEN');
    if (ls_is_autorised || ss_is_autorised) {
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
            component: MainPage
        },
        {
            path: '/home',
            beforeEnter: ifAuthenticated,
            component: () => import("@/components/Home")
        },
        {
            path: '/login',
            component: () => import("@/components/RegisterPage/LoginPage")
        },
        {
            path: '/me',
            beforeEnter: ifAuthenticated,
            component: () => import("@/components/AccountPage/MePage")
        },
        {
            path: '/upload',
            beforeEnter: ifAuthenticated,
            component: () => import("@/components/UploadPage/UploadPage")
        },
        {
            path: '/register',
            component: () => import("@/components/RegisterPage/RegisterPage")
        }
    ]
})