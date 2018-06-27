<template>
  <div class="demo-tabs-style1 panel" style="margin: 20px;padding: 30px; width: 90%" >
    <div class="search">
      <div class="search-row flex">
        <div class="search-row-item">
          条件：
          <Select style="width: 250px" v-model="id" filterable remote :remote-method="loadIdMethod" :loading="loading" :clearable="true"  placeholder="输入用户名或姓名搜索">
            <Option v-for="(option, index) in options" :value="option.id" :key="index" :label="option.true_name">
              <div style="display: flex; height: 19px; padding: 2px 0 0 0">
                <div style="max-width: 150px;overflow: hidden;text-overflow: ellipsis;white-space: nowrap;">{{option.true_name + '(' + option.user_name + ')'}}</div>
                <span style="position: absolute; left: 180px; color: rgb(116,116,116); font-size: 12px">{{option.id}}</span>
              </div>
            </Option>
          </Select>
        </div>
        <div style="margin-left: 80px">
          日期范围：
          <DatePicker @on-change="loadStoreStatistic" :value="date_range" format="yyyy-MM-dd" type="daterange" placement="bottom-end" placeholder="Select date" style="width: 200px"></DatePicker>
        </div>
      </div>
      <div style="right: 100px; top:0px; height: auto;" class="search-right2 flex ">
        <Button @click="searching=true; changePage(1)"  :loading="searching" style="border-radius: 4px; font-size:14px; margin-top: 10px; padding: 4px 30px; background-color: #f92f47; color: #fff">
          <span v-if="searching">搜索中...</span>
          <span v-else>搜索</span>
        </Button>
      </div>
    </div>
    <div style="margin-top: 30px">
      <div class="guest_list">
        <table border="0" cellspacing="0" cellpadding="0">
          <tr class="table_title">
            <th><div style="width: 178px">修改用户</div></th>
            <th><div style="width: 108px">修改类型</div></th>
            <th><div style="width: 220px">角色</div></th>
            <th><div style="width: 220px">绑定门店</div></th>
            <th><div style="width: 150px">操作者</div></th>
            <th><div style="width: 120px">修改时间</div></th>
          </tr>
        </table>
      </div>

      <div v-if="log_data.length > 0" class="guest_list">
        <table border="0" cellspacing='0' cellpadding="0">
          <tr v-for="(item, index) in log_data" :key="index" style="height:63px; cursor: pointer">
            <td style="margin-left:20px; text-align: center">
              <div style="width: 185px">{{item.u_trueName + ' (' + item.u_userName + ')'}}</div>
            </td>
            <td><div style="width: 95px">
              <span v-if="item.type==0" class="role-status-fag-sub">{{item.type | type_name}}</span>
              <span v-if="item.type==1" class="role-status-fag-add">{{item.type | type_name}}</span>
            </div></td>
            <td><div style="width: 220px">{{ role_dict[item.value] }}</div></td>
            <td><div style="width: 220px">{{item.storeName | store_name}}</div></td>
            <td style="text-align: center">
              <div style="width: 150px">{{item.o_trueName}}</div>
              <div style="width: 150px">{{ item.o_trueName && "(" + item.o_userName + ")"}}</div>
            </td>
            <td><div style="width: 120px">{{item.time}}</div></td>
          </tr>
        </table>
      </div>
      <div v-else class="guest_list">
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
  </div>
</template>

<script>
  export default {
    data () {
      return {
        id: null,
        limit: 10,
        offset: 0,
        start_date: '',
        end_date: '',
        search_text: null,
        searching: false,
        total: null,
        pageSize: 10,
        date_range: [],
        log_data: {
        },
        loading: false,
        options: [],
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
      this.loadList();
    },
    methods: {
      loadList() {
        this.changePage(1);
      },
      loadStoreStatistic (dates) {
        if (dates) {
          if (dates[0] && dates[1]) {
            this.start_time = dates[0];
            this.end_time = dates[1];
            this.date_range[0] = new Date(dates[0]);
            this.date_range[1] = new Date(dates[1]);
          } else {
            this.start_time = this.end_time = '';
          }
        } else {
          this.start_time = this.date_range[0].format('yyyy-MM-dd');
          this.end_time = new Date((this.date_range[1] / 1000 + 86400) * 1000).format('yyyy-MM-dd');
        }
      },
      changePage(page) {
        var params = '';
        params += 'offset=' + (Number(page) - 1) * 10 + '&limit=10';
        if (this.id) params += '&search_text=' + this.id;
        if (this.start_time && this.end_time) params += '&start_date=' + this.start_time + '&end_date=' + this.end_time;
        this.ajax.get('/log/r_search_log?' + params).then(response => {
          if (response.data.code === 0) {
            console.log(response.data.data.log);
            this.total = response.data.data.total;
            this.log_data = response.data.data.log;
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
