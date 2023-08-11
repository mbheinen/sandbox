<template>
    <div class="component">
        <h3>You may edit the User here</h3>
        <p>Edit me!</p>
        <button @click="editAdge">Edit Age</button>
    </div>
</template>

<script>
// Import named export to import the event bus
import { eventBus } from '../main';
export default {
    props: ['userAge'],
    methods: {
        editAge () {
            this.userAge = 33;
            // emits event on the event bus we created to pass data directly to component (not through child)
            eventBus.$emit()
        }
    }
}
</script>

<style scoped>
    div {
        background-color: lightgreen;
    }
</style>
