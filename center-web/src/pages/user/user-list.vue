<template>
  <div class="car-info-modal flex flex-v">
    <div class="car-info">
      <div class="editCarForm">
        <Form ref="id" label-position="right" :label-width="120" inline>
          <Form-item  label="搜索用户：">
            <div class="flex">
              <Select style="width: 250px" v-model="id" filterable remote :remote-method="loadIdMethod" :loading="loading" placeholder="输入用户名或姓名搜索" @on-change="getUser">
                <Option v-for="(option, index) in options" :value="option.id" :key="index" :label="option.true_name">
                  <div style="display: flex; height: 19px; padding: 2px 0 0 0">
                    <div style="max-width: 150px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;">{{option.true_name + '(' + option.user_name + ')'}}</div>
                    <span style="position: absolute; left: 180px; color: rgb(116,116,116); font-size: 12px">{{option.id}}</span></div>
                </Option>
              </Select>
            </div>
          </Form-item>
        </Form>
        <Card style="width: 798px">
          <div class="info-title">
            <div class="circle" style="background-color: #2d8cf0"></div>
          </div>
          <p style="margin-left: 15px" slot="title">角色信息 {{  id && ': ' + user_info.trueName + '(' + user_info.userName + ')'  }}</p>
          <Transfer
            v-if="id"
            :data="total_key"
            :target-keys="role_key"
            :render-format="role_render"
            @on-change="handleChange"
            :list-style="listStyle"
            :titles="['可分配角色', '用户角色']">
          </Transfer>
          <div v-else><p>暂无角色信息</p></div>
        </Card>
      </div>
    </div>

    <Modal v-model="delModal" :mask-closable="false" :scrollable="false" width="480" @on-ok="deleteRole(del_dateform, del_newKey)">
      <p slot="header" class="modal-header">
        <span>该角色已经与以下地区绑定,确定删除?</span>
      </p>
      <div v-for="(value, key) in clash">
        {{ role_dict[key] }}:<span v-for="value1 in clash[key]">{{ value1 }}</span>
      </div>
    </Modal>
  </div>
</template>

<script>
    export default {
      data() {
        return {
          id: null,
          loading: false,
          options: [],
          can_add: [],
          user_info: {role: [], trueName: '', userName: ''},
          total_key: [],
          role_key: [],
          total_list: [],
          listStyle: {width: '354px', height: '472px'},
          role_dict: {
            'SUPER_USER': 'SUPER_USER', 'VALUER': '评估师', 'STORE_VALUER': '门店评估师', 'STORE_SALES': '门店销售',
            'REGION_MANAGER': '区域经理', 'ADMIN_BUYER_SELLER': '管理员', 'STORAGE_MANAGER': '仓库管理员',
            'VEHICLE_VERIFER': '车辆审核员', 'REGION_DEPUTY_DIRECTOR': '区域副总监', 'REGION_DIRECTOR': '区域总监',
            'STORE_USER': '门店帐号', 'BUYER': '买家帐号', 'GROUP_USER': '集团用户', 'VICE_GENERAL_MANAGER': '副总经理',
            'FINANCE_MANAGER': '财务经理', 'GENERAL_MANAGER': '总经理', 'Finance': '财务', 'Transfer': '过户专员',
            'MRZB': '每日战报接收', 'ARBITRATOR': '仲裁专员', 'ARBITRATE_MANAGER': '仲裁经理',
            'ARBITRATE_DIRECTOR': '仲裁总监', 'SERVICE_DIRECTOR': '服务总监', 'CHEVIP_VALUER': '唯普估价员',
            'GWQM_VALUER': '汽贸二手车部门', 'GROUP_SH': '汽贸审核员', 'SALES_STORAGE': '销售部库存管理',
            'DATA_COLLECTOR': '资料回收员', 'TMP_VEHICLE_OUT_ASSESSOR': '临时车出库审核人', 'SALES_DIRECTOR': '销售总监',
            'ORDER_OBSERVER': '订单观察员', 'COTB_MANAGE': 'CTO统筹员',
          },
          clash: {},
          delModal: false,
          del_dateform: {},
          del_newKey: ''
        }
      },
      methods: {
        init_status() {
          this.can_add= [];
          this.role_key = [];
          this.user_info = {role: [], trueName: '', userName: ''};
          this.can_add = [];
          this.total_key = [];
          this.role_key = [];
          this.total_list = [];
        },
        getUser() {
          this.init_status();
          if (this.id) {
            var dateform = {};
            dateform['id']= this.id;
            this.ajax.post('/users/get_user', dateform).then(rsp => {
              if (rsp.data.code === 0){
                this.can_add = rsp.data.data.can_add;
                for (var k in this.user_info) {
                  this.user_info[k] = rsp.data.data.info[k];
                }
                this.total_key = this.getMockData();
                this.role_key = this.getTargetKeys();
              }
            });
          }
        },
        loadIdMethod (query) {
          if (query && query.length > 1) {
            this.loading = true;
            this.ajax.get('/users/find_name?name=' + query).then(rsp => {
              if (rsp.data.code === 0){
                this.options = rsp.data.data;
              }
              this.loading = false;
            }, err => {
              this.loading = false;
            });
          }
        },
        getMockData () {
          let mockData = [];
          this.total_list = this.can_add.concat(this.user_info.role);
          for (let i = 0; i < this.total_list.length; i++) {
            mockData.push({
              key: i.toString(),
              label: this.total_list[i],
              disabled: false,
            });
          }
          return mockData;
        },
        getTargetKeys () {
          return this.total_key
            .filter(item => this.user_info.role.indexOf(item.label) > -1)
            .map(item => item.key);
        },
        role_render (item) {
          return this.role_dict[item.label] + ' (' + item.label + ')';
        },
        handleChange (newTargetKeys, direction, moveKeys) {
          var dateform = {};
          dateform['user_id']= this.id;
          dateform['op_id'] = this.$store.state.user.id;
          if (direction === 'right') {
            dateform['role'] = '';
            for (let i = 0; i < moveKeys.length; i++){
              dateform['role'] = dateform['role'] + ';' + this.total_key[parseInt(moveKeys[i])].label;
            }
            this.ajax.post('/users/add_role', dateform).then(rsp => {
              if (rsp.data.code === 0){
                this.$Message.success('添加成功');
                this.role_key = newTargetKeys;
              }
            });
          }
          else {
            dateform['role'] = '';
            for (let i = 0; i < moveKeys.length; i++){
              dateform['role'] = dateform['role'] + ';' + this.total_key[parseInt(moveKeys[i])].label;
            }
            this.ajax.post('/users/check_role', dateform).then(rsp => {
              if (rsp.data.code === 0){
                console.log(rsp.data.data);
                if (rsp.data.data) {
                  this.clash = rsp.data.data;
                  console.log(this.clash);
                  this.delModal = true;
                  this.del_dateform = dateform;
                  this.del_newKey = newTargetKeys;
                }
                else {
                  this.deleteRole(dateform, newTargetKeys)
                }
              }
            });
          }
        },

        deleteRole(dateform, newTargetKeys) {
          this.ajax.post('/users/sub_role', dateform).then(rsp => {
            if (rsp.data.code === 0){
              this.$Message.success('删除成功');
              this.role_key = newTargetKeys;
              console.log(dateform);
              console.log(newTargetKeys);
            }
          });
          this.delModal = false;
          this.del_newKey = '';
          this.del_dateform = {};
        }
      }
    }
</script>

<style scoped>

</style>
