<template>
  <div>
    <div style="font-size: 18px; font-weight: bold; margin: 2px 12px 12px 12px; color: #000">安保管理值班表</div>

    <div class="flex">
    <Card style="width: 280px; height: 300px;  text-align: center">
      <div class="textbg" style="margin-top:40px;text-align:center; line-height:180px;font-size: 126px; font-weight: bold; color: #eb4b4b">
        {{date.getDate()}}<span style="font-size: 20px; color: #bbbec4">日</span>
      </div>
      <span style="color: #bbbec4; width: 100%; line-height: 270px; height: 270px; font-size: 76px; font-weight: bold;"></span>
    </Card>
    <Card style="width: 280px; height: 300px;  text-align: center">
      <div class="textbg" style="margin-top: 25px">
        <Tag style="margin: 6px" v-for="(item, index) in one" :key="index" :name="index" closable @on-close="handleClose1">{{ item.name }}</Tag>
        <Button style="margin: 6px" icon="ios-plus-empty" type="dashed" size="small" @click="RoleModal=true; role_form.day=1">添加值班人员</Button>
      </div>
      <span style="color: #bbbec4; width: 100%; line-height: 270px; height: 270px; font-size: 76px; font-weight: bold;">周一</span>
    </Card>
    <Card style="width: 280px; height: 300px;  text-align: center">
      <div class="textbg" style="margin-top: 25px">
        <Tag style="margin: 6px" v-for="(item, index) in two" :key="index" :name="index" closable @on-close="handleClose2">{{ item.name }}</Tag>
        <Button style="margin: 6px" icon="ios-plus-empty" type="dashed" size="small" @click="RoleModal=true; role_form.day=2">添加值班人员</Button>
      </div>
      <span style="color: #bbbec4; width: 100%; line-height: 270px; height: 270px; font-size: 76px; font-weight: bold;">周二</span>
    </Card>
    <Card style="width: 280px; height: 300px;  text-align: center">
      <div class="textbg" style="margin-top: 25px">
        <Tag style="margin: 6px" v-for="(item, index) in three" :key="index" :name="index" closable @on-close="handleClose3">{{ item.name }}</Tag>
        <Button style="margin: 6px" icon="ios-plus-empty" type="dashed" size="small" @click="RoleModal=true; role_form.day=3">添加值班人员</Button>
      </div>
      <span style="color: #bbbec4; width: 100%; line-height: 270px; height: 270px; font-size: 76px; font-weight: bold;">周三</span>

    </Card>
    </div>
    <div class="flex">
      <Card style="width: 280px; height: 300px;  text-align: center">
        <div class="textbg" style="margin-top: 25px">
          <Tag style="margin: 6px" v-for="(item, index) in four" :key="index" :name="index" closable @on-close="handleClose4">{{ item.name }}</Tag>
          <Button style="margin: 6px" icon="ios-plus-empty" type="dashed" size="small" @click="RoleModal=true; role_form.day=4">添加值班人员</Button>
        </div>
        <span style="color: #bbbec4; width: 100%; line-height: 270px; height: 270px; font-size: 76px; font-weight: bold;">周四</span>
      </Card>
      <Card style="width: 280px; height: 300px;  text-align: center">
        <div class="textbg" style="margin-top: 25px">
          <Tag style="margin: 6px" v-for="(item, index) in five" :key="index" :name="index" closable @on-close="handleClose5">{{ item.name }}</Tag>
          <Button style="margin: 6px" icon="ios-plus-empty" type="dashed" size="small" @click="RoleModal=true; role_form.day=5">添加值班人员</Button>
        </div>
        <span style="color: #bbbec4; width: 100%; line-height: 270px; height: 270px; font-size: 76px; font-weight: bold;">周五</span>
      </Card>
      <Card style="width: 280px; height: 300px;  text-align: center">
        <div class="textbg" style="margin-top: 25px">
          <Tag style="margin: 6px" v-for="(item, index) in six" :key="index" :name="index" closable @on-close="handleClose6">{{ item.name }}</Tag>
          <Button style="margin: 6px" icon="ios-plus-empty" type="dashed" size="small" @click="RoleModal=true; role_form.day=6">添加值班人员</Button>
        </div>
        <span style="color: #bbbec4; width: 100%; line-height: 270px; height: 270px; font-size: 76px; font-weight: bold;">周六</span>
      </Card>
      <Card style="width: 280px; height: 300px;  text-align: center">
        <div class="textbg" style="margin-top: 25px;">
          <Tag style="margin: 6px" v-for="(item, index) in seven" :key="index" :name="index" closable @on-close="handleClose7">{{ item.name }}</Tag>
          <Button style="margin: 6px" icon="ios-plus-empty" type="dashed" size="small" @click="RoleModal=true; role_form.day=7">添加值班人员</Button>
        </div>
        <span style="color: #bbbec4; width: 100%; line-height: 270px; height: 270px; font-size: 76px; font-weight: bold;">周日</span>
      </Card>
    </div>
    <Modal v-model="RoleModal" :mask-closable="false" :scrollable="false" width="380">
      <p slot="header" class="modal-header">
        <span>添加值班保安</span>
      </p>
      <div style="padding: 0 10px 0 10px">
        <Form :model="role_form" :label-width="80">
          <FormItem label="添加保安">
            <Select v-model="role_form.id" filterable remote :remote-method="loadIdMethod" :loading="loading" placeholder="请输入用户名" @on-change="getEmployee">
              <Option v-for="(option, index) in users" :value="option.id" :key="index" :label="option.name">
                <div style="display: flex; height: 19px; padding: 2px 0 0 0">
                  <div style="max-width: 150px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;">{{option.name}}</div>
                </div>
                  <!--<span style="position: absolute; left: 180px; color: rgb(116,116,116); font-size: 12px">{{option.id}}</span></div>-->
              </Option>
            </Select>
          </FormItem>
        </Form>
      </div>
      <div class="flex flex-center" style="padding:0px 0 0px 35px">
        <div @click="submitUserInfo" style="width: 390px" class="modal-button ">提 交</div>
      </div>
      <div slot="footer">
      </div>
    </Modal>
  </div>
