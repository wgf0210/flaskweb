<template>
  <div class="index-wrapper">
    <div class="index-left">
      <div class="index-left-block">
        <h2>全部产品</h2>
        <template v-for="product in productlist">
          <h3>{{ product.title }}</h3>
          <ul>
            <li v-for="item in product.list">
              <a v-bind:href="item.url">{{ item.title }}</a>
            </li>
          </ul>
          <div v-if="product.title == 'PC产品'" class="hr"></div>
        </template>
        <!-- <h3>{{ i.title }}</h3>
        <ul>
          <li v-for="i in productlist">{{ i.title }}</li>
        </ul>-->

        <!-- <h3>手机应用</h3>
        <ul>
          <li>dadada</li>
        </ul>-->
      </div>
      <div class="index-left-block lastest-news">
        <h2>最新消息</h2>
        <ul>
          <li>xin</li>
        </ul>
      </div>
    </div>
    <div class="index-right">
      <div style="width:700px;height:300px;background:red;margin:0 auto">组件代替</div>
      <div class="index-border-list">
        <div class="index-border-item">
          <h2>第一</h2>
          <p>第一描述</p>
          <div class="index-border-button">立即购买</div>
        </div>
        <div class="index-border-item">
          <h2>第二</h2>
          <p>第二描述</p>
          <div class="index-border-button">立即购买</div>
        </div>
        <div class="index-border-item">
          <h2>第三</h2>
          <p>第三描述</p>
          <div class="index-border-button">立即购买</div>
        </div>
        <div class="index-border-item">
          <h2>第四</h2>
          <p>第四描述</p>
          <div class="index-border-button">立即购买</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      productlist: {
        pc: {
          title: "PC产品",
          list: [
            {
              title: "数据统计",
              url: "http://starcraft.com"
            },
            {
              title: "数据预测",
              url: "http://warcraft.com"
            },
            {
              title: "流量分析",
              url: "http://overwatch.com",
              hot: true
            },
            {
              title: "广告发布",
              url: "http://hearstone.com"
            }
          ]
        },
        app: {
          title: "手机应用类",
          list: [
            {
              title: "91助手",
              url: "http://weixin.com"
            },
            {
              title: "产品助手",
              url: "http://weixin.com",
              hot: true
            },
            {
              title: "智能地图",
              url: "http://weixin.com"
            },
            {
              title: "语音助手",
              url: "http://weixin.com",
              hot: true
            }
          ]
        }
      }
    };
  }
};
</script>

<style scoped>
a {
  text-decoration: none;
  color: #444444;
}
.index-wrapper {
  display: flex;
}
.index-left {
  width: 30%;
}
ul {
  list-style-type: none;
}
.index-right {
  width: 70%;
}
.index-left-block {
  margin: 15px;
  background: white;
  border-radius: 15px;
  box-shadow: 0 0 1px #dddddd;
}
.index-left-block .hr {
  border-bottom: 1px solid black;
  margin: 20px 0;
}
.index-left-block h2 {
  background: #4fc08d;
  color: white;
  padding: 15px 10px;
  margin-bottom: 20px;
}
.index-left-block h3 {
  color: #222;
  font-weight: bolder;
  padding: 0 15px 0 15px;
}
.index-left-block ul {
  padding: 0 15px;
}
.index-left-block ul li {
  padding: 5px;
}
.index-border-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
.index-border-item {
  width: 45%;
  height: 125px;
  line-height: ;
  background: white;
  padding-left: 20px;
  margin-right: 1%;
  box-shadow: 0 0 1px #dddddd;
  margin-bottom: 20px;
  border-radius: 0 0 15px 15px;
}
</style>