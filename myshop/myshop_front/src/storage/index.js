import { useStorage } from '@vueuse/core'

export default useStorage(
    'my-store',
    {'someValue': 'value'}
)