</template>

<script>
    export default {
      data() {
        return {
          date: '',
          one: [],
          two: [],
          three: [],
          four: [],
          five: [],
          six: [],
          seven: [],
          RoleModal: false,
          users: [],
          role_form: {
            id: '',
            day: '',
          }
        }
      },
      created: function () {
        this.date = new Date();
        this.get_role();
      },
      methods: {
        get_role() {
          this.ajax.get('/admin/get_role')
            .then(rsp => {
              if (rsp.data.code === 0){
                this.one = rsp.data.data[1];
                this.two = rsp.data.data[2];
                this.three = rsp.data.data[3];
                this.four = rsp.data.data[4];
                this.five = rsp.data.data[5];
                this.six = rsp.data.data[6];
                this.seven = rsp.data.data[7];

                console.log(this.one)
              }
            });
        },
        handleClose1 (event, index) {
          console.log(index);
          this.ajax.get('/admin/del_role?day=1&id='+this.one[index].id)
            .then(rsp => {
              if (rsp.data.code === 0){
                this.$Message.success('删除成功');
                this.one.splice(index, 1);
              }
            });
        },
        handleClose2 (event, index) {
          console.log(index);
          this.ajax.get('/admin/del_role?day=2&id='+this.two[index].id)
            .then(rsp => {
              if (rsp.data.code === 0){
                this.$Message.success('删除成功');
                this.two.splice(index, 1);
              }
            });
        },
        handleClose3 (event, index) {
          console.log(index);
          this.ajax.get('/admin/del_role?day=3&id='+this.three[index].id)
            .then(rsp => {
              if (rsp.data.code === 0){
                this.$Message.success('删除成功');
                this.three.splice(index, 1);
              }
            });
        },
        handleClose4 (event, index) {
          console.log(index);
          this.ajax.get('/admin/del_role?day=4&id='+this.four[index].id)
            .then(rsp => {
              if (rsp.data.code === 0){
                this.$Message.success('删除成功');
                this.four.splice(index, 1);
              }
            });
        },
        handleClose5 (event, index) {
          console.log(index);
          this.ajax.get('/admin/del_role?day=5&id='+this.five[index].id)
            .then(rsp => {
              if (rsp.data.code === 0){
                this.$Message.success('删除成功');
                this.five.splice(index, 1);
              }
            });
        },
        handleClose6 (event, index) {
          console.log(index);
          this.ajax.get('/admin/del_role?day=6&id='+this.six[index].id)
            .then(rsp => {
              if (rsp.data.code === 0){
                this.$Message.success('删除成功');
                this.six.splice(index, 1);
              }
            });
        },
        handleClose7 (event, index) {
          console.log(index);
          this.ajax.get('/admin/del_role?day=7&id='+this.seven[index].id)
            .then(rsp => {
              if (rsp.data.code === 0){
                this.$Message.success('删除成功');
                this.seven.splice(index, 1);
              }
            });
        },
        loadIdMethod (query) {
          this.ajax.get('/admin/get_tt_user?text=' + query)
            .then(rsp => {
              if (rsp.data.code === 0){
                this.users = rsp.data.data;
              }
            }, err => {
            });
        },
        submitUserInfo () {
          this.ajax.post('/admin/add_role', this.role_form).then(response => {
            if (response.data.code === 0) {
              this.$Message.success('绑定成功');
              this.RoleModal=false;
              this.role_form = {id: null, day: null};
              this.users = [];
              this.get_role()
            }
          });
        },
      },
    }
</script>

<style scoped>

</style>
