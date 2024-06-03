<template>
    <header-component></header-component>
    <div class="wrapper">
        <main class="p-5">
            <div class="error-container">
                <h1>404</h1>
                <p>Ой. Такой страницы нет!</p>
                <router-link to="/">Вернуться на главную</router-link>
            </div>
        </main>
    </div>
    <footer-component></footer-component>
</template>

<script>
    export default {
        
    }
</script>

<style scoped>
.error-container { 
    text-align: center; 
    background-color: #fff; 
    padding: 20px; 
    border-radius: 5px; 
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); 
}
h1 { 
    font-size: 5rem; 
    color: #ff5733; 
} 
  
p { 
    font-size: 1.5rem; 
    color: #333; 
    margin-bottom: 20px; 
} 
  
a { 
    text-decoration: none; 
    background-color: #ff5733; 
    color: #fff; 
    padding: 10px 20px; 
    border-radius: 3px; 
    font-weight: bold; 
    transition: background-color 0.3s ease; 
} 
  
a:hover { 
    background-color: #e6482e; 
}
</style>