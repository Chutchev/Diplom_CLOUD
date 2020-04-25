<template>
    <v-card
            class="mx-auto"
            width="35%"
            elevation="6"
            style="margin: auto">
        <v-card-title class="d-inline-block text-truncate text-uppercase"
                      style="width: 100%; background: #1E1E1E; color: white">
            Войти
        </v-card-title>
        <v-form
                ref="form"
                v-model="valid"
        >
            <v-text-field
                    v-model="form.name"
                    :rules="nameRules"
                    label="Логин"
                    required
                    style="width: 90%; margin: auto;"
            ></v-text-field>

            <v-text-field
                    v-model="form.email"
                    :rules="emailRules"
                    label="E-mail"
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
            <v-btn
                    class="mr-4"
                    @click="this.onSubmit"
                    style="margin-bottom: 10px"
            >
                Зарегистрироваться!
            </v-btn>
        </v-form>
    </v-card>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "RegisterPage",
        data() {
            return {
                form: {
                    name: '',
                    pwd: '',
                    email: ''
                },
                valid: true,
                nameRules: [
                    v => !!v || 'Name is required',
                    v => (v && v.length > 2) || 'Имя должно быть длиннее 2-х символов',
                ],
                emailRules: [
                    v => !!v || 'E-mail is required',
                    v => /.+@.+\..+/.test(v) || 'Введите верный email',
                ],
                passwordRules: [
                    v => !!v || 'Password is required',
                    v => (v && v.length >= 8) || 'Длина пароля должна быть больше 8 символов',
                ],
                select: null,
                checkbox: false,
                show1: false
            }
        },
        methods: {
            async loginToCloud(login, password, email) {
                console.log(password);
                const url = 'http://127.0.0.1:8000/api/user/';
                let credentials = {
                    'user': {
                        username: login,
                        password: password,
                        email: email
                    }
                };
                await axios.post(url, credentials)
                    .then((response) => {
                        if (response.data['success']) {
                            document.location.href = 'http://localhost:8080/login'
                        } else {
                            alert('Вы ввели что то неверно!')
                        }
                    })
                    .catch(error => console.log('ОШИБКА!!!!: ' + error));
            },
            async onSubmit(evt) {
                evt.preventDefault();
                let login = this.form.name;
                let pwd = this.form.pwd;
                let email = this.form.email;
                await this.loginToCloud(login, pwd, email);
            }
        },
    }
</script>

<style scoped>
    @import url(https://fonts.googleapis.com/css?family=Open+Sans:400,700);

    body {
        background: #456;
        font-family: 'Open Sans', sans-serif;
    }

    .login {
        width: 400px;
        margin: 16px auto;
        font-size: 16px;
    }

    /* Reset top and bottom margins from certain elements */
    .login-header,
    .login p {
        margin-top: 0;
        margin-bottom: 0;
    }

    /* The triangle form is achieved by a CSS hack */
    .login-triangle {
        width: 0;
        margin-right: auto;
        margin-left: auto;
        border: 12px solid transparent;
        border-bottom-color: #e67e22;
    }

    .login-header {
        background: #e67e22;
        padding: 20px;
        font-size: 1.4em;
        font-weight: normal;
        text-align: center;
        text-transform: uppercase;
        color: #fff;
    }

    .login-container {
        background: #ebebeb;
        padding: 12px;
    }

    /* Every row inside .login-container is defined with p tags */
    .login p {
        padding: 12px;
    }

    .login input {
        box-sizing: border-box;
        display: block;
        width: 100%;
        border-width: 1px;
        border-style: solid;
        padding: 16px;
        outline: 0;
        font-family: inherit;
        font-size: 0.95em;
    }

    .login input[type="login"],
    .login input[type="password"] {
        background: #fff;
        border-color: #bbb;
        color: #555;
    }

    /* Text fields' focus effect */
    .login input[type="email"]:focus,
    .login input[type="password"]:focus {
        border-color: #888;
    }

    .login input[type="submit"] {
        background: #e67e22;
        border-color: transparent;
        color: #fff;
        cursor: pointer;
    }

    .login input[type="submit"]:hover {
        background: #ff7700;
    }

    /* Buttons' focus effect */
    .login input[type="submit"]:focus {
        border-color: #f09a4f;
    }

    #remember {
        display: inline-block;
        width: auto;
    }
</style>