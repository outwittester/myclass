<!DOCTYPE html>
<html lange="en" xmlns:v-bind="http://www.w3.org/1999/xhtml" xmlns:v-on="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="UTF-8"/>
    <title>Vue my title</title>

</head>
<body>
<div id="app">
    {{message2}}
    <h1 v-bind:title="message"></h1>
    <!-- v-bind:value只能进行单向的数据渲染 -->
    <input type="text" v-bind:value="searchMap.keyWord">
    <!-- v-model 可以进行双向的数据绑定  -->
    <input type="text" v-model="searchMap.keyword">
    <p>您要查询的是：{{searchMap.keyword}}</p>
    <!--        <button v-on:click="search()">click to search</button>-->
    <button @click="search()">click to search</button>
    <p><a v-bind:href="result.site" target="_blank">{{result.title}}</a></p>
    <h1>Hello Routers!</h1>
    <p>
        <!-- <router-link> 默认会被渲染成一个 `<a>` 标签 -->
        <!-- 通过传入 `to` 属性指定链接. -->
        <router-link to="/">首页</router-link>
        <router-link to="/student">会员管理</router-link>
        <router-link to="/teacher">讲师管理</router-link>
    </p>
    <router-view></router-view>
</div>
<script src="vue.js"></script>
<script src="vue-router.js"></script>
<script>
    const Welcome = {template: '<div>欢迎</div>'}
    const Student = {template: '<div>student list</div>'}
    const Teacher = {template: '<div>teacher list</div>'}
    const routes =[
        {path:'/',redirect:'/welcome'},
        {path:'/welcome',comment: Welcome},
        {path:'/student',comment: Student},
        {path:'/teacher',comment: Teacher},
    ]
    const router = new VueRouter({
        routes
    })
    new Vue({
        el: '#app',
        data: {
            message: 'Hello xikai is coming',
            message2: 'loading data ' + new Date().toLocaleDateString(),
            searchMap: {
                keyword: '7-yr-developer'
            },
            result: {
                'title': 'google',
                // 'site':'https://www.google.com'
                'site': 'www.google.com' // this is relative
            }
        },
        methods: {
            search() {
                console.log('search method called');
                //todo
            }
        },
        router
    })
</script>
</body>
</html>
