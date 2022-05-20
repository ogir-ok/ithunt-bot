<template>

  <form @submit="performLogin" v-if="user">
    login: <input name="email"/>
    password: <input type="password" name="password"/>
    <input type="submit"/>
  </form>

    <h2> {{ user }}</h2>

</template>

<script>
export default {
  name: "LoginForm",
  async mounted() {
    const response = await fetch('/api/user/', {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('accessToken')}`
        },
        method: "get",
      })
    if (response.status === 200) {
      this.user = await response.json();
    }
  },
  data() {
    return {user: null}
  },
  methods: {
    async performLogin(e) {
      e.stopPropagation();
      e.preventDefault();

      const email = 'admin@admin.com'
      const password = 'admin123'
      const response = await fetch('/api/token/', {
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
        },
        method: "post",
        body: JSON.stringify({email, password})
      })

      const tokens = await response.json()
      console.log('tokens:', tokens)

      localStorage.setItem('accessToken', tokens.access)

    }
  }
}
</script>

<style scoped>

</style>