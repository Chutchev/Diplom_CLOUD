<template>
    <div class="row_pop-up">
        <div class="box small-6 large-centered">
            <a href="#" class="close-button" @click="this.closePopUp">&#10006;</a>
            <h3>Ссылка на файл</h3>
            <input type="text" :value="this.url"/>
        </div>
    </div>
</template>

<script>
    export default {
        name: "CopyUrlHTML",
        props:{
            url: null
        },
        methods: {
            closePopUp(){
                let popup = document.getElementsByClassName('row_pop-up')[0];
                popup.style.display = 'none';
            }
        }
    }
</script>

<style scoped>
    .row_pop-up {
        position: absolute;
        margin: auto;
        display: none;
        left: 0;
        right: 0;
        z-index: 2;
        width: 400px;
    }
    .row_pop-up input {
        width: 350px;
        text-align: center;
        margin-bottom: 5%;
    }

    .box {
        background-color: whitesmoke;
        text-align: center;
        margin-left: auto;
        margin-right: auto;
        margin-top: 10%;
        position: relative;
        -webkit-box-shadow: 0px 4px 6px 0px rgba(0,0,0,0.1);
        -moz-box-shadow: 0px 4px 6px 0px rgba(0,0,0,0.1);
        box-shadow: 0px 4px 6px 0px rgba(0,0,0,0.1);
    }

    .button {
        margin: 0 auto;
        background-color: #FF8566;
        margin-bottom: 33px;
    }

    .button:hover {
        background-color: #7CCF29;
        -webkit-box-shadow: 0px 4px 6px 0px rgba(0,0,0,0.1);
        -moz-box-shadow: 0px 4px 6px 0px rgba(0,0,0,0.1);
        box-shadow: 0px 4px 6px 0px rgba(0,0,0,0.1);
    }

    .close-button {
        transition: all 0.5s ease;
        position: absolute;
        background-color: #FF9980;
        padding: 1.5px 7px;
        left: 0;
        margin-left: -10px;
        margin-top: -9px;
        border-radius: 50%;
        border: 2px solid #fff;
        color: white;
        -webkit-box-shadow: -4px -2px 6px 0px rgba(0,0,0,0.1);
        -moz-box-shadow: -4px -2px 6px 0px rgba(0,0,0,0.1);
        box-shadow: -3px 1px 6px 0px rgba(0,0,0,0.1);
    }

    .close-button:hover {
        background-color: tomato;
        color: #fff;
    }

    h3 {
        text-align: center;
        padding-top: 15px;
        padding-bottom: 15px;
        color: #fff;
        background-color: #FF704D;
    }

    p {
        padding: 20px 65px 10px 65px;
        color: dimgray;
    }

    h1 {
        color: dimgray;
        font-family: Garamond, Baskerville, "Baskerville Old Face", "Hoefler Text", "Times New Roman", serif;
    }
</style>