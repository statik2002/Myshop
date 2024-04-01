<template>
    <div class="carousel">
        <div class="inner" ref="inner">
            <div class="card" v-for="card in cards" :key="card">
                {{ card }}
            </div>
        </div>
    </div>
    <button>prev</button>
    <button @click="next">next</button>
</template>

<script>
    export default {
        name: 'multiitem-carousel',
        data () {
            return {
                cards: [1, 2, 3, 4, 5, 6, 7, 8],
                innerStyles: {},
                step: ''
            }
        },
        methods: {
            next() {
                this.innerStyles = {
                    transform: `translateX(-${this.step})`
                }
                this.afterTransition(() => { // ❶
                    const card = this.cards.shift() // ❷
                    this.cards.push(card) // ❸
                    })
            },
            afterTransition (callback) {
                const listener = () => { // ❹
                    callback()
                    this.$refs.inner.removeEventListener('transitionend', listener)
                }
                this.$refs.inner.addEventListener('transitionend', listener) // ❺
            }
        },
        mounted() {
            const innerWidth = this.$refs.inner.scrollWidth
            const totalCards = this.cards.length
            this.step = `${innerWidth / totalCards}px`
            console.log(this.step)
        }
    }
</script>

<style scoped>
.carousel {
  width: 170px; /* ❶ */
  overflow: hidden; /* ❷ */
}

.inner {
    transition: transform 0.2s;
  white-space: nowrap; /* ❸ */
}

.card {
  width: 40px;
  margin-right: 10px;
  display: inline-flex;

  /* optional */
  height: 40px;
  background-color: #39b1bd;
  color: white;
  border-radius: 4px;
  align-items: center;
  justify-content: center;
}

/* optional */
button {
  margin-right: 5px;
  margin-top: 10px;
}
</style>