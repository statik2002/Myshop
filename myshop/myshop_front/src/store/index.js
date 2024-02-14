import axios from "axios";
import { createStore } from "vuex";

export default createStore({
    state: () => ({
        likes: 1,
        isAuth: false,
        user: {},
        userPhone: '+79149569967',
        userPassword: 'obninsk1978#',
        accessToken: '',
        refreshToken: '',
        cart: [],
        cartProductsQuantity: 0,
        cartProductsTotal: 0,
    }),

    getters: {
        doubleLikes(state) {
            return state.likes * 2;
        },
        checkUserLogin(state) {

        },
        getPhoneNumber(state) {
            return state.userPhone;
        },

        getCart(state) {
            return state.cart;
        },

        getCartTotal(state) {
            return state.cartProductsTotal;
        },

        getCartProductsCount(state) {
            return state.cartProductsQuantity;
        },

        getCartPositionCount(state) {
            return state.cart.length;
        },
        getProductQuantity(state, id) {
            const productIndex = state.cart.findIndex((index) => index.id === id);
            return state.cart[productIndex].quantity;
        },
        getProductInCart(state, id) {
            const productIndex = state.cart.findIndex((index) => index.id === id);
            return state.cart[productIndex];
        },
        getTotalProductQuantity(state) {
            let total = 0
            for (let product of state.cart) {
                total += product.quantity
            }
            return total
        },
        getTotalProductsAmount(state) {
            let total = 0
            for (let product of state.cart) {
                total += product.quantity * product.price
            }
            return total
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

        addProductToCart(state, product) {
            const productIndex = state.cart.findIndex((index) => index.id === product.id);
            if (productIndex >= 0) {
                state.cart[productIndex].quantity += 1;
                state.cartProductsQuantity += 1;
                state.cartProductsTotal += state.cart[productIndex].quantity * product.price;
                localStorage.setItem('cart', JSON.stringify(state.cart))
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
                state.cart.push(newCartItem);
                state.cartProductsQuantity += 1;
                state.cartProductsTotal += 1 * product.price;
                localStorage.setItem('cart', JSON.stringify(state.cart))
            }
        },
        removeProductFromCart(state, product) {
            const productIndex = state.cart.findIndex((index) => index.id === product.id);
            state.cart.splice(productIndex, 1);
            state.cartProductsQuantity -= 1;
            state.cartProductsTotal -= Number(state.cartProductsTotal - product.price)
        },

        addOne(state, id) {
            const productIndex = state.cart.findIndex((index) => index.id === id);
            state.cart[productIndex].quantity += 1;
            state.cartProductsQuantity += 1;
            state.cartProductsTotal += Number(state.cart[productIndex].price)
            localStorage.setItem('cart', JSON.stringify(state.cart))
        },

        subOne(state, id) {
            const productIndex = state.cart.findIndex((index) => index.id === id);
            if (state.cart[productIndex].quantity > 1)
            {
                state.cart[productIndex].quantity -= 1;
                state.cartProductsQuantity -= 1;
                state.cartProductsTotal -= state.cart[productIndex].price
                localStorage.setItem('cart', JSON.stringify(state.cart))
            }
            
        },

        deleteProductFromCart(state, id) {
            const productIndex = state.cart.findIndex((index) => index.id === id);
            state.cart.splice(productIndex, 1)
            localStorage.setItem('cart', JSON.stringify(state.cart))
        },

        setUser(state, user) {
            state.user = user
        }
    },

    actions: {
        updatePhone({commit, state}, tel) {
            console.log(tel)
            commit('setUserPhone', tel)
        },

        registerUser({commit, state}, user) {
            return new Promise((resolve, reject) => {
                axios(
                    {
                        method: 'post',
                        url: 'http://127.0.0.1:8000/api/v1/customers/',
                        headers: {'Content-Type': 'application/json;charset=utf-8'},
                        data: JSON.stringify(user)
                    }
                )
                .then((response) => {
                    console.log(response)
                    commit('setUser', {'phone': user.phone_number, 'password': user.password, 'isAuth': true})
                })
                .catch((error) => {
                    console.log(error)
                })
            })
        },

        loginUser({commit, state}, user) {
            return new Promise((resolve, reject) => {
                axios(
                    {
                        method: 'post',
                        url: 'http://127.0.0.1:8000/api/token/',
                        headers: {'Content-Type': 'application/json;charset=utf-8'},
                        data: JSON.stringify({'phone_number': user.phone, 'password': user.password})
                    }
                )
                .then((response) => {
                    //console.log(response)
                    commit('setUser', {'phone': user.phone, 'password': user.password, 'isAuth': true, 'access': response.data.access})
                })
                .catch((error) => {
                    console.log(error)
                })
            })
        }
    },

    modules: {

    }
})