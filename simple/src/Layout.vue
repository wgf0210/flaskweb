<template>
  <div>
    <div class="app-head">
      <div class="app-head-inner">
        <img src="./assets/logo.png" alt="">
        <div class="head-nav">
          <ul class="nav-list">
            <li>登录</li>
            <li class="nav-pile">|</li>
            <li>注册</li>
            <li class="nav-pile">|</li>
            <li>关于</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="app-content">
      <router-view></router-view>
    </div>
    <div class="app-footer">
      <p>&copy;1903C-2020</p>
    </div>
  </div>
</template>

<script>
export default {
}
</script>

<style scoped>
/* layout样式 */
.app-head{
  background: #363636;
  color:#b2b2b2;
  height: 90px;
  line-height: 90px;
  width: 100%;
}
.app-head-inner{
  width: 1200px;
  margin: 0 auto;
}
.app-head-inner img{
  float: left;
  width: 50px;
  margin-top: 20px;
}
.head-nav{
  float: right;
}
.head-nav li{
  float: left;
  cursor: pointer;
}
.nav-pile{
  padding: 0 10px;
}
.app-footer{
  text-align: center;
  height: 80px;
  line-height: 80px;
  width: 100%;
  background: #e3e4e8;
  margin-top: 30px;
}
.app-content{
  width: 1200px;
  margin: 0 auto;
}
/* reset重置样式 */
html {
overflow-x:auto;
overflow-y:scroll;
}
body, dl, dt, dd, ul, ol, li, pre, form, fieldset, input, p, blockquote, th, td {
font-weight:400;
margin:0;
padding:0;
}
h1, h2, h3, h4, h4, h5 {
margin:0;
padding:0;
}
body {
background-color:#FFFFFF;
color:#666666;
font-family:Helvetica,Arial,sans-serif;
font-size:12px;
padding:0 10px;
text-align:left;
}
select {
font-size:12px;
}
table {
border-collapse:collapse;
}
fieldset, img {
border:0 none;
}
fieldset {
margin:0;
padding:0;
}
fieldset p {
margin:0;
padding:0 0 0 8px;
}
legend {
display:none;
}
address, caption, em, strong, th, i {
font-style:normal;
font-weight:400;
}
table caption {
margin-left:-1px;
}
hr {
border-bottom:1px solid #FFFFFF;
border-top:1px solid #E4E4E4;
border-width:1px 0;
clear:both;
height:2px;
margin:5px 0;
overflow:hidden;
}
ol, ul {
list-style-image:none;
list-style-position:outside;
list-style-type:none;
}
caption, th {
text-align:left;
}
q:before, q:after, blockquote:before, blockquote:after {
content:””;
}
</style>