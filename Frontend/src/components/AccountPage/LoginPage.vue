<template>
    <v-card
            class="mx-auto"
            width="35%"
            elevation="6"
            style="margin: auto">
        <v-card-title class="d-inline-block text-truncate text-uppercase"
                      style="width: 100%; background: #1E1E1E; color: white; margin-bottom: 10px">
            Войти
        </v-card-title>
        <v-form
                ref="form"
                v-model="valid"
                :lazy-validation="lazy"
        >
            <v-text-field
                    v-model="form.name"
                    :rules="nameRules"
                    label="Логин"
                    required
                    style="width: 90%; margin: auto;"
            ></v-text-field>
            <v-text-field
                    v-model="form.pwd"
                    :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                    :rules="passwordRules"
                    :type="show1 ? 'text' : 'password'"
                    name="input-10-1"
                    label="Пароль"
                    hint="Минимум 8 символов"
                    counter
                    @click:append="show1 = !show1"
                    style="width: 90%; margin: auto;"
            ></v-text-field>
            <v-card-text>Не зарегистрированы?
                <v-btn text color="primary" @click="this.rebaseToRegister">Зарегистрируйтесь!</v-btn>
            </v-card-text>
            <v-checkbox
                    v-model="form.remember"
                    label="Запомнить меня?"
                    style="margin-left: 25px;"
            ></v-checkbox>
            <v-btn
                    :disabled="!valid"
                    class="mr-4"
                    @click="this.onSubmit"
                    style="margin-bottom: 10px"
            >
                Войти
            </v-btn>
        </v-form>
    </v-card>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "LoginPage",
        data() {
            return {
                form: {
                    name: '',
                    pwd: '',
                    remember: false
                },
                valid: true,
                nameRules: [
                    v => !!v || 'Name is required',
                    v => (v && v.length > 2) || 'Имя должно быть длиннее 2-х символов',
                ],
                passwordRules: [
                    v => !!v || 'Password is required',
                    v => (v && v.length >= 8) || 'Длина пароля должна быть больше 8 символов',
                ],
                select: null,
                checkbox: false,
                lazy: false,
                show1: false
            }
        },
        methods: {
            validate() {
                this.$refs.form.validate()
            },
            rebaseToRegister(){
              location.href='/register'
            },
            async loginToCloud(login, password) {
                const url = 'http://127.0.0.1:8000/api/authtoken/';
                let credentials = {
                    username: login,
                    password: password
                };
                await axios.post(url, credentials)
                    .then((response) => {
                        console.log(response.data);
                        if (this.form.remember){
                            localStorage.setItem('TOKEN', response.data['token']);
                            sessionStorage.setItem('TOKEN', response.data['token']);
                        }
                        else {
                            sessionStorage.setItem('TOKEN', response.data['token'])
                        }
                        if (response.data['token']) {
                            document.location.href = 'http://localhost:8080/files'
                        }
                        else {
                            alert('Вы ввели что то неверно!')
                        }
                    })
                    .catch(error => console.log('ОШИБКА!!!!: ' + error));
            },
            async onSubmit() {
                let login = this.form.name;
                let pwd = this.form.pwd;
                await this.loginToCloud(login, pwd);
            }
        },
        mounted() {
        }
    }
</script>

<style scoped>
</style>