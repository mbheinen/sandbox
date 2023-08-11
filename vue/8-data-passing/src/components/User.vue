<template>
    <div class="component">
        <h1>The User Component</h1>
        <p>I'm an awesome User!</p>
        <button @click="changeName">Change my Name</button>
        <p>Name is {{name}}</p>
        <hr>
        <div class="row">
            <div class="col-xs-12 col-sm-6">
                <!-- Passes name data property to UserDetail component using binding to myName
                Also, catches event emitted from UserDetail component if that component resets the name -->
                <app-user-detail 
                     :myName="name" 
                     @nameWasReset="name=$event"
                     :resetFn="resetName"
                     :userAge="age"></app-user-detail>
            </div>
            <div class="col-xs-12 col-sm-6">
                <app-user-edit :userAge="age"></app-user-edit>
            </div>
        </div>
    </div>
</template>

<script>
    import UserDetail from './UserDetail.vue';
    import UserEdit from './UserEdit.vue';

    export default {
        data: function() {
            return {
                name: 'Mike',
                age: 21
            };
        },
        methods: {
            changeName() {
                this.name = 'Michael'
            },
            resetName() {
                this.name = 'Bobby'
            }
        },
        components: {
            appUserDetail: UserDetail,
            appUserEdit: UserEdit
        }

    }
</script>

<style scoped>
    div {
        background-color: lightblue;
    }
</style>
