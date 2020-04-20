<template>
    <div class="login">
        <div class="login-triangle"></div>
        <h2 class="login-header">Регистрация</h2>
        <form class="login-container" @submit="onSubmit">
            <p><input v-model="loginForm.login" type="textarea" placeholder="Введите ваш логин"></p>
            <p><input v-model="loginForm.pwd" type="password" placeholder="Введите ваш пароль"></p>
            <p><input v-model="loginForm.email" type="email" placeholder="Введите вашу эл. почту"></p>
            <input type="submit" value="Зарегистрироваться">
        </form>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: "RegisterPage",
        data() {
            return {
                loginForm: {
                    login: '',
                    pwd: '',
                    email: ''
                },
            }
        },
        methods: {
            initForm() {
                this.loginForm.login = '';
                this.loginForm.pwd = '';
                this.loginForm.email = '';
            },
            async loginToCloud(login, password, email) {
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
                let login = this.loginForm.login;
                let pwd = this.loginForm.pwd;
                let email = this.loginForm.email;
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