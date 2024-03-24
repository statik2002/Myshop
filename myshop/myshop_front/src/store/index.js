import axios from "axios";
import { createStore } from "vuex";

export default createStore({

    state() {
        return {
            user: {},
            userIsAuth: false,
        }
    },

    getters: {
        getCart(state) {
            return state.user.cart;
        },

        getCartTotal(state) {
            let total = 0
            if (state.user.cart.products.length > 0){
                for(const product of state.user.cart.products){
                    total += product.quantity * product.price
                }
                return total
            } else {
                return 0
            }
        },

        getCartProductsCount(state) {
            if(!state.userIsAuth) return 0
            
            let total = 0
            for (const product of state.user.cart.products){
                total += product.quantity
            }

            return total
        },

        getCartPositionCount(state) {
            if (!state.userIsAuth) return 0

            return state.user.cart.products.length;
        },
        getProductQuantity(state, id) {
            if (state.user.cart.products > 0) {
                const productIndex = state.user.cart.products.findIndex((index) => index.id === id);
                return state.user.cart.products[productIndex].quantity;
            } else {
                return 0
            }
            
        },
        getProductInCart(state, id) {
            const productIndex = state.user.cart.products.findIndex((index) => index.id === id);
            return state.user.cart.products[productIndex];
        },

        isUserLogin(state) {
            return state.userIsAuth
        }
    },

    mutations: {
        incrementLikes(state) {
            state.likes += 1
        },

        decrementLikes(state) {
            (state.likes > 1) ? state.likes -= 1 : 1;
        },

        setUserPhone(state, phone) {
            state.userPhone = phone
        },

        setUserPassword(state, password) {
            state.userPassword = password
        },

        setAccessToken(state, token) {
            state.accessToken = token
        },

        updateUser(state, user) {
            state.user.first_name = user.first_name
            state.user.last_name = user.last_name
            state.user.address = user.address
            localStorage.setItem('user', JSON.stringify(state.user))
        },

        addProductToCart(state, product) {
            const productIndex = state.user.cart.products.findIndex((index) => index.id === product.id);
            if (productIndex >= 0) {
                state.user.cart.products[productIndex].quantity += 1;
                state.user.cart.cartProductsQuantity += 1;
                state.user.cart.cartProductsTotal += state.user.cart.products[productIndex].quantity * product.price;
                localStorage.setItem('user', JSON.stringify(state.user))
            } else {
                const newCartItem = {
                    id: product.id,
                    name: product.name,
                    product_images: product.product_images,
                    description: product.description,
                    available: product.available,
                    slug: product.slug,
                    rating: product.rating,
                    show_count: product.show_count,
                    create_date: product.create_date,
                    price: product.price,
                    discount: product.discount,
                    code_1c: product.code_1c,
                    quantity: 1,
                    catalog: product.catalog,
                    tags: product.tags
                };
                state.user.cart.products.push(newCartItem);
                localStorage.setItem('user', JSON.stringify(state.user))
            }
        },
        removeProductFromCart(state, product) {
            const productIndex = state.user.cart.products.findIndex((index) => index.id === product.id);
            state.user.cart.products.splice(productIndex, 1);
            localStorage.setItem('user', JSON.stringify(state.user))
        },

        addOne(state, id) {
            const productIndex = state.user.cart.products.findIndex((index) => index.id === id);
            state.user.cart.products[productIndex].quantity += 1;
            localStorage.setItem('user', JSON.stringify(state.user))
        },

        subOne(state, id) {
            const productIndex = state.user.cart.products.findIndex((index) => index.id === id);
            if (state.user.cart.products[productIndex].quantity > 1)
            {
                state.user.cart.products[productIndex].quantity -= 1;
                localStorage.setItem('user', JSON.stringify(state.user))
            }
            
        },

        deleteProductFromCart(state, id) {
            const productIndex = state.user.cart.products.findIndex((index) => index.id === id);
            state.user.cart.products.splice(productIndex, 1)
            localStorage.setItem('user', JSON.stringify(state.user))
        },

        deleteProductsFromCart(state, products){

            for (const product in products) {
                const productIndex = state.user.cart.products.findIndex((index) => index.id === product.id);
                state.user.cart.products.splice(productIndex, 1)
            }
            localStorage.setItem('user', JSON.stringify(state.user))


        },

        setUser(state, user) {
            state.user = user
            localStorage.setItem('user', JSON.stringify(user))
            state.userIsAuth = true
        },

        logoutUser(state) {
            state.user = {}
            state.userIsAuth = false
            localStorage.removeItem('user')
        },
        setUserState(state, flag){
            state.userIsAuth = flag
        },
        clearCart(state) {
            state.user.cart.products = []
            state.user.cart.cartProductsQuantity = 0
            state.user.cart.cartProductsTotal = 0
            localStorage.setItem('user', state.user)
        },
        like(state, product_id){
            state.user.likes.push(product_id)
            localStorage.setItem('user', JSON.stringify(state.user))
        },
        dislike(state, product_id){
            state.user.likes.pop(product_id)
            localStorage.setItem('user', JSON.stringify(state.user))
        },
        reloadUser(state) {
            if (state.userIsAuth)
            {
                try {
                    axios(
                        {
                        url: `http://127.0.0.1:8000/api/v1/customers/${state.user.id}/`,
                        method: 'get',
                        headers: {'Authorization': `Bearer ${state.user.access}`},
                        }
                    ).then((response) => {
                            //console.log(response.status)
                            if (response.status == 200){
                                state.user = response.data
                                localStorage.setItem('user', JSON.stringify(state.user))
                            }
                            else {
                                console.log('Error')
                            }
                        })
                } catch (e) {
                        console.log(`Connection error: ${e}`);
                } finally {

                }
            }
        },
        
    },

    actions: {
        updatePhone({commit, state}, tel) {
            console.log(tel)
            commit('setUserPhone', tel)
        },

        saveUserCartToServer({state}) {
            let cart = JSON.parse(localStorage.getItem('cart'))
            console.log({'customer': state.user.id,  'cart': cart})
            try {
                axios(
                  {
                    url: `http://127.0.0.1:8000/api/v1/carts/`,
                    method: 'post',
                    headers: {'Authorization': `Bearer ${state.user.access}`},
                    data: JSON.stringify({'customer': state.user.id,  'cart': cart})
                  }
                ).then((response) => {
                  console.log(response.data)
                  })
            } catch(e) {
                console.log(`Connection error: ${e}`);
            }
            finally {
    
            }
        },
    },

    modules: {

    },
})