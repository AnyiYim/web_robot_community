<template>
  <div class="demo-tabs-style1 panel" style="margin: 20px;padding: 30px; width: 90%" >
    <div class="search">
      <div class="search-row flex">
        <div class="search-row-item">
          条件：
          <Select style="width: 250px" v-model="vid" filterable remote :remote-method="remoteMethod"  :clearable="true" :loading="loading" placeholder="输入车牌搜索">
            <Option v-for="(option, index) in options" :value="option.id" :key="index" :label="option.licenseplace">
              {{option.licenseplace}}
              <span style="margin-left: 50px; color: rgb(116,116,116); font-size: 12px">{{option.id}}</span>
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
            <th><div style="width: 135px">车牌</div></th>
            <th><div style="width: 75px">修改类型</div></th>
            <th><div style="width: 120px">修改属性</div></th>
            <th><div style="width: 150px">旧值</div></th>
            <th><div style="width: 150px">新值</div></th>
            <th><div style="width: 80px">操作者</div></th>
            <th><div style="width: 120px">修改时间</div></th>
          </tr>
        </table>
      </div>

      <div v-if="log_data.length > 0" class="guest_list">
        <table border="0" cellspacing='0' cellpadding="0">
          <tr v-for="(item, index) in log_data" :key="index" style="height:63px; cursor: pointer">
            <td style="text-align: center">
              <div style="width: 135px">{{item.licenseplace}}</div>
              <div style="width: 135px">{{item.vehicle_id}}</div>
            </td>
            <td><div style="width: 75px">{{item.type | type_name}}</div></td>
            <td><div style="width: 120px">{{item.field | file_name}}</div></td>
            <td><div style="width: 150px">{{item.old_value}}</div></td>
            <td><div style="width: 150px">{{item.new_value}}</div></td>
            <td style="text-align: center">
              <div style="width: 80px">{{item.trueName}}</div>
              <div style="width: 80px">{{ item.trueName && "(" + item.userName + ")"}}</div>
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
        vid: null,
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
        licData:[],
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
        if (this.vid) params += '&search_text=' + this.vid;
        if (this.start_time && this.end_time) params += '&start_date=' + this.start_time + '&end_date=' + this.end_time;
        this.ajax.get('/log/search_log?' + params).then(response => {
          if (response.data.code === 0) {
            console.log(response.data.data.log);
            this.total = response.data.data.total;
            this.log_data = response.data.data.log;
            this.searching = false;
          }
          this.options=[];
          this.licData=[];
          document.body.scrollTop = 0;
          document.documentElement.scrollTop = 0;
        }).catch(err => {
          this.searching = false;
        });
      },
      remoteMethod (query) {
        if (query !== '') {
          this.loading = true;
          if (query.length > 2) {
            this.ajax.get('/vehicle/find_license?licenseplace=' + query)
              .then(rsp => {
                if (rsp.data.code === 0){
                  console.log(rsp.data.data);
                  this.licData = rsp.data.data;
                }
              });
          }
          setTimeout(() => {
            this.loading = false;
            const list = this.licData.map(item => {
              return {
                id: item.id,
                licenseplace: item.licenseplace
              };
            });
            this.options = list.filter(item => item.licenseplace.indexOf(query) > -1);
          }, 200);
        } else {
          this.vid = null;
          this.options = [];
          this.licData = [];
        }
      },
    },
    filters: {
      type_name: function(value) {
        const type_name = {
          'auction': '车辆拍卖信息', 'vehicle': '车辆基本信息',
          'transfer': '车辆过户信息', 'procedure': '车辆手续信息',
        };
        if (value in type_name) {
          return type_name[value]
        }
        else {
          return value
        }
      },
      file_name: function (value) {
        const type_name = {
          'vin': 'Vin码', 'brand': '品牌', 'series': '车系', 'model': '车型', 'getlicence_date': '上牌日期',
          'displacement': '排量', 'mileage': '表显示里程', 'engineno': '发动机号', 'cartype': '车辆类型',
          'color': '车辆颜色', 'gearbox': '变速箱类型', 'is_vin_complete': '车架号是否完整', 'usage': '使用性质',
          'criterion': '环保类型', 'factory_date': '出厂日期', 'seat_count': '座位数', 'vehicle_type': '车辆类别',
          'origin_price': '原车价格', 'owner_type': '所有人性质', 'supplementary': '补充信息', 'bconfiguration': '车况描述',
          'is_engineno_complete': '发动机号是否完整',

          'valuer_id': '发起人id', 'store_id': '门店id', 'licenseplace': '车牌',

          "auction_type": '拍卖方式', "balance_contract_price": '合同价', "balance_counttype": '结算方式',
          "balance_pay_for_client": '车付款第三方', "balance_payee_id": '付款人id', "bundling_vehicle": "是否打包车",
          "client_name": "委托人姓名", "client_phone": "委托人手机", "end_time": "结束时间",
          "fee0": '手续费', "fee1": '场地费', "fee2": '综合服务费', "fee3": '违章罚款', "fee4": '其他费用', "fee5": '评估费',
          "feename4": "其他费用名称", "feetype0": '手续费类型', "feetype1": '场地费类型', "feetype2": '综合服务费类型',
          "feetype3": '违章罚款类型', "feetype4": '其他费用类型', "feetype5": '评估费类型',
          "other_req": "其他要求", "pay_req": "付款要求", "reserve_price": '车主保留价', "sale_type": "销售方法",
          "start_time": "拍卖时间", "starting_price": '起拍价', "transfer_req": "过户要求",

          "annual_ticket_vld": "年票有效期", "annual_verification_info": "年审说明", "annual_verification_vld": "年审有效期",
          "come_insurance_vld": "交通险有效期", "commercial_insurance_price": "商业险金额",
          "commercial_insurance_vld": "商业险有效期", "endorsement": "违章事故", "endorsement_info": "违章说明",
          "invoice": "原始购车发票", "maintenance_log": "保养记录", "maintenance_procedure": "保养手续",
          "manual": "说明书", "modification_info": "改装说明", "registration": "登记证",
          "vehicle_and_vessel_tax_vld": "车船税有效期", "vehicle_license": "行驶证", "vehicle_warranty": "新车质保",

          "be_put_in_time": "车辆预计入库时间", "look_addr": "看车地址", "look_contract": "看车联系人", "look_tel": "看车电话",
          "old_owner": "旧车主", "old_owner_tel": "旧车主电话", "old_owner_type": "旧车主类型", "purchase_tax": "购置税",
          "salename": "业务员", "salephone": "业务员电话", "transfer_about": "过户相关", "transfer_addr": "过户地点",
          "transfer_info": "过户说明", "transfer_time": "过户时间", "vehicle_addr": "车辆地址",
          "vehicle_addr_cityid": "车辆地址(城市)", "vehicle_addr_provinceid": "车辆地址(省份)"
        };
        if (value in type_name) {
          return type_name[value]
        }
        else {
          return value
        }
      }
    },
  }
</script>

<style scoped>

</style>
