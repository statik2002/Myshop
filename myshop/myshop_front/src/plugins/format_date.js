export default {
    install: (app, options) => {
      app.config.globalProperties.$FormatDate = (date) => {
        date = new Date(date)
        let year = new Intl.DateTimeFormat('ru', { year: 'numeric' }).format(date);
        let month = new Intl.DateTimeFormat('ru', { month: 'short' }).format(date);
        let day = new Intl.DateTimeFormat('ru', { day: '2-digit' }).format(date);
        let hour = new Intl.DateTimeFormat('ru', { hour: '2-digit' }).format(date);
        let minute = new Intl.DateTimeFormat('ru', { minute: '2-digit' }).format(date);
        return `${day} ${month} ${year} ${hour}:${minute}`
      }
    }
  }