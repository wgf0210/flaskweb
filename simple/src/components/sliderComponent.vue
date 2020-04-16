<template>
    <div class="slider-wrapper" @mouseover="clearInv" @mouseout="runInv">
        <!-- 四张轮播图 -->
        <div class="slider-item item1">1</div>
        <div class="slider-item item2">0</div>
        <div class="slider-item item3">3</div>
        <div class="slider-item item4">4</div>
        <!-- 下方的原点 -->
        <ul class="slider-dots">
            <li>&lt;</li>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
            <li>&gt;</li>
        </ul>
    </div>
</template>

<script>
export default {
    props:{
        inv:{
            type:Number,
            default:1000   /* 1000毫秒 */
        }
    },
    data() {
        return {
            
        }
    },
    methods: {
        runInv(){
            setInterval(()=>{

            },this.inv)
        },
        clearInv(){

        }
    },
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
}
.slider-dots li{
    width: 15px;
    height: 15px;
    border-radius: 50%;
    background: #000;
    color: white;
    text-align: center;
    line-height: 15px;
    float: left;
    margin: 0 10px;
    opacity: 0.6;
}
</style>