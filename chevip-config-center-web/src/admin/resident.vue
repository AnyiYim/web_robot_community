<template>
  <div class="demo-tabs-style1 panel" style="margin: 20px;padding: 30px; width: 90%" >
    <div class="search">
      <Button @click='changePage()' style="border-radius: 4px; font-size:14px; margin-top: 10px; padding: 4px 30px;">
        全部居民
      </Button>
      <Button @click='changePage(14)' style="margin-left: 700px; border-radius: 4px; font-size:14px; margin-top: 10px; padding: 4px 30px; background-color: #f92f47; color: #fff">
        14栋
      </Button>
      <Button @click='changePage(15)' style="border-radius: 4px; font-size:14px; margin-top: 10px; padding: 4px 30px; background-color: #f92f47; color: #fff">
        15栋
      </Button>
      <div class="search-row flex">
      </div>
    </div>
    <div style="margin-top: 30px">
      <div class="guest_list">
        <table border="0" cellspacing="0" cellpadding="0">
          <tr class="table_title">
            <th><div style="width: 128px">地址</div></th>
            <th><div style="width: 108px">门牌号</div></th>
            <th><div style="width: 220px">姓名</div></th>
            <th><div style="width: 120px">绑定用户</div></th>
            <th><div style="width: 100px">性别</div></th>
            <th><div style="width: 150px">联系电话</div></th>
            <th><div style="width: 120px">操作</div></th>
          </tr>
        </table>
      </div>

      <div v-if="resident_data.length > 0" class="guest_list">
        <table border="0" cellspacing='0' cellpadding="0">
          <tr v-for="(item, index) in resident_data" :key="index" style="height:63px; cursor: pointer">
            <td style="margin-left:20px; text-align: center">
              <div style="width: 125px">{{item.building + '栋'}}</div>
            </td>
            <td>
              <div style="width: 105px">{{item.address + '号' }}</div>
            </td>
            <td><div style="width: 220px">{{ item.true_name }}</div></td>
            <td><div style="width: 120px">{{item.user_name}}</div></td>
            <td><div style="width: 100px">{{item.sex && '男' || '女'}}</div></td>
            <td style="text-align: center">
              <div style="width: 150px">{{item.telephone}}</div>
            </td>
            <td><div style="width: 120px">
              <Button @click='role_form.id = item.id; BindModal=true' v-if="!item.user_name" style="border-radius: 4px; font-size:14px; margin-top: 10px; padding: 4px 30px; background-color: #f92f47; color: #fff">
                绑定用户
              </Button>
            </div></td>
          </tr>
        </table>
      </div>
      <div v-else class="guest_list">
        <table border="0" cellspacing="0" cellpadding="0">
          <tr >
            <Card style="margin-top: 5px;text-align: center">
              <div class="flex flex-center">
                <!--<img src="../../public/img/404.png">-->
                <div>无匹配数据</div>
              </div>
            </Card>
          </tr>
        </table>
      </div>
    </div>

    <Modal v-model="BindModal" :mask-closable="false" :scrollable="false" width="380">
      <p slot="header" class="modal-header">
        <span>绑定用户</span>
      </p>
      <div style="padding: 0 10px 0 10px">
        <Form :model="role_form" :label-width="80">
          <FormItem label="添加用户">
            <Select v-model="role_form.uid" filterable remote :remote-method="loadIdMethod" :loading="loading" placeholder="请输入用户名" @on-change="getEmployee">
              <Option v-for="(option, index) in users" :value="option.id" :key="index" :label="option.user_name">
                <div style="display: flex; height: 19px; padding: 2px 0 0 0">
                  <div style="max-width: 150px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;">{{ option.user_name }}</div>
                  <!--<span style="position: absolute; left: 180px; color: rgb(116,116,116); font-size: 12px">{{option.id}}</span>-->
                </div>
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
        // editingId: null,
        // id: null,
        search_text: null,
        searching: false,
        resident_data: {
        },
        users: [],
        role_form: {uid: null, id: null},
        loading: false,
        options: [],
        BindModal: false,
      }
    },
    created: function () {
      this.loadList();
    },
    methods: {
      loadList() {
        this.changePage();
      },
      loadIdMethod (query) {
        if (query && query.length > 1) {
          this.loading = true;
          this.ajax.get('/admin/find_name?name=' + query).then(rsp => {
            if (rsp.data.code === 0){
              this.users = rsp.data.data;
            }
            this.loading = false;
          }, err => {
            this.loading = false;
          });
        }
      },
      submitUserInfo () {
        this.ajax.post('/admin/bind_user', this.role_form).then(response => {
          console.log('绑定用户', response.data.data);
          if (response.data.code === 0) {
            this.$Message.success('绑定成功');
            this.BindModal=false;
            this.role_form = {user_id: null, pid: null, role: ''};
            this.users = [];
            this.changePage()
          }
        });
      },
      changePage(bui='') {
        var params = '';
        if (bui !== '') {
          params = params + 'building=' + bui;
        }
        this.ajax.get('/admin/get_resident?' + params).then(response => {
          if (response.data.code === 0) {
            console.log(response.data.data);
            this.resident_data = response.data.data;
            this.searching = false;
          }
          this.options=[];
          // this.licData=[];
          document.body.scrollTop = 0;
          document.documentElement.scrollTop = 0;
        }).catch(err => {
          this.searching = false;
        });
      },
    },
    filters: {
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
