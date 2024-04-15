import axios from "axios";
import { createStore } from "vuex";

export default createStore({

    state() {
        return {
            user: {},
            userIsAuth: false,
            windowWidth: '',
            cart: {
                products: [],
            }
        }
    },

    getters: {
        getCart(state) {
            return state.user.cart;
        },

        productsInCart(state) {
            if (state.userIsAuth) {
                return state.user.cart.products;
            } else {
                return state.cart.products
            }
            
        },

        getCartTotal(state) {
            let total = 0
            if (state.userIsAuth) {
                if (state.user.cart.products.length > 0){
                    for(const product of state.user.cart.products){
                        total += product.quantity * product.fixed_price
                    }
                    return total
                } else {
                    return 0
                }
            } else {
                if (state.cart.products.length > 0){
                    for(const product of state.cart.products){
                        total += product.quantity * product.fixed_price
                    }
                    return total
                } else {
                    return 0
                }
            }
            
            
        },

        getCartProductsCount(state) {
            let total = 0
            if(state.userIsAuth) {
                for (const product of state.user.cart.products){
                    total += product.quantity
                }
            } else {
                for (const product of state.cart.products){
                    total += product.quantity
                }
            }

            return total
        },

        getCartPositionCount(state) {
            if (state.userIsAuth) {
                return state.user.cart.products.length;
            } else {
                return state.cart.products.length;
            }

            
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
            if (state.userIsAuth) {
                const productIndex = state.user.cart.products.findIndex((index) => index.id === product.id);
                if (productIndex >= 0) {
                    state.user.cart.products[productIndex].quantity += 1;
                    state.user.cart.cartProductsQuantity += 1;
                    state.user.cart.cartProductsTotal += state.user.cart.products[productIndex].quantity * product.price;
                    localStorage.setItem('user', JSON.stringify(state.user))
                } else {
                    const newCartItem = {
                        id: product.id,
                        product: product,
                        quantity: 1,
                        fixed_price: product.price,
                        cart: state.user.cart.id
                    };
                    state.user.cart.products.push(newCartItem);
                    localStorage.setItem('user', JSON.stringify(state.user))
                }
            } else {
                const productIndex = state.cart.products.findIndex((index) => index.id === product.id);
                if (productIndex >= 0) {
                    state.cart.products[productIndex].quantity += 1;
                    state.cart.cartProductsQuantity += 1;
                    state.cart.cartProductsTotal += state.cart.products[productIndex].quantity * product.price;
                    localStorage.setItem('cart', JSON.stringify(state.cart))
                } else {
                    const newCartItem = {
                        id: product.id,
                        product: product,
                        quantity: 1,
                        fixed_price: product.price,
                        cart: state.cart.id
                    };
                    state.cart.products.push(newCartItem);
                    localStorage.setItem('cart', JSON.stringify(state.cart))
                }
            }
        },
        removeProductFromCart(state, product) {
            const productIndex = state.user.cart.products.findIndex((index) => index.id === product.id);
            state.user.cart.products.splice(productIndex, 1);
            localStorage.setItem('user', JSON.stringify(state.user))
        },

        addOne(state, id) {
            if (state.userIsAuth) {
                const productIndex = state.user.cart.products.findIndex((index) => index.id === id);
                state.user.cart.products[productIndex].quantity += 1;
                localStorage.setItem('user', JSON.stringify(state.user))
            } else {
                const productIndex = state.cart.products.findIndex((index) => index.id === id);
                state.cart.products[productIndex].quantity += 1;
                localStorage.setItem('cart', JSON.stringify(state.cart))
            }
        },

        subOne(state, id) {
            if (state.userIsAuth) {
                const productIndex = state.user.cart.products.findIndex((index) => index.id === id);
                if (state.user.cart.products[productIndex].quantity > 1)
                {
                    state.user.cart.products[productIndex].quantity -= 1;
                    localStorage.setItem('user', JSON.stringify(state.user))
                }
            } else {
                const productIndex = state.cart.products.findIndex((index) => index.id === id);
                if (state.cart.products[productIndex].quantity > 1)
                {
                    state.cart.products[productIndex].quantity -= 1;
                    localStorage.setItem('cart', JSON.stringify(state.cart))
                }
            }
            
            
        },

        deleteProductFromCart(state, id) {
            if (state.userIsAuth) {
                const productIndex = state.user.cart.products.findIndex((index) => index.id === id);
                state.user.cart.products.splice(productIndex, 1)
                localStorage.setItem('user', JSON.stringify(state.user))
            } else {
                const productIndex = state.cart.products.findIndex((index) => index.id === id);
                state.cart.products.splice(productIndex, 1)
                localStorage.setItem('cart', JSON.stringify(state.cart))
            }
            
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

        logoutUser(state,actions) {
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
            commit('setUserPhone', tel)
        },

        saveUserCartToServer({state}) {
            const cart = state.user.cart
            let cart_products = []
            for (const key in state.user.cart.products){
                cart_products.push({
                    'product': state.user.cart.products[key],
                    'quantity': state.user.cart.products[key].quantity,
                    'fixed_price': state.user.cart.products[key].fixed_price,
                    'cart': cart.id,
                })
            }
            try {
                axios(
                  {
                    url: `http://127.0.0.1:8000/api/v1/carts/${cart.id}/`,
                    method: 'put',
                    headers: {'Authorization': `Bearer ${state.user.access}`},
                    data: cart
                  }
                ).then((response) => {
                  //console.log(response.data)
                  return
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