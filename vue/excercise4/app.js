new Vue({
  el: '#exercise',
  data: {
    highlightActive: true,
    enteredClass: 'green',
    enteredSecondClass: 'blue',
    showAnother: false,
    enteredStyle: 'yellow',
    progressSize: 0
  },
  computed: {
    coupleOfClasses: function() {
      return {green: true, big: true};
    },
    progressStyle: function() {
      return {width: this.progressSize + 'px', backgroundColor: 'purple'}
    }
  },
  methods: {
    startEffect: function() {
      var vm = this;
      setInterval(function() {
          vm.highlightActive = !vm.highlightActive;
        },
        1000);
    
    },
    startProgress: function() {
      var vm = this;
      setInterval(function() {
        vm.progressSize += 2;
      }, 1000)
    }
  }
});
