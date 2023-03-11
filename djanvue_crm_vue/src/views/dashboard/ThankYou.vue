<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Thank you</h1>
            </div>
            <div class="column is-4">
                <p>Thank you for your subscription !</p>
                <br>
                <button class="button is-light" @click="$router.push({ name: 'Team' })">
                    🙂
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
export default {
    name: "ThankYou",
    data() {
        return {

        };
    },
};
</script>
