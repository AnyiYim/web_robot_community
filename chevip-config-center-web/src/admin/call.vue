<template>
  <Card class="demo-tabs-style1 panel" style="margin: 20px; width: 90%" >
    <div class="info-title">
      <div class="circle" style="background-color: #2d8cf0"></div>
    </div>
    <p style="margin-left: 15px" slot="title">居民问题反馈</p>
    <div style="">

      <div v-if="msg.length>0" v-for="(item, index) in msg" :key="index" @click="editPP = item; CallModal=true">
      <Card style="width: 100%; height: 60px;">
        <div style="font-size: 16px; margin-top: 2px; margin-left: 20px">来自{{item.user_name}}的一个问题</div>
        <div style="position: absolute; top:18px; left: 920px; font-size: 16px">{{item.time}}</div>
      </Card></div>
      <div v-else class="guest_list">
        <table border="0" cellspacing="0" cellpadding="0">
          <tr >
            <Card style="margin-top: 5px;text-align: center">
              <div class="flex flex-center">
                <div>无匹配数据</div>
              </div>
            </Card>
          </tr>
        </table>
      </div>
    </div>

    <Modal v-model="CallModal" :mask-closable="false" :scrollable="false" width="580">
      <p slot="header" class="modal-header">
        <span>回复反馈</span>
      </p>
      <div style="padding: 0 40px 0 40px">
        <Form :label-width="120">
          <FormItem label="问题：">
            {{editPP.msg}}
          </FormItem>
          <FormItem label="解决方案：">
            <Input v-model="call_text" type="textarea" :autosize="{minRows: 5,maxRows: 8}" placeholder="输入社区对问题的反馈"></Input>
          </FormItem>
        </Form>
      </div>
      <div class="flex flex-center" style="padding:0px 0 0px 35px">
        <div @click="submitCall" style="width: 570px" class="modal-button ">提 交</div>
      </div>
      <div slot="footer">
      </div>
    </Modal>

  </Card>
</template>

<script>
    export default {
      data() {
        return {
          call_text: '',
          editPP: {},
          CallModal: false,
          msg: [],
        }
      },

      created: function () {
        this.loadMsg();
      },
      methods: {
        loadMsg() {
          this.ajax.get('/admin/get_msg').then(response => {
            if (response.data.code === 0) {
              this.msg = response.data.data;
            }
          });
        },
        submitCall () {
          if (this.call_text.length>0) {
            this.ajax.post('/admin/call_back', {id: this.editPP.id, call: this.call_text})
              .then(response => {
                // console.log('绑定用户', response.data.data);
                if (response.data.code === 0) {
                  this.$Message.success('回复成功');
                  this.CallModal = false;
                  this.editPP = {};
                  this.call_text = '';
                  this.loadMsg()
                }
              });
          }
        },
      },
    }
</script>

<style scoped>

</style>
