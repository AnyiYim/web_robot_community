<template>
  <div>
    <div class="home-page">
      <!--首页-->
      <div v-if="$store.state.user.role === 'ADMIN' || $store.state.user.role === 'ROLE'">
        <div v-if="robot.length > 0" style="flex-wrap: wrap;" class="flex flex-pack-spacearound">
          <Card v-for="(item, index) in robot" :key="index" style="width: 280px; height: 300px; margin-left: 20px; margin-bottom: 30px; text-align: center">
            <a href="https://geocam.tv/streamer/2576.mjpg" target="view_window"><img src="../public/img/robot.jpg" alt="" width="100%"></a>
            <span style="font-size: 16px; font-weight: bold;">{{(item.place + '区机器人： ') + (item.status && '工作中' || '巡逻中')}}</span>
          </Card>
          <Card v-if="$store.state.user.role === 'ADMIN'" style="width: 280px; height: 300px; margin-left: 20px; margin-bottom: 30px; text-align: center">
            <div @click="robot_add"><a><img src="../public/img/add.jpg" alt="" width="100%"></a>
            <span style="font-size: 16px; font-weight: bold;">添加机器人</span></div>
          </Card>
          <Card v-if="$store.state.user.role === 'ADMIN'" style="width: 280px; height: 300px; margin-left: 20px; margin-bottom: 30px; text-align: center">
            <div @click="robot_sub"><a ><img src="../public/img/sub.jpg" alt="" width="100%"></a>
            <span style="font-size: 16px; font-weight: bold;">删除机器人</span></div>
          </Card>
        </div>


      </div>

      <div v-else>

        <div class="flex">
          <Button v-if="flag == 0" type="primary" :loading="uu" @click="use_robot" style="width:400px; height:300px; font-size: 36px; margin-left: 13px; margin-top: 1px">{{'委托帮助'}}</Button>
          <Button v-else-if="flag == 1" type="primary" :loading="loading" style="width:400px; height:300px; font-size: 36px; margin-left: 13px; margin-top: 1px">
            {{rid + '号机器人'}}<br>{{'还有' + rtime + '秒到达'}}
          </Button>

          <div v-else-if="flag == 2" class="robot">
          <Button @click="done_robot" type="primary" style="width:400px; height:300px; font-size: 36px; margin-left: 13px; margin-top: 1px">
            <span class="robot-sub1">{{rid + '号机器人'}}<br>{{'正在为您服务'}}</span>
            <span class="robot-sub2">点击完成服务</span>
          </Button>
          </div>

          <Button type="error" @click="$Message.success('成功报警')" style="width:400px; height:300px; font-size: 36px; margin-left: 53px; margin-top: 1px">报警</Button>

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
      rtime: 20,
      flag: 0,
      loading: false,
      has: false,
      rid: null,
      uu: false,

    }
  },
  created: function () {
    console.log(process.env.API + 'pic/vehicle_pic/upload')
    this.flag = false;
    this.has = false;
    if (this.$store.state.user.role === 'ADMIN' || this.$store.state.user.role === 'ROLE') {
      this.get_robot();
    }
    else {
      this.get_robot_user();
    }
  },
  methods: {
    get_robot() {
      this.ajax.get('/admin/all_robot').then(rsp => {
        if (rsp.data.code === 0) {
          this.robot = rsp.data.data.robol;
        }
      }, err => {
      });
    },
    robot_add() {
      this.ajax.get('/admin/add_robot').then(rsp => {
        if (rsp.data.code === 0) {
          this.get_robot();
        }
      }, err => {
      });
    },
    robot_sub() {
      this.ajax.get('/admin/sub_robot').then(rsp => {
        if (rsp.data.code === 0) {
          this.get_robot();
        }
      }, err => {
      });
    },
    get_robot_user() {
      this.ajax.get('/user/get_robot_user?uid=' + this.$store.state.user.id).then(rsp => {
        if (rsp.data.code === 0 && rsp.data.data) {
          this.has = true;
          this.rid = rsp.data.data;
          this.flag = 2;
        }
      }, err => {
      });
    },
    done_robot() {
      this.ajax.get('/user/done_robot?uid=' + this.$store.state.user.id).then(rsp => {
        if (rsp.data.code === 0) {
          this.has = false;
          this.rid = null;
          this.flag = 0;
          this.$Message.success('服务已完成')
        }
      }, err => {
      });
    },
    use_robot() {
      this.uu = true
      // console.log(this.$store.state.user.id);
      this.ajax.get('/admin/use_robot?uid=' + this.$store.state.user.id).then(
        rsp => {
          if (rsp.data.code === 0) {
            this.$Message.success('机器人成功派遣');
            this.uu = false;
            this.rid = rsp.data.data;
            this.flag = 1;
            let that = this;
            let rtime = that.rtime;
            this.loading = true
            let interval = window.setInterval(() => {
              if (--that.rtime <= 0) {
                that.rtime = rtime;
                window.clearInterval(interval);
              }
              else {
                this.loading = false;
                this.flag = 2
              }
            }, 1000)

          }
        });
    }
  },

}
</script>
<style lang="less" scoped>
</style>
