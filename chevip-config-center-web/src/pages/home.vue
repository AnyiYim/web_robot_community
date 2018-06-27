<template>
  <div>
    <div class="home-page">
      <!--首页-->
      <div v-if="$store.state.user.role === 'ADMIN'">
        <div v-if="robot.length > 0" style="flex-wrap: wrap;" class="flex flex-pack-spacearound">
          <Card v-for="(item, index) in robot" :key="index" style="width: 280px; height: 300px; margin-left: 20px; margin-bottom: 30px; text-align: center">
            <a href="https://geocam.tv/streamer/2576.mjpg" target="view_window"><img src="../public/img/robot.jpg" alt="" width="100%"></a>
            <span style="font-size: 16px; font-weight: bold;">{{(item.place + '区机器人： ') + (item.status && '工作中' || '巡逻中')}}</span>
          </Card>
          <Card style="width: 280px; height: 300px; margin-left: 20px; margin-bottom: 30px; text-align: center">
            <div @click="robot_add"><a><img src="../public/img/add.jpg" alt="" width="100%"></a>
            <span style="font-size: 16px; font-weight: bold;">添加机器人</span></div>
          </Card>
          <Card  style="width: 280px; height: 300px; margin-left: 20px; margin-bottom: 30px; text-align: center">
            <div @click="robot_sub"><a ><img src="../public/img/sub.jpg" alt="" width="100%"></a>
            <span style="font-size: 16px; font-weight: bold;">删除机器人</span></div>
          </Card>
        </div>


      </div>

      <div v-else>
        <div>
          <Button v-if="!flag" type="primary" @click="use_robot" style="width:30%; height:300px; font-size: 36px; margin-left: 13px; margin-top: 1px">{{'委托帮助'}}</Button>
          <Button v-else type="primary" style="width:30%; height:300px; font-size: 36px; margin-left: 13px; margin-top: 1px">{{rid + '号机器人还有' + rtime + '秒到达'}}</Button>
          <Button type="error" style="width:30%; height:300px; font-size: 36px; margin-left: 13px; margin-top: 1px">报警</Button>

        </div>

      </div>
    </div>
  </div>

</template>
<script>
export default {
  data() {
    return {
      role: '',
      robot: [],
      rtime: 270,
      flag: false,

    }
  },
  created: function () {
    if (this.$store.state.user.role === 'ADMIN') {
      this.get_robot();
    }
  },
  methods: {
    get_robot() {
      this.ajax.get('/admin/all_robot').then(rsp => {
        if (rsp.data.code === 0){
          this.robot = rsp.data.data.robol;
        }
      }, err => {
      });
    },
    robot_add() {
      this.ajax.get('/admin/add_robot').then(rsp => {
        if (rsp.data.code === 0){
          this.get_robot();
        }
      }, err => {
      });
    },
    robot_sub() {
      this.ajax.get('/admin/sub_robot').then(rsp => {
        if (rsp.data.code === 0){
          this.get_robot();
        }
      }, err => {
      });
    },

    use_robot() {
      console.log(this.$store.state.user.id);
      this.ajax.get('/admin/use_robot?uid=' + this.$store.state.user.id).then(rsp => {
        if (rsp.data.code === 0){
          this.rid = rsp.data.data;
          this.flag = true;
          let that = this;
          let rtime = that.rtime;
          let interval = window.setInterval(() => {
            if (--that.rtime <= 0) {
              that.rtime = rtime;
              window.clearInterval(interval);
            }
          }, 1000)

        }
      }, err => {
      });
    }


  }
}
</script>
<style lang="less" scoped>
</style>
