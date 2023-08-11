<template>
    <div>
      <welcome-message v-for="message in 5" :key="message.i"></welcome-message>
    </div>
</template>

<script>
import WelcomeMessage from './WelcomeMessage.vue';

export default {
    components :{
        'welcome-message': WelcomeMessage
    }
}
</script>