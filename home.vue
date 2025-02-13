<template>
    <div class="home">
        <h1>Welcome to the Home Page</h1>
        <p>This is a simple Vue.js home page.</p>
    </div>
</template>

<script>
export default {
    name: 'Home',
    data() {
        return {
            message: 'Hello, Vue!'
        };
    }
};
</script>

<style scoped>
.home {
    text-align: center;
    margin-top: 50px;
}

h1 {
    color: #42b983;
}

p {
    font-size: 18px;
}
</style></div></template>