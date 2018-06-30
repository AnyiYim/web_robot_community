<template>
  <Card class="demo-tabs-style1 panel" style="margin: 20px; width: 90%" >
    <div class="info-title">
      <div class="circle" style="background-color: #2d8cf0"></div>
    </div>
    <p style="margin-left: 15px" slot="title">我发起的问题</p>
    <Button type='primary' style="position: absolute; top:19px; left: 980px; font-size: 14px" @click="AskModal=true">发起投诉</Button>
    <div style="">

      <div v-if="msg.length>0" v-for="(item, index) in msg" :key="index" @click="editPP = item; CallModal=true">
        <Card style="width: 100%; height: 60px;">
          <div style="font-size: 16px; margin-top: 2px; margin-left: 20px">发布于{{item.time}}的一个问题</div>
          <div v-if="!item.flag" style="position: absolute; top:18px; left: 920px; font-size: 16px">{{item.flag || '已答复'}}</div>
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


    <Modal v-model="AskModal" :mask-closable="false" :scrollable="false" width="580">
      <p slot="header" class="modal-header">
        <span>查看问题</span>
      </p>
      <div style="padding: 0 40px 0 40px">
        <Form :label-width="120">
          <FormItem label="我的问题：">
            <Input v-model="call_text" type="textarea" :autosize="{minRows: 5,maxRows: 8}" placeholder="输入您的问题，社区将于24小时内给予你回复"></Input>
          </FormItem>
        </Form>
      </div>
      <div class="flex flex-center" style="padding:0px 0 0px 35px">
      <div @click="submitCall" style="width: 570px; height: 35px;  line-height: 35px; font-size: 16px" class="modal-button ">提 交</div>
      </div>
      <div slot="footer">
      </div>
    </Modal>

    <Modal v-model="CallModal" :mask-closable="false" :scrollable="false" width="580">
      <p slot="header" class="modal-header">
        <span>查看问题</span>
      </p>
      <div style="padding: 0 40px 0 40px">
        <Form :label-width="150">
          <FormItem label="我提出的问题：">
            {{editPP.msg}}
          </FormItem>
          <FormItem label="社区回复：">
            {{editPP.call && editPP.call || '暂无回复，请耐心等待。'}}
          </FormItem>
        </Form>
      </div>
      <!--<div class="flex flex-center" style="padding:0px 0 0px 35px">-->
        <!--<div @click="submitCall" style="width: 570px; height: 35px;  line-height: 35px; font-size: 16px" class="modal-button ">提 交</div>-->
      <!--</div>-->
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
          AskModal: false,
          msg: [],
        }
      },

      created: function () {
        this.loadMsg();
      },
      methods: {
        loadMsg() {
          this.ajax.get('/user/get_msg?uid=' + this.$store.state.user.id).then(response => {
            if (response.data.code === 0) {
              this.msg = response.data.data;
            }
          });
        },
        submitCall () {
          if (this.call_text.length>0) {
            this.ajax.post('/user/call_in', {id: this.$store.state.user.id, msg: this.call_text})
              .then(response => {
                if (response.data.code === 0) {
                  this.$Message.success('提交成功');
                  this.AskModal = false;
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
