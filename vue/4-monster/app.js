new Vue({
  el: '#app',
  data: {
    gameLog: [],
    playerHealth: 100,
    monsterHealth: 100,
    gameInProgress: false
  },
  methods: {
    startGame: function() {
        this.gameInProgress = true;
        this.playerHealth = 100;
        this.monsterHealth = 100;
        this.gameLog = [];
    },
    attack: function() {
        var monsterHit = this.getRandomInt(3, 10);
        this.monsterHealth -= monsterHit;
        this.gameLog.unshift({player: true, text: "PLAYER HITS MONSTER FOR " + monsterHit});
        if (this.checkWinLose()) {
            return;
        }

        var playerHit = this.getRandomInt(5, 10);
        this.playerHealth -= playerHit;
        this.gameLog.unshift({player: false, text: "MONSTER HITS PLAYER FOR " + playerHit});
        this.checkWinLose();
    },
    specialAttack: function() {
        var monsterHit = this.getRandomInt(10, 20);
        this.monsterHealth -= monsterHit;
        this.gameLog.unshift({player: true, text: "PLAYER CHOPS MONSTER FOR " + monsterHit});
        this.checkWinLose();
    },
    heal: function() {
        if(this.playerHealth < 90) {
          var playerHeal = this.getRandomInt(8, 12);
          this.playerHealth += playerHeal;
          this.gameLog.unshift({player: true, text: "PLAYER HEALS FOR" + playerHeal});
        }

        var playerHit = this.getRandomInt(1, 5);
        this.playerHealth -= playerHit;
        this.gameLog.unshift({player: false, text: "MONSTER HITS PLAYER FOR " + playerHit});
        this.checkWinLose();
    },
    giveUp: function() {
        this.gameInProgress = false;
    },
    getRandomInt: function(min, max) {
        return Math.max(Math.floor(Math.random() * max) + 1, min);
    },
    checkWinLose: function() {
        if (this.monsterHealth <= 0) {
            if(confirm("Great work, you won! New game?")) {
                this.startGame();
            }
            else {
                this.gameInProgress = false;
            }
            return true;
        }
        else if (this.playerHealth <= 0) {
            if(confirm("Oh no, you lost! New game?")) {
                this.startGame();
            }
            else {
                this.gameInProgress = false;
            }
            return false;
        }
    }
  }
});