<template>
    <div class="component">
        <h3>You may view the User Details here</h3>
        <p>Many Details</p>
        <p>Reversed User Name: {{ switchName() }}</p>
        <button @click="resetName">Reset Name</button>
        <button @click="resetFn()">Reset Name</button>
    </div>
</template>

<script>
import { eventBus } from '../main'
export default {
    // props defines allowed parameters that can be passed to this component
    props: {
        myName: {
            type: String,
            required: true,
        },
        resetFn: Function
    },
    methods: {
        switchName() {
            return this.myName.split("").reverse().join("");
        },
        resetName() {
            this.myName = 'Arlo';
            this.$emit('nameWasReset', this.myName);
        }
    },
    // Using ES6 instead of ES5 syntax
    created() {
        eventBus.$on('ageWasEdited',  (age) => {
            this.userAge = age;
        })
    }
}
</script>

<style scoped>
    div {
        background-color: lightcoral;
    }
</style>
