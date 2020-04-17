<template>
    <div class="slider-wrapper" @mouseover="clearInv" @mouseout="runInv">
        <!-- 四张轮播图 -->
        <div v-show="nowIndex===index" class="slider-item item1" v-bind:class="['item'+[index+1]]" v-for="(item,index) in sliderimglist" v-bind:key="index">
            <a href="">
                <img v-bind:src="item" alt="" style="width:900px;height:500px">
            </a>
        </div>
        <!-- 上一张，下一张： 写成一个button，避免跳转 -->
        <a v-on:click="preHander" href="javascript:viod(0)" class="btn pre-btn">&lt;</a>
        <a v-on:click="autoPlay" href="javascript:viod(0)" class="btn next-btn">&gt;</a>
        <!-- 下方的原点 -->
        <ul class="slider-dots">
            <li v-on:click="clickDot(index)" v-for="(item,index) in sliderimglist" v-bind:key="index">{{ index+1 }}</li>
        </ul>
    </div>
</template>

<script>
export default {
    data() {
        return {
            nowIndex:0,
            sliderimglist:[
                require('../assets/pic1.jpg'),
                require('../assets/pic2.jpg'),
                require('../assets/pic3.jpg'),
                require('../assets/pic4.jpg')
            ]
        }
    },
    methods: {
        preHander(){
            this.nowIndex--;
            if(this.nowIndex<0){
                this.nowIndex = 3
            }
        },
        // nextHander(){
        //     this.autoPlay
        // },
        clickDot(index){
            this.nowIndex = index
        },
        autoPlay(){
            this.nowIndex++;
            if(this.nowIndex>3){
                this.nowIndex = 0
            }
        },
        runInv(){
            this.invId = setInterval(this.autoPlay,1000)
        },
        clearInv(){
            clearInterval(this.invId)
        }
    },
    created(){
        console.log('调用')
        this.runInv()
    }
}
</script>

<style>
.slider-wrapper{
    width: 900px;
    height: 500px;
    background: red;
    position: relative;
}
.slider-item{
    width: 900px;
    height: 500px;
    text-align: center;
    line-height: 500px;
    font-size: 40px;
    position:absolute;
}
.item1{
    z-index: 100;
}
.item2{
    z-index: 90;
}
.item3{
    z-index: 80;
}
.item4{
    z-index: 70;
}
.slider-dots{
    position: absolute;
    right: 20px;
    bottom: 20px;
    list-style: none;
    z-index: 200;
}
.slider-dots li{
    width: 15px;
    height: 15px;
    border-radius: 50%;
    background: red;
    color: white;
    text-align: center;
    line-height: 15px;
    float: left;
    margin: 0 10px;
    opacity: 0.6;
}
.btn{
    display: inline-block;
    width: 50px;
    height: 50px;
    color: white;
    background: #000;
    font-size: 40px;
    text-align: center;
    line-height: 50px;
    position: absolute;
    top: 50%;
    margin-top: -25px;
    z-index: 300;
    text-decoration: none;
    opacity: 0.6;
}
.pre-btn{
    left:10px
}
.next-btn{
    right: 10px;
}
</style>