<template>
<div>
<span>历史资料</span>
<span>文学创作</span>
<button @click= 'anniu1'>Test Post</button>
<p> {{message}} </p>
</div>
</template>
<script>
export default{
  data () {
    return {
      message: 'message'
    }
  },
  methods: {
    async anniu1 () {
      const result = await this.$http.post('api', '1')
      console.log(result)
      this.message = result.data
    }
  }
}
</script>
<style>
</style>
