<template>
  <div class="login-wrapper">
    <div class="login-mask" id="mask"></div>
    <div class="ui-dialog" id="dialogMove">
      <div class="ui-dialog-title" id="dialogDrag">
        用户密码登录
        <a class="ui-dialog-closebutton" href="javascript：viod(0)">✖</a>
      </div>
      <div class="ui-dialog-content">
        <div class="uis uis-condition ui-dialog-username">
          <input type="text" name="username" placeholder="手机/邮箱/用户名" />
        </div>
        <div class="uis uis-condition ui-dialog-password">
          <input type="text" name="password" placeholder="密码" />
        </div>
        <div class="uis ui-dialog-login">
          <a href>登录</a>
        </div>
        <div class="uis ui-dialog-forget">
          <a href>忘记密码</a>
        </div>
        <div class="uis ui-dialog-register">
          <a href>立即注册</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    
}
</script>

<style>
.ui-dialog {
  width: 400px;
  height: auto;
  position: absolute;
  z-index: 1000;
  top: 0;
  left: 0;
  border: 1px solid black;
  background: white;
}
.ui-dialog a {
  text-decoration: none;
  color: black;
}
.ui-dialog-title {
  height: 48px;
  line-height: 48px;
  padding: 0 20px;
  color: #535353;
  font-size: 25px;
  border-bottom: 1px solid #efefef;
  background: #f5f5f5;
  cursor: move;
  user-select: none;
  text-align: center;
}
.ui-dialog-closebutton {
  width: 16px;
  height: 16px;
  display: block;
  position: absolute;
  top: -10px;
  right: 6px;
  cursor: pointer;
}
.ui-dialog-closebutton:hover {
  color: red;
}
.ui-dialog-content {
  padding: 15px 30px;
}
.uis {
  height: 40px;
  line-height: 40px;
  text-align: right;
  padding: 15px;
}
.uis-condition input {
  width: 100%;
  height: 40px;
  margin: 0;
  padding: 0;
  border: 1px solid #d5d5d5;
  font-size: 16px;
  text-indent: 25px;
  outline: none;
}
.ui-dialog-login a {
  width: 100%;
  height: 50px;
  background: rgba(74, 128, 189, 0.479);
  font-size: 20px;
  display: block;
  color: white;
  text-align: center;
  line-height: 50px;
}
.ui-dialog-login a:hover {
  background: #3f81b0;
}
.login-mask {
  width: 100%;
  height: 100%;
  background: burlywood;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 900;
  opacity: 0.4;
}
</style>