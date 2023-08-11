new Vue({
        el: '#exercise2',
        data: {
            value1: '',
            value2: ''
        },
        methods: {
          showAlert: function() {
            alert("What up?")
          },
          storeValue: function() {
            this.value1 = event.target.value;
          },
          storeEnteredValue: function() {
            this.value2 = event.target.value;
          }
        }
    });
