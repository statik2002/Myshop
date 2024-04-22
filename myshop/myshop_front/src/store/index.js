import axios from "axios";
import { createStore } from "vuex";

export default createStore({

    state() {
        return {
            user: {},
            userIsAuth: false,
            unregisteredUser: {
                cart: {
                    products: []
                },
                likes: []
            },
            catalogs: []
        }
    },

    getters: {
        getCart(state) {
            if (state.userIsAuth){
                return state.user.cart;
            } else {
                return state.unregisteredUser.cart
            }
        },

        productsInCart(state) {
            if (state.userIsAuth) {
                return state.user.cart.products;
            } else {
                return state.unregisteredUser.cart.products;
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
                if (state.unregisteredUser.cart.products.length > 0){
                    for(const product of state.unregisteredUser.cart.products){
                        total += product.quantity * product.fixed_price
                    }
                    return total
                } else {
                    return 0
                }
            }
        },

        getCartTotalWithoutDiscount(state) {
            let total = 0
            if (state.userIsAuth) {
                if (state.user.cart.products.length > 0){
                    for(const product of state.user.cart.products){
                        total += product.quantity * product.product.price
                    }
                    return total
                } else {
                    return 0
                }
            } else {
                if (state.unregisteredUser.cart.products.length > 0){
                    for(const product of state.unregisteredUser.cart.products){
                        total += product.quantity * product.product.price
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
                for (const product of state.unregisteredUser.cart.products){
                    total += product.quantity
                }
            }

            return total
        },

        getCartPositionCount(state) {
            if (state.userIsAuth) {
                return state.user.cart.products.length;
            } else {
                if (state.unregisteredUser.cart.products === undefined) {
                    return 0
                }
                return state.unregisteredUser.cart.products.length;
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

        getLikedProducts(state) {
            if(state.user.userIsAuth){
                if(state.user.likes === undefined) {
                    return []
                }
                return state.user.likes;
            } else {
                return state.unregisteredUser.likes;
            }
            
        },

        getLikedProductsCount(state) {
            if(state.user.userIsAuth){
                if(state.user.likes === undefined) {
                    return 0
                }
                return state.user.likes.length;
            } else {
                return state.unregisteredUser.likes.length;
            }
        },

        isUserLogin(state) {
            return state.userIsAuth
        },
        getCatalog(state) {
            return state.catalogs
        }
    },

    mutations: {
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
                const productIndex = state.user.cart.products.findIndex((index) => index.id === product.product.id);
                if (productIndex >= 0) {
                    state.user.cart.products[productIndex].quantity += product.quantity;
                    state.user.cart.cartProductsQuantity += product.quantity;
                    state.user.cart.cartProductsTotal += state.user.cart.products[productIndex].quantity * product.product.price;
                    localStorage.setItem('user', JSON.stringify(state.user))
                } else {
                    const newCartItem = {
                        id: product.product.id,
                        product: product.product,
                        quantity: product.quantity,
                        fixed_price: product.product.price - product.product.price * product.product.discount / 100,
                        cart: state.user.cart.id
                    };
                    state.user.cart.products.push(newCartItem);
                    localStorage.setItem('user', JSON.stringify(state.user))
                }
            } else {
                const productIndex = state.unregisteredUser.cart.products.findIndex((index) => index.id === product.product.id);
                if (productIndex >= 0) {
                    state.unregisteredUser.cart.products[productIndex].quantity += product.quantity;
                    state.unregisteredUser.cart.cartProductsQuantity += product.quantity;
                    state.unregisteredUser.cart.cartProductsTotal += state.unregisteredUser.cart.products[productIndex].quantity * product.product.price;
                    localStorage.setItem('unregisteredUser', JSON.stringify(state.unregisteredUser))
                } else {
                    const newCartItem = {
                        id: product.product.id,
                        product: product.product,
                        quantity: product.quantity,
                        fixed_price: product.product.price - product.product.price * product.product.discount / 100,
                        cart: 1
                    };
                    state.unregisteredUser.cart.products.push(newCartItem);
                    localStorage.setItem('unregisteredUser', JSON.stringify(state.unregisteredUser))
                }
            }
        },
        removeProductFromCart(state, product) {
            if (state.userIsAuth) {
                const productIndex = state.user.cart.products.findIndex((index) => index.id === product.id);
                state.user.cart.products.splice(productIndex, 1);
                localStorage.setItem('user', JSON.stringify(state.user))
            } else {
                const productIndex = state.unregisteredUser.cart.products.findIndex((index) => index.id === product.id);
                state.unregisteredUser.cart.products.splice(productIndex, 1);
                localStorage.setItem('unregisteredUser', JSON.stringify(state.unregisteredUser))
            }
            
        },

        addOne(state, id) {
            if (state.userIsAuth) {
                const productIndex = state.user.cart.products.findIndex((index) => index.id === id);
                state.user.cart.products[productIndex].quantity += 1;
                localStorage.setItem('user', JSON.stringify(state.user))
            } else {
                const productIndex = state.unregisteredUser.cart.products.findIndex((index) => index.id === id);
                state.unregisteredUser.cart.products[productIndex].quantity += 1;
                localStorage.setItem('unregisteredUser', JSON.stringify(state.unregisteredUser))
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
                const productIndex = state.unregisteredUser.cart.products.findIndex((index) => index.id === id);
                if (state.unregisteredUser.cart.products[productIndex].quantity > 1)
                {
                    state.unregisteredUser.cart.products[productIndex].quantity -= 1;
                    localStorage.setItem('unregisteredUser', JSON.stringify(state.unregisteredUser))
                }
            }
            
            
        },

        deleteProductFromCart(state, id) {
            if (state.userIsAuth) {
                const productIndex = state.user.cart.products.findIndex((index) => index.id === id);
                state.user.cart.products.splice(productIndex, 1)
                localStorage.setItem('user', JSON.stringify(state.user))
            } else {
                const productIndex = state.unregisteredUser.cart.products.findIndex((index) => index.id === id);
                state.unregisteredUser.cart.products.splice(productIndex, 1)
                localStorage.setItem('unregisteredUser', JSON.stringify(state.unregisteredUser))
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
            if(state.userIsAuth){
                state.user.cart.products = []
                state.user.cart.cartProductsQuantity = 0
                state.user.cart.cartProductsTotal = 0
                localStorage.setItem('user', JSON.stringify(state.user))
            } else {
                state.unregisteredUser.cart.products = []
                localStorage.setItem('unregisteredUser', JSON.stringify(state.unregisteredUser))
            }
            
        },
        like(state, product_id){
            if (state.userIsAuth) {
                state.user.likes.push(product_id)
                localStorage.setItem('user', JSON.stringify(state.user))
            } else {
                state.unregisteredUser.likes.push(product_id)
                localStorage.setItem('unregisteredUser', JSON.stringify(state.unregisteredUser))
            }
            
        },
        dislike(state, product_id){
            if (state.userIsAuth) {
                state.user.likes.pop(product_id)
                localStorage.setItem('user', JSON.stringify(state.user))
            } else {
                state.unregisteredUser.likes.pop(product_id)
                localStorage.setItem('unregisteredUser', JSON.stringify(state.unregisteredUser))
            }
            
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
        updateCatalog(state, catalog) {
            state.catalogs = catalog
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

        getCatalog({commit, state}) {
            try {
                axios(
                  {
                    url: `http://127.0.0.1:8000/api/v1/catalogs/`,
                    method: 'get'
                  }
                ).then((response) => {
                    commit('updateCatalog', response.data.results)
                })
          } catch(e) {
              console.log(`Connection error: ${e}`);
          }
          finally {
  
          }
        }
    },

    modules: {

    },
})