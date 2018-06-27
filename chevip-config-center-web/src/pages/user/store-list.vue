<template>
  <div class="car-info-modal flex flex-v">
    <div class="car-info">
      <div class="editCarForm">
        <Form ref="id" label-position="right" :label-width="140" inline>
          <Form-item  label="选择门店用户：">
            <div class="flex">
              <Select style="width: 250px" v-model="sid" filterable placeholder="请选择门店" >
                <Option v-for="(item, index) in storeList" :value="item.id" :key="index" :label="item.store_name">
                  <span style="font-size: 13px">{{ item.store_name }}</span>
                </Option>
              </Select>
              <Select style="width: 250px; margin-left: 20px" v-model="id" filterable remote :remote-method="loadIdMethod" :loading="loading" placeholder="请输入分配的用户名或姓名" @on-change="getEmployee">
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
          <p style="margin-left: 15px" slot="title">门店角色信息 {{  sid && id && ': ' + user_info.true_name + '(' + user_info.user_name + ')'  }}</p>
          <Transfer
            v-if="id && sid"
            :data="total_key"
            :target-keys="role_key"
            :render-format="role_render"
            @on-change="handleChange"
            :list-style="listStyle"
            :titles="['可分配角色', '本门店角色']">
          </Transfer>
          <div v-else><p>暂无角色信息</p></div>
        </Card>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        id: null,
        sid: null,
        store_name: '',
        loading: false,
        storeList: [],
        options: [],
        can_add: [],
        user_info: {store_role: [], user_role:[], true_name: '', user_name: ''},
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
        }
      }
    },
    created: function () {
      this.getStore();
    },
    methods: {
      init_status() {
        this.can_add= [];
        this.role_key = [];
        this.user_info = {store_role: [], user_role:[], true_name: '', user_name: ''};
        this.can_add = [];
        this.total_key = [];
        this.role_key = [];
        this.total_list = [];
      },
      getStore() {
        this.ajax.get('/vehicle/get_all_store')
          .then(rsp => {
            if (rsp.data.code === 0){
              this.storeList = rsp.data.data;
            }
          });
      },
      getEmployee() {
        this.init_status();
        if (this.id) {
          var dateform = {};
          dateform['id']= this.id;
          dateform['sid'] = this.sid;
          this.ajax.post('/users/get_employee', dateform).then(rsp => {
              if (rsp.data.code === 0){
                console.log(rsp.data.data.info);
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
        this.total_list = this.user_info.user_role;
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
          .filter(item => this.user_info.store_role.indexOf(item.label) > -1)
          .map(item => item.key);
      },
      role_render (item) {
        return this.role_dict[item.label] + ' (' + item.label + ')';
      },
      handleChange (newTargetKeys, direction, moveKeys) {
        var dateform = {};
        dateform['user_id']= this.id;
        dateform['store_id'] = this.sid;
        dateform['op_id'] = this.$store.state.user.id;
        if (direction === 'right') {
          dateform['role'] = '';
          for (let i = 0; i < moveKeys.length; i++){
            dateform['role'] = dateform['role'] + ';' + this.total_key[parseInt(moveKeys[i])].label;
          }
          this.ajax.post('/users/add_store_role', dateform).then(rsp => {
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
          this.ajax.post('/users/sub_store_role', dateform).then(rsp => {
            if (rsp.data.code === 0){
              this.$Message.success('删除成功');
              this.role_key = newTargetKeys;
            }
          });
        }
      }
    }
  }
</script>

<style scoped>

</style>
