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
              <span v-if="item.hot" style="color:white;background:purple;font-size:13px">HOT</span>
            </li>
          </ul>
          <div v-if="!product.last" class="hr"></div>
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
          <li v-for="item in newList">
            <a v-bind:href="item.url">{{ item.title }}</a>
          </li>
        </ul>
      </div>
    </div>
    <div class="index-right">
      <SliderComponent></SliderComponent>
      <div class="index-border-list">
        <div class="index-border-item" v-for="item in borderlist">
          <div class="index-border-item-inner">
            <h2>{{ item.title }}</h2>
            <p>{{ item.description }}/p>
            <div class="index-border-button">立即购买</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import SliderComponent from '../components/sliderComponent'

export default {
  // 注册
  components:{
    SliderComponent
  },
  mounted() {
    // 接口获取数据
    axios.post('api/getnewList')  /* 接口 */
    .then((res) => {      /*请求成功*/  
      console.log(res)    /*打印 */
      this.newList = res.data.list
    })
    .catch((error) => {   /* 请求失败 */
      console.log(error)
    });

    axios.get('api/getproductlist')
    .then((res) => {     
      console.log(res)
      this.productlist = res.data
    })
    .catch((error) => {  
      console.log(error)
    });

    axios.get('api/getborderlist') 
    .then((res) => {    
      console.log(res)
      this.borderlist = res.data
    })
    .catch((error) => { 
      console.log(error)
    })
  },
  data() {
    return {
      newList:[],
      productlist:null,
      borderlist:null
    }
  },
}
// export default{
//   data() {
//     return {
//       newList: [
//         {
//           title: "数据统计",
//           url: "http://starcraft.com"
//         },
//         {
//           title: "数据预测",
//           url: "http://warcraft.com"
//         },
//         {
//           title: "流量分析",
//           url: "http://overwatch.com",
//           hot: true
//         },
//         {
//           title: "广告发布",
//           url: "http://hearstone.com"
//         }
//       ],
//       productlist: {
//         pc: {
//           title: "PC产品",
//           list: [
//             {
//               title: "数据统计",
//               url: "http://starcraft.com"
//             },
//             {
//               title: "数据预测",
//               url: "http://warcraft.com"
//             },
//             {
//               title: "流量分析",
//               url: "http://overwatch.com",
//               hot: true
//             },
//             {
//               title: "广告发布",
//               url: "http://hearstone.com"
//             }
//           ]
//         },
//         app: {
//           title: "手机应用类",
//           last: true,
//           list: [
//             {
//               title: "91助手",
//               url: "http://weixin.com"
//             },
//             {
//               title: "产品助手",
//               url: "http://weixin.com",
//               hot: true
//             },
//             {
//               title: "智能地图",
//               url: "http://weixin.com"
//             },
//             {
//               title: "语音助手",
//               url: "http://weixin.com",
//               hot: true
//             }
//           ]
//         }
//       }
//     };
//   }
// }
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
  width: 300px;
}
ul {
  list-style-type: none;
}
.index-right {
  width: 900px;
  margin-top: 18px;
}
.index-left-block {
  margin: 15px;
  background: white;
  border-radius: 15px;
  box-shadow: 0 0 1px #dddddd;
}
.index-left-block .hr {
  border-bottom: 1px solid rgba(226, 218, 218, 0.671);
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
  justify-content: space-between;
  margin-top: 15px;
}
.index-border-item {
  width: 400px;
  height: 125px;
  background: white;
  box-shadow: 0 0 1px #dddddd;
  border-radius: 0 0 15px 15px;
  margin-bottom: 20px;
  padding: 20px;
}
.index-border-item-inner {
  padding-left: 180px;
  background-image: url(../assets/logo.png);
  background-repeat: no-repeat;
  background-size: 30%;
}
.index-border-item-inner h2 {
  font-size: 18px;
  font-weight: bolder;
  color: #000;
  margin-bottom: 15px;
}
.index-border-item-inner p {
  margin-bottom: 20px;
}
.index-border-button {
  width: 80px;
  height: 40px;
  background: rgb(121, 167, 75);
  color: white;
  border-radius: 5px;
  line-height: 40px;
  text-align: center;
}
</style>