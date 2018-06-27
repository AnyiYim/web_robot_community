<template>
  <div class="demo-tabs-style1 panel" style="margin: 20px;padding: 30px; width: 90%" >
    <div class="search">
      <div class="search-row flex">
        <div style="margin-left: 50px" class="search-row-item">
          条件：
          <Input v-model="search" placeholder="输入区域名搜索"></Input>
        </div>
      </div>
      <div style="right: 80px; top:0px; height: auto;" class="search-right2 flex ">
        <Button @click="PlaceModal = true" style="font-size:14px; margin-top: 10px; padding: 4px 16px" class="myGhostButton ">
          <span>新增区域</span>
        </Button>
        <Button @click="searching=true; changePage(1)"  :loading="searching" style="margin-left: 15px; border-radius: 4px; font-size:14px; margin-top: 10px; padding: 4px 30px; background-color: #f92f47; color: #fff">
          <span v-if="searching">搜索中...</span>
          <span v-else>搜索</span>
        </Button>
      </div>
    </div>
    <div style="margin-top: 30px">
      <div class="guest_list">
        <table border="0" cellspacing="0" cellpadding="0">
          <tr class="table_title">
            <th><div style="width: 190px">区域名称</div></th>
            <th><div style="width: 190px">区域全称</div></th>
            <th><div style="width: 220px">所属门店</div></th>
            <th><div style="width: 250px">区域车牌</div></th>
            <th><div style="width: 380px; margin-left: -30px">操作</div></th>
          </tr>
        </table>
      </div>

      <div v-if="tree.length > 0" class="guest_list">
        <table border="0" cellspacing='0' cellpadding="0">
          <tr v-for="(item, index) in tree" :key="index" style="height:63px; cursor: pointer">
            <div class="table-body">
              <td style="margin-left:20px; text-align: center">
                <div style="width: 200px">{{item.name }}</div>
              </td>
              <td><div style="width: 200px">{{item.fullname}}</div></td>
              <td><div style="width: 250px">{{ item.store }}</div></td>
              <td><div style="width: 220px">{{ item.local_license}}</div></td>
              <td style="text-align: center; width: 400px">
                <div style="margin-left: 65px; width: 350px; text-align: left ">
                <Button @click.shop="item.list = !item.list" style="margin-top: 10px; padding: 4px 16px;" class="myGhostButton ">
                  <span>查看仓库</span>
                </Button>
                <Button v-if="!item.store" @click="editingId=item.id; BindModal = true" style="margin-top: 10px; padding: 4px 16px; background-color: #f92f47; color: #fff" >
                  <span>绑定门店</span>
                </Button>
                <Button @click="editingId=item.id; getRole(); RoleModal = true; " style="margin-top: 10px; padding: 4px 16px; background-color: #f92f47; color: #fff" >
                  <span>绑定用户</span>
                </Button>
                </div>
              </td>
            </div>
            <div v-if="item.list" class="flex remark">
              <div style="width: 800px;">
                <div v-for="item2 in item.places" class="remark-content flex">
                  <div style="background-color: #05beaf"class="circle"></div>
                  <div>
                    {{item2.name + ' (' + item2.fullname + ')'}}
                  </div>
                  <div style="min-width: 160px">
                    <span class="remark-content-date">{{'车位数: ' + item2.seat_count}}</span>
                  </div>
                </div>
                <div v-if="item.places.length <= 0" class="remark-content">
                  <span class="red3">请点击右侧新增按钮新增仓库</span>
                </div>
              </div>
              <div style="position: absolute;right: 205px" class="flex flex-v">
                <Button @click="editingId=item.id; RepertoryModal = true"  style="margin-top: 10px; padding: 4px 16px" class="myGhostButton ">新增仓库</Button>
              </div>
            </div>
          </tr>
        </table>
      </div>
      <div v-if="tree.length <= 0" class="guest_list">
        <table border="0" cellspacing="0" cellpadding="0">
          <tr >
            <Card style="margin-top: 5px;text-align: center">
              <div class="flex flex-center">
                <img src="../../public/img/404.png">
                <div>无匹配数据</div>
              </div>
            </Card>
          </tr>
        </table>
      </div>
      <div v-if="total > 0" class="text-center" style="margin-right: 50px;margin-top: 40px">
        <Page v-on:on-change="changePage" :total="total" show-total :page-size="pageSize"></Page>
      </div>
    </div>


    <Modal v-model="RepertoryModal" :mask-closable="false" :scrollable="false" width="350">
      <p slot="header" class="modal-header">
        <span>新增仓库</span>
      </p>
      <div style="padding: 10px">
        <Form :model="new_repertory" :rules="ruleValidate"  :label-width="60">
          <FormItem prop="name" label="名称">
            <Input v-model="new_repertory.name" placeholder="请输入仓库名简称"></Input>
          </FormItem>
          <FormItem prop="fullname" label="全称">
            <Input v-model="new_repertory.fullname" placeholder="请输入仓库名全称"></Input>
          </FormItem>
          <FormItem label="车位数">
            <Input v-model="new_repertory.seat_count" placeholder="请输入车位数"></Input>
          </FormItem>
        </Form>
      </div>
      <div class="flex flex-center" style="margin:20px 0 0px 40px">
        <div @click="submitRepertoryInfo" class="modal-button ">提交</div>
      </div>
      <div slot="footer">
      </div>
    </Modal>

    <Modal v-model="PlaceModal" :mask-closable="false" :scrollable="false" width="420">
      <p slot="header" class="modal-header">
        <span>新增区域</span>
      </p>
      <div style="padding: 20px">
        <Form :model="new_place" :rules="ruleValidate"  :label-width="80">
          <FormItem  prop="name" label="名称">
            <Input v-model="new_place.name" placeholder="请输入仓库名简称"></Input>
          </FormItem>
          <FormItem prop="fullname" label="全称">
            <Input v-model="new_place.fullname" placeholder="请输入仓库名全称"></Input>
          </FormItem>
          <FormItem label="绑定门店">
            <Select v-model="new_place.store_id" filterable placeholder="请选择门店" >
              <Option v-for="(item, index) in storeList" :value="item.id" :key="index" :label="item.store_name">
                <span style="font-size: 13px">{{ item.store_name }}</span>
              </Option>
            </Select>
          </FormItem>
          <FormItem prop="license" label="区域车牌">
            <Input v-model="new_place.license" placeholder="请输入区域车牌, 以';'隔开"></Input>
          </FormItem>
        </Form>
      </div>
      <div class="flex flex-center" style="margin:20px 0 0px 40px">
        <div @click="submitPlaceInfo" class="modal-button ">提交</div>
      </div>
      <div slot="footer">
      </div>
    </Modal>

    <Modal v-model="BindModal" :mask-closable="false" :scrollable="false" width="380">
      <p slot="header" class="modal-header">
        <span>绑定门店</span>
      </p>
      <div style="padding: 0 10px 0 10px">
        <Form :model="bind_form" :label-width="80">
          <FormItem label="绑定门店">
            <Select v-model="bind_form.sid" filterable placeholder="请选择门店" >
              <Option v-for="(item, index) in storeList" :value="item.id" :key="index" :label="item.store_name">
                <span style="font-size: 13px">{{ item.store_name }}</span>
              </Option>
            </Select>
          </FormItem>
        </Form>
      </div>
      <div class="flex flex-center" style="padding:0px 0 0px 35px">
        <div @click="submitBindInfo" style="width: 390px" class="modal-button ">提 交</div>
      </div>
      <div slot="footer">
      </div>
    </Modal>

    <Modal v-model="RoleModal" :mask-closable="false" :scrollable="false" width="580">
      <p slot="header" class="modal-header">
        <span>绑定用户</span>
      </p>

      <Tabs size="small" style="margin-top: -20px">
        <TabPane label="资料回收员">
          <Tag v-for="(item, index) in dc_user" :key="index" :name="index" closable @on-close="dc_handleClose">{{ item.user_name + ' (' + item.true_name + ')' }}</Tag>
          <Button icon="ios-plus-empty" type="dashed" size="small" @click="UserModal=true; role_form.role='DATA_COLLECTOR'; role_form.pid=editingId">添加标签</Button>
        </TabPane>
        <TabPane label="仓库管理员">
          <Tag v-for="(item, index) in sm_user" :key="index" :name="index" closable @on-close="sm_handleClose">{{ item.user_name + ' (' + item.true_name + ')' }}</Tag>
          <Button icon="ios-plus-empty" type="dashed" size="small" @click="UserModal=true; role_form.role='STORAGE_MANAGER'; role_form.pid=editingId">添加标签</Button>
          <!--标签二的内容-->
        </TabPane>
        <TabPane label="临时车出库审核人">
          <Tag v-for="(item, index) in ta_user" :key="index" :name="index" closable @on-close="ta_handleClose">{{ item.user_name + ' (' + item.true_name + ')' }}</Tag>
          <Button icon="ios-plus-empty" type="dashed" size="small" @click="UserModal=true; role_form.role='TMP_VEHICLE_OUT_ASSESSOR'; role_form.pid=editingId">添加标签</Button>
        </TabPane>
      </Tabs>
      <div slot="footer">
      </div>
    </Modal>

    <Modal v-model="UserModal" :mask-closable="false" :scrollable="false" width="380">
      <p slot="header" class="modal-header">
        <span>添加绑定用户</span>
      </p>
      <div style="padding: 0 10px 0 10px">
        <Form :model="role_form" :label-width="80">
          <FormItem label="添加用户">
            <Select v-model="role_form.user_id" filterable remote :remote-method="loadIdMethod" :loading="loading" placeholder="请输入用户名或姓名" @on-change="getEmployee">
              <Option v-for="(option, index) in users" :value="option.id" :key="index" :label="option.true_name">
                <div style="display: flex; height: 19px; padding: 2px 0 0 0">
                  <div style="max-width: 150px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;">{{option.true_name + '(' + option.user_name + ')'}}</div>
                  <span style="position: absolute; left: 180px; color: rgb(116,116,116); font-size: 12px">{{option.id}}</span></div>
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
    data () {
      return {
        search: '',
        id: null,
        limit: 10,
        offset: 0,
        search_text: null,
        searching: false,
        total: null,
        pageSize: 10,
        tree: [],
        loading: false,
        options: [],
        remark: [],
        editingId: null,
        PlaceModal: false,
        RepertoryModal: false,
        BindModal: false,
        RoleModal: false,
        UserModal: false,
        storeList: [],
        new_repertory: {name: '', fullname: '', seat_count: 0, parent_id: null,},
        new_place: {name: '', fullname: '', store_id: null, local_license: '',},
        bind_form: {pid: null, sid: null,},
        role_form: {user_id: null, pid: null, role: ''},
        ruleValidate: {
          name: [{required: true, message: 'The name cannot be empty', trigger: 'blur'}],
          fullname: [{required: true, message: 'The full name cannot be empty', trigger: 'blur'},],
          license: [{required: true, message: 'The license place cannot be empty', trigger: 'blur'},],
        },
        dc_user: [],
        sm_user: [],
        ta_user: [],
        users: [],
      }
    },
    created: function () {
      this.loadList();
      this.getStore();
    },
    methods: {
      getRole() {
        this.ajax.get('/place/get_role?pid='+this.editingId)
          .then(rsp => {
            if (rsp.data.code === 0){
              this.dc_user = rsp.data.data.DATA_COLLECTOR;
              this.sm_user = rsp.data.data.STORAGE_MANAGER;
              this.ta_user = rsp.data.data.TMP_VEHICLE_OUT_ASSESSOR;
            }
          });
      },
      getStore() {
        this.ajax.get('/vehicle/get_all_store')
          .then(rsp => {
            if (rsp.data.code === 0){
              this.storeList = rsp.data.data;
            }
          });
      },
      loadIdMethod (query) {
        if (query && query.length > 1) {
          this.loading = true;
          this.ajax.get('/users/find_name?name=' + query).then(rsp => {
            if (rsp.data.code === 0){
              this.users = rsp.data.data;
            }
            this.loading = false;
          }, err => {
            this.loading = false;
          });
        }
      },
      init(){
        this.search = '';
        this.editingId = null;
        this.RepertoryModal = false;
        this.PlaceModal = false;
        this.BindModal = false;
        this.bind_form = {pid: null, sid: null,};
        this.new_repertory = {name: '', fullname: '', seat_count: 0, parent_id: null,};
        this.new_place = {name: '', fullname: '', store_id: null, license: '',}
      },
      loadList() {
        this.changePage(1);
      },
      changePage(page) {
        var params = '';
        params += 'offset=' + (Number(page) - 1) * 10 + '&limit=10';
        if (this.search) params += '&search=' + this.search;
        this.ajax.get('/place/tree?' + params).then(response => {
          if (response.data.code === 0) {
            for (var k in response.data.data.tree) {
              response.data.data.tree[k].list = false;
            }
            console.log(response.data.data.tree);
            this.total = response.data.data.total;
            this.tree = response.data.data.tree;
            this.searching = false;
          }
          this.options=[];
          document.body.scrollTop = 0;
          document.documentElement.scrollTop = 0;
        }).catch(err => {
          this.searching = false;
        });
      },
      submitRepertoryInfo () {
        this.new_repertory.parent_id = this.editingId;
        this.ajax.post('/place/create_place', this.new_repertory).then(response => {
          console.log('新增仓库', response.data.data);
          if (response.data.code === 0) {
            this.$Message.success('创建成功');
            this.changePage(1);
            this.init()
          }
        });
      },
      submitPlaceInfo () {
        this.ajax.post('/place/create_root', this.new_place).then(response => {
          console.log('新增区域', response.data.data);
          if (response.data.code === 0) {
            this.$Message.success('创建成功');
            this.changePage(1);
            this.init()
          }
        });
      },
      submitBindInfo () {
        this.bind_form.pid = this.editingId;
        this.ajax.post('/place/bind_store', this.bind_form).then(response => {
          console.log('绑定门店', response.data.data);
          if (response.data.code === 0) {
            this.$Message.success('绑定成功');
            this.changePage(1);
            this.init()
          }
        });
      },
      submitUserInfo () {
        this.ajax.post('/place/add_role', this.role_form).then(response => {
          console.log('绑定用户', response.data.data);
          if (response.data.code === 0) {
            this.$Message.success('绑定成功');
            this.UserModal=false;
            this.role_form = {user_id: null, pid: null, role: ''};
            this.users = [];
            this.getRole()
          }
        });
      },
      dc_handleClose (event, index) {
        console.log(index);
        this.ajax.get('/place/del_role?rid='+this.dc_user[index].id)
          .then(rsp => {
            if (rsp.data.code === 0){
              this.$Message.success('删除成功');
              this.dc_user.splice(index, 1);
            }
          });
      },
      sm_handleClose (event, index) {
        console.log(index);
        this.ajax.get('/place/del_role?rid='+this.sm_user[index].id)
          .then(rsp => {
            if (rsp.data.code === 0){
              this.$Message.success('删除成功');
              this.sm_user.splice(index, 1);
            }
          });
      },
      ta_handleClose (event, index) {
        console.log(index);
        this.ajax.get('/place/del_role?rid='+this.ta_user[index].id)
          .then(rsp => {
            if (rsp.data.code === 0){
              this.$Message.success('删除成功');
              this.ta_user.splice(index, 1);
            }
          });
      }

    },
    filters: {
      type_name: function(value) {
        const type_name = {
          1: '添加', 0: '删除',
        };
        if (value in type_name) {
          return type_name[value]
        }
        else {
          return value
        }
      },
      store_name: function(value) {
        if (!value) {
          return '-'
        }
        else {
          return value
        }
      },
    },
  }
</script>

<style scoped>

</style>
