<template>
    <v-card
            class="mx-auto overflow-hidden"
    >
        <v-app-bar
                color="deep-purple"
                dark
        >
            <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

            <v-toolbar-title>CerBeR Cloud
                <v-icon>mdi-cloud</v-icon>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <v-spacer></v-spacer>
            <v-toolbar-title>{{login}}
            </v-toolbar-title>
            <v-btn icon @click="this.LogOut">
                <v-icon large>mdi-exit-to-app</v-icon>
            </v-btn>
        </v-app-bar>

        <v-navigation-drawer
                v-model="drawer"
                absolute
                temporary
                height="100vh"
        >
            <v-list
                    nav
                    dense
            >
                <v-list-item-group
                        active-class="deep-purple--text text--accent-4"
                >
                    <v-list-item onclick="location.href='/files'">
                        <v-list-item-icon>
                            <v-icon>mdi-file-multiple</v-icon>
                        </v-list-item-icon>
                        <v-list-item-title>Мои файлы</v-list-item-title>
                    </v-list-item>

                    <v-list-item onclick="location.href='/upload'">
                        <v-list-item-icon>
                            <v-icon>mdi-cloud-upload</v-icon>
                        </v-list-item-icon>
                        <v-list-item-title>Загрузить файл</v-list-item-title>
                    </v-list-item>

                </v-list-item-group>
            </v-list>
        </v-navigation-drawer>
    </v-card>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "MainInfoBar",
        data: () => ({
            drawer: false,
            login: 'Your Nickname',
        }),
        methods: {
            LogOut() {
                window.location.href = '/login';
                localStorage.removeItem('TOKEN');
                sessionStorage.removeItem('TOKEN');
            }
        },
        async mounted() {
            let self = this;
            const url = 'http://127.0.0.1:8000/api/user/';
            let token = sessionStorage.getItem('TOKEN');
            await axios.get(url, {
                headers: {
                    'authorization': `Token ${token}`
                }
            }).then(response => {
                self.login = response.data[0].user.username
            }).catch(()=>{
                window.location.href='/login'
            })
        }
    }

</script>

<style scoped>
</style>