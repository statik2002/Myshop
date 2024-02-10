import { createStore } from "vuex";

export default createStore({
    state: () => ({
        likes: 1,
        isAuth: false,
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
            return state.cartProductsTotal;
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
                state.cartProductsQuantity += product.quantity;
                state.cartProductsTotal += product.quantity * product.price;
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
                    quantity: product.quantity,
                    catalog: product.catalog,
                    tags: product.tags
                };
                state.cart.push(newCartItem);
                state.cartProductsQuantity += product.quantity;
                state.cartProductsTotal += product.quantity * product.price;
            }
        },
        removeProductFromCart(state, product) {
            const productIndex = state.cart.findIndex((index) => index.id === product.id);
            state.cart.splice(productIndex, 1);
            state.cartProductsQuantity -= product.quantity;
            state.cartProductsTotal -= product.quantity - product.price;
        },

        addOne(state, id) {
            const productIndex = state.cart.findIndex((index) => index.id === id);
            state.cart[productIndex].quantity += 1;
        },

        subOne(state,product) {
            const productIndex = state.cart.findIndex((index) => index.id === id);
            state.cart[productIndex].quantity -= 1;
        }
    },

    actions: {
        updatePhone({commit, state}, tel) {
            console.log(tel)
            commit('setUserPhone', tel)
        },
    },

    modules: {

    }
})