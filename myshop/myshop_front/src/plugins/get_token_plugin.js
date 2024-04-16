import axios from 'axios';

export default {
    install: (app, options) => {
        app.config.globalProperties.$getToken = (login, password) => {
            axios(
                {
                    method: 'post',
                    url: 'http://127.0.0.1:8000/api/v1/token/login/',
                    headers: {'Content-Type': 'application/json;charset=utf-8'},
                    data: JSON.stringify({'phone_number': login, 'password': password})
                }
            )
            .then((response) => {
                const token = response.data.access
                console.log(response.data)
                return {'access': response.data.access, 'refresh': response.data.refresh}
            })
            .catch((error) => {
                if (error.response.data.error) {
                    return {}
                }
            })
        }
    }
  }