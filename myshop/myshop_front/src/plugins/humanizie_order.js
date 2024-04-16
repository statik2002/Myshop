export default {
    install: (app, options) => {
      app.config.globalProperties.$HumanizieOrders = (numOrders) => {
        if (numOrders < 10)
        {
            if ([0, 5, 6, 7, 8, 9].includes(numOrders)) {
                return `${numOrders} заказов`
            } else if ([2, 3, 4].includes(numOrders)) {
                return `${numOrders} заказа`
            } else {
                return `${numOrders} заказ`
            }
        } else {
            const astNumOrders = numOrders % 10
            if ([0, 5, 6, 7, 8, 9].includes(lastNumOrders)) {
                return `${numOrders} заказов`
            } else if ([2, 3, 4].includes(lastNumOrders)) {
                return `${numOrders} заказа`
            } else {
                return `${numOrders} заказ`
            }
        }
        }
    }
  }