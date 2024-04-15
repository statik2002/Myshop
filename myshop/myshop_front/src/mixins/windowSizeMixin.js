import { ref, onMounted, onUnmounted } from 'vue'

export function useWindowWidth() {

    const windowSize = ref('xl')

    function update(event) {
        const clientWidth = document.documentElement.clientWidth

        if (clientWidth < 576) {
            windowSize.value = 'esm'
        } else if (clientWidth >= 576 && clientWidth < 768) {
            windowSize.value = 'sm'
        } else if (clientWidth >= 768 && clientWidth < 992) {
            windowSize.value = 'md'
        } else if (clientWidth >= 992 && clientWidth < 1200) {
            windowSize.value = 'lg'
        } else if (clientWidth >= 1200 && clientWidth < 1400) {
            windowSize.value = 'xl'
        } else if (clientWidth >= 1400) {
            windowSize.value = 'xxl'
        }
    }
    

    onMounted(() => window.addEventListener('resize', update))
    onUnmounted(() => window.removeEventListener('resize', update))

    return windowSize
}