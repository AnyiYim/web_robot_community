<template>
  <div class="car-info-modal flex flex-v">
    <div class="car-info">
      <div class="editCarForm">
        <Form ref="id" label-position="right" :label-width="120" inline>
          <Form-item  label="请输入车牌：">
            <div class="flex">
              <Select style="width: 250px" v-model="id" filterable remote :remote-method="remoteMethod" :loading="loading" placeholder="输入车牌搜索" @on-change="getLicense">
                <Option v-for="(option, index) in options" :value="option.id" :key="index" :label="option.licenseplace">
                  {{option.licenseplace}}
                  <span style="margin-left: 50px; color: rgb(116,116,116); font-size: 12px">{{option.id}}</span>
                </Option>
              </Select>
            </div>
          </Form-item>
        </Form>
        <div style="width: 1190px; display: flex">
          <Card style="width: 100%">
            <div class="info-title">
              <div class="circle" style="background-color: #2d8cf0"></div>
            </div>
            <p style="margin-left: 15px" slot="title">车辆基本信息 {{ vehicle.licenseplace && ': ' + vehicle.licenseplace}}</p>
            <span v-if="vehicle.sub_status" class="v-status-fag">{{vehicle.sub_status|get_status}}</span>
            <div v-if="vehicle.licenseplace" style="position: absolute; left: 550px; top:8px">
             <Button type="primary" style="margin-left: 13px; margin-top: 1px" @click="lic_modal=true">修改车牌</Button>
            </div>
            <div >
              <table v-if="vehicle.id" style="width: 550px" class="transform-table">
              <tr>
                <td>
                  <div style="width: 215px;white-space: nowrap">id：{{vehicle.id}}</div>
                </td>
                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">Vin码：
                    <Input v-if="vflag.vin" type="text" style="width: 180px" v-model="vehicle.vin"></Input>
                    <span v-else>{{vehicle.vin}}</span>
                    <i @click="change_v('vin')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">品牌：
                    <Input v-if="vflag.brand" type="text" style="width: 180px" v-model="vehicle.brand"></Input>
                    <span v-else>{{vehicle.brand}}</span>
                    <i @click="change_v('brand')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>
                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">车系：
                    <Input v-if="vflag.series" type="text" style="width: 189px" v-model="vehicle.series"></Input>
                    <span v-else>{{vehicle.series}}</span>
                    <i @click="change_v('series')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>
              </tr>
              <tr>
                <td colspan="2" class="card-v">
                  <div style=" width: 600px">
                    <div style="float: left">车型：</div>
                    <Input v-if="vflag.model" type="textarea" :rows="2" style="width: 502px" v-model="vehicle.model"></Input>
                    <div v-else style="width: 450px; float: left">{{vehicle.model}}</div>
                    <i @click="change_v('model')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>
              </tr>
              <tr style="margin-top: 38px">
                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">上牌日期：
                    <Input v-if="vflag.getlicence_date" type="text" style="width: 150px" v-model="vehicle.getlicence_date"></Input>
                    <span v-else>{{vehicle.getlicence_date}}</span>
                    <i @click="change_v('getlicence_date')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>
                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">排量：
                    <a v-if="vflag.displacement">
                      <Input type="text" style="width: 165px" v-model="vehicle.displacement"></Input>
                      <span style="color: #6e6e6e;">升</span>
                    </a>
                    <span v-else>{{vehicle.displacement ? vehicle.displacement + '升' : ''}}</span>
                    <i @click="change_v('displacement')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>
              </tr>

              <tr>
                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">表显示里程：
                    <a v-if="vflag.mileage">
                      <Input type="text" style="width: 80px" v-model="vehicle.mileage"></Input>
                      <span style="color: #6e6e6e;">万公里</span>
                    </a>
                    <span v-else>{{vehicle.mileage ? vehicle.mileage + '万公里' : ''}}</span>
                    <i @click="change_v('mileage')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>

                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">发动机号：
                    <Input v-if="vflag.engineno" type="text" style="width: 157px" v-model="vehicle.engineno"></Input>
                    <span v-else>{{vehicle.engineno}}</span>
                    <i @click="change_v('engineno')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>

              </tr>
              <tr>
                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">车辆类型：
                    <Input v-if="vflag.cartype" type="text" style="width: 150px" v-model="vehicle.cartype"></Input>
                    <span v-else>{{vehicle.cartype}}</span>
                    <i @click="change_v('cartype')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>
                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">车辆颜色：
                    <Input v-if="vflag.color" type="text" style="width: 157px" v-model="vehicle.color"></Input>
                    <span v-else>{{vehicle.color}}</span>
                    <i @click="change_v('color')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">变速箱类型：
                    <Input v-if="vflag.gearbox" type="text" style="width: 133px" v-model="vehicle.gearbox"></Input>
                    <span v-else>{{vehicle.gearbox}}</span>
                    <i @click="change_v('gearbox')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>
                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">车架号是否完整：
                    <Radio-group v-if="vflag.is_vin_complete" style="width: 110px" v-model="vehicle.is_vin_complete">
                      <Radio label="1"><span>是</span></Radio>
                      <Radio label="0"><span>否</span></Radio>
                    </Radio-group>
                    <span v-else>{{vehicle.is_vin_complete ? '是' : '否'}}</span>
                    <i @click="change_v('is_vin_complete')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>

              </tr>
              <tr>
                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">发动机号是否完整：
                    <Radio-group v-if="vflag.is_engineno_complete" style="width: 80px" v-model="vehicle.is_engineno_complete">
                      <Radio label="1"><span>是</span></Radio>
                      <Radio label="0"><span>否</span></Radio>
                    </Radio-group>
                    <!--<Input v-if="vflag.brand" type="text" style="width: 150px" v-model="vehicle.brand"></Input>-->
                    <span v-else>{{vehicle.is_engineno_complete ? '是' : '否'}}</span>
                    <i @click="change_v('is_engineno_complete')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>
                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">使用性质：
                    <Input v-if="vflag.usage" type="text" style="width: 157px" v-model="vehicle.usage"></Input>
                    <span v-else>{{vehicle.usage}}</span>
                    <i @click="change_v('usage')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">环保类型：
                    <Input v-if="vflag.criterion" type="text" style="width: 150px" v-model="vehicle.criterion"></Input>
                    <span v-else>{{vehicle.criterion}}</span>
                    <i @click="change_v('criterion')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>
                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">出厂日期：
                    <Input v-if="vflag.factory_date" type="text" style="width: 157px" v-model="vehicle.factory_date"></Input>
                    <span v-else>{{vehicle.factory_date}}</span>
                    <i @click="change_v('factory_date')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">座位数：
                    <a v-if="vflag.seat_count">
                      <Input type="text" style="width: 142px" v-model="vehicle.seat_count"></Input>
                      <span style="color: #6e6e6e;">个</span>
                    </a>
                    <span v-else>{{vehicle.seat_count ? vehicle.seat_count + '个' : ''}}</span>
                    <i @click="change_v('seat_count')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>
                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">车辆类别：
                    <Input v-if="vflag.vehicle_type" type="text" style="width: 157px" v-model="vehicle.vehicle_type"></Input>
                    <span v-else>{{vehicle.vehicle_type}}</span>
                    <i @click="change_v('vehicle_type')" style="margin-left: 10px" class="i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>
              </tr>
              <tr>
                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">原车价格：
                    <a v-if="vflag.origin_price">
                      <Input type="text" style="width: 110px" v-model="vehicle.origin_price"></Input>
                      <span style="color: #6e6e6e;">万元</span>
                    </a>
                    <span v-else>{{vehicle.origin_price ? vehicle.origin_price + '万元' : ''}}</span>
                    <i @click="change_v('origin_price')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>
                <td class="card-v">
                  <div style=" width: 215px;white-space: nowrap;">所有人性质：
                    <Input v-if="vflag.owner_type" type="text" style="width: 140px" v-model="vehicle.owner_type"></Input>
                    <span v-else>{{vehicle.owner_type}}</span>
                    <i @click="change_v('owner_type')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>
              </tr>
              <tr>
                <td colspan="2" class="card-v">
                  <div style=" width: 600px">
                    <div style="float: left">补充信息：</div>
                    <Input v-if="vflag.supplementary" type="textarea" :rows="2" style="width: 470px" v-model="vehicle.supplementary"></Input>
                    <div v-else style="width: 410px; float: left">{{vehicle.supplementary}}</div>
                    <i @click="change_v('supplementary')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>

              </tr>
              <tr>
                <td colspan="2" class="card-v">
                  <div style=" width: 600px">
                    <div style="float: left">车况描述：</div>
                    <Input v-if="vflag.bconfiguration" type="textarea" :rows="2" style="width: 470px" v-model="vehicle.bconfiguration"></Input>
                    <div v-else style="width: 410px; float: left">{{vehicle.bconfiguration}}</div>
                    <i @click="change_v('bconfiguration')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                  </div>
                </td>
              </tr>
              </table>
              <div v-else><p>暂无车辆信息</p></div>
            </div>
          </Card>
          <div v-if="vehicle.id" style="margin-left: 20px;">
            <Card style="width: 511px">
              <div class="info-title">
                <div class="circle" style="background-color: #2d8cf0"></div>
              </div>
              <p style="margin-left: 15px" slot="title">评估师</p>
              <div v-if="vehicle.valuer_id" style="position: absolute; left: 395px; top:8px">
                <Button v-if="!v_edit" type="primary" style="margin-left: 13px; margin-top: 1px" @click="v_edit=true">修改评估师</Button>
                <Button v-if="v_edit" style="margin-left: 13px; margin-top: 1px" @click="v_edit=false">取消修改</Button>
              </div>
              <div v-if="!v_edit">
                <div style="margin-left: 57px; margin-bottom: 30px; margin-top: 20px">
                  <span style="font-size: 14px">评估师:</span>
                  <span style="font-size: 14px; margin-left:8px">
                    {{vehicle.valuer_name}}({{ vehicle.valuer_user_name }})
                  </span>
                </div>
              </div>

              <div v-if="v_edit">
                <div style="margin-left: 57px"><span style="font-size: 14px">评估师:</span>
                  <span style="font-size: 14px; margin-left:8px">
                    {{vehicle.valuer_name}}({{ vehicle.valuer_user_name }})
                  </span>
                </div>
                <div style="margin-left: 40px;margin-bottom: 40px; margin-top: 20px ">
                  <span style="font-size: 14px; float: left; margin-top: 6px">修改评估师:</span>
                  <Select style="width: 250px; margin-left: 15px" v-model="change_valuer" filterable remote :remote-method="valuerMethod" :loading="loading" placeholder="输入姓名/账号">
                    <Option v-for="(option, index) in users" :value="option.id" :key="index" :label="option.trueName + '(' + option.userName + ')'">
                    </Option>
                  </Select>

                  <!--<Input style="margin-left:8px; float: left; width: 250px" v-model="change_valuer"></Input>-->
                </div>
                <div style="margin-top: 40px">
                  <Button type="primary" size="large" long :loading="valuer_loading" @click="valuer_change">修改</Button>
                </div>
              </div>
            </Card>

            <Card style="margin-top: 20px;width: 511px">
              <div class="info-title">
                <div class="circle" style="background-color: #2d8cf0"></div>
              </div>
              <p style="margin-left: 15px" slot="title">门店信息</p>
              <div v-if="vehicle.store_id" style="position: absolute; left: 395px; top:8px">
                <Button v-if="!s_edit" type="primary" style="margin-left: 13px; margin-top: 1px" @click="try_s_edit">修改门店</Button>
                <Button v-if="s_edit" style="margin-left: 13px; margin-top: 1px" @click="s_edit=false">取消修改</Button>
              </div>
              <div v-if="!s_edit">
                <div style="margin-left: 57px;"><span style="font-size: 14px">门店id:</span><span style="font-size: 14px; margin-left:8px"> {{vehicle.store_id}}</span></div>
                <div style="margin-left: 57px; margin-bottom: 30px; margin-top: 20px"><span style="font-size: 14px">门店名称:</span><span style="font-size: 14px; margin-left:8px"> {{vehicle.store_name}}</span></div>
              </div>

              <div v-if="s_edit">
                <div style="margin-left: 37px"><span style="font-size: 14px">现门店:</span><span style="font-size: 14px; margin-left:8px"> {{vehicle.store_name}}</span></div>
                <div style="margin-left: 20px;margin-bottom: 40px; margin-top: 20px ">
                  <span style="font-size: 14px; float: left; margin-top: 6px">修改门店:</span>

                  <Select style="margin-left:10px; width: 320px;" v-model="change_store" filterable>
                    <Option v-for="item in storeList" :value="item.id" :key="item.value" :label="item.store_name">
                      <span style="font-size: 13px">{{ item.store_name }}({{ item.user_name }})</span>
                    </Option>
                  </Select>
                  <!--<Input style="margin-left:8px; float: left; width: 250px" v-model="change_store"></Input>-->
                </div>
                <div style="margin-top: 40px">
                  <Button type="primary" size="large" long :loading="store_loading" @click="store_change">修改</Button>
                </div>
              </div>
            </Card>


            <Card style="margin-top: 20px;width: 511px">
              <div class="info-title">
                <div class="circle" style="background-color: #2d8cf0"></div>
              </div>
              <p style="margin-left: 15px" slot="title">结算信息</p>
              <div v-if="has_auction">
                <table class="transform-table">
                  <tr>
                    <td colspan="2" class="card-v">
                      <div style=" width: 505px;white-space: nowrap;">
                        <span style="float: left">结算方式：</span>
                        <div style="float: left; margin-top: -8px" v-if="aflag.balance_counttype">
                          <Select size="large" style="width:160px" v-model="auction.balance_counttype">
                            <Option v-for="item in auctionBFormOption" :value="item.value" :key="item.value">{{ item.label }}</Option>
                          </Select>
                          <span style="margin-left: 10px" v-if="auction.balance_counttype === 5">
                            <span class="red need">*</span>合同价：
                            <Input class="no-border" style="width: 90px; padding: 0 0 0 0" v-model="auction.balance_contract_price" size="large" placeholder=""></Input>
                            <span style="position: absolute; left: 418px; top: 7px; color: #666666">元</span>
                          </span>
                        </div>
                        <div style="float: left" v-if="!aflag.balance_counttype">
                          <span style="float: left">
                            {{auction.balance_counttype === 4 ? '付成交价+分润': (auction.balance_counttype === 5 ? '付合同价+分润' : '付成交价(0分润)')}}
                          </span>
                          <span v-if="auction.balance_counttype === 5" style="float: left; margin-left: 45px">
                            合同价：{{auction.balance_contract_price && auction.balance_contract_price + '元'}}
                          </span>
                        </div>
                        <i @click="change_a('balance_counttype')" style="float:left; margin-top: 3px;margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                      </div>
                    </td>
                  </tr>
                  <tr>
                    <td class="card-v">
                      <div style=" width: 215px;white-space: nowrap;">车款付第三方：
                        <Radio-group v-if="aflag.balance_pay_for_client" v-model="auction.balance_pay_for_client">
                          <Radio :label="1"><span>是</span></Radio>
                          <Radio :label="0"><span>否</span></Radio>
                        </Radio-group>
                        <span v-else>
                          {{auction.balance_pay_for_client === 1 ? '是': '否'}}
                        </span>
                        <i @click="change_a('balance_pay_for_client')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                      </div>
                    </td>
                  </tr>
                  <tr>
                    <td class="card-v">
                      <div style=" width: 215px;white-space: nowrap;">收款账号：
                        <Select v-if="aflag.balance_payee_id" style="width: 320px; margin-left: 15px" v-model="auction.balance_payee_id" filterable remote :remote-method="payeeMethod" :loading="loading" placeholder="输入身份证或银行卡号查询" :label="auction.balance_payee_bankAccount">
                          <Option v-for="(option, index) in payees" :value="option.id" :key="index" :label="option.accountName + ' ' + option.bankAccount">
                            <div style="padding: 4px">
                              <div class="">
                                 {{ option.accountName }}
                                 <span style="color: rgb(116,116,116);">{{ option.idCard }}</span>
                              </div>
                              <div class="">
                                卡号：{{ option.bankAccount }}
                              </div>
                              <div class="">
                                开户行：{{ option.bankName }}
                              </div>
                            </div>
                          </Option>
                        </Select>
                        <span v-else>
                          {{auction.balance_payee_bankAccount}}
                        </span>
                        <i @click="change_a('balance_payee_id')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                      </div>
                    </td>
                  </tr>
                </table>
              </div>

              <div v-else>
               <p>暂无结算信息</p>
              </div>
            </Card>
          </div>
        </div>
        <div>
          <Card style="width: 1190px; margin-top: 20px">
            <div class="info-title">
              <div class="circle" style="background-color: #2d8cf0"></div>
            </div>
            <p style="margin-left: 15px" slot="title">拍卖基本信息</p>
            <div v-if="has_auction">
              <table class="transform-table">
                <tr>
                  <td colspan="2" class="card-v">
                    <div style=" width: 215px;white-space: nowrap;">销售方法：
                      <Select v-if="aflag.sale_type" v-model="auction.sale_type" size="large" style="width:320px">
                        <Option v-for="item in auctionFormOption" :value="item.name" :key="item.name">{{ item.name }}</Option>
                      </Select>
                      <span style="margin-left: 10px" v-if="aflag.sale_type && auction.sale_type === '自定义'"><Input style="width: 153px" v-model="sale_type_input" size="large" placeholder="请选择销售方式"></Input></span>
                      <span v-if="!aflag.sale_type">
                         {{auction.sale_type}}
                      </span>
                      <i @click="change_a('sale_type')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">拍卖方式：
                      <Radio-group v-if="aflag.auction_type" style="width: 189px" v-model="auction.auction_type">
                        <Radio label="1"><span>竞价</span></Radio>
                        <Radio label="3"><span>一口价</span></Radio><br>
                        <Radio label="2"><span>竞标</span></Radio>
                        <Radio label="4" v-if="auction.can_resale"><span>好车直卖</span></Radio>
                      </Radio-group>
                      <span v-else>{{ {1:'竞价',2:'竞标',3:'一口价',4:'好车直卖'}[auction.auction_type] }}</span>
                      <i @click="change_a('auction_type')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">拍卖时间：
                      <Input v-if="aflag.start_time" type="text" style="width: 189px" v-model="auction.start_time"></Input>
                      <span v-else>{{auction.start_time}}</span>
                      <i @click="change_a('start_time')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">结束时间：
                      <Input v-if="aflag.end_time" type="text" style="width: 189px" v-model="auction.end_time"></Input>
                      <span v-else>{{auction.end_time}}</span>
                      <i @click="change_a('end_time')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">是否打包车：
                      <Checkbox v-if="aflag.bundling_vehicle" style="margin-top: 1px;" v-model="isPackCar">是</Checkbox>
                      <span v-if="aflag.bundling_vehicle && isPackCar">
                        <Input style="width: 160px" v-model="auction.bundling_vehicle" size="large" placeholder="请输入需要绑定的车牌"></Input>
                      </span>
                      <span v-else>{{auction.bundling_vehicle || '否'}}</span>
                      <i @click="change_a('bundling_vehicle')" style="margin-left: 0px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">委托人姓名：
                      <Input v-if="aflag.client_name" type="text" style="width: 170px" v-model="auction.client_name"></Input>
                      <span v-else>{{auction.client_name}}</span>
                      <i @click="change_a('client_name')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">委托人手机：
                      <Input v-if="aflag.client_phone" type="text" style="width: 170px" v-model="auction.client_phone"></Input>
                      <span v-else>{{auction.client_phone}}</span>
                      <i @click="change_a('client_phone')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">车主保留价：
                      <Input v-if="aflag.reserve_price" type="text" style="width: 153px" v-model="auction.reserve_price"></Input>
                      <span v-if="aflag.reserve_price">元</span>
                      <span v-else>{{auction.reserve_price && auction.reserve_price +  "元"}}</span>
                      <i @click="change_a('reserve_price')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">起拍价：
                      <Input v-if="aflag.starting_price" type="text" style="width: 178px" v-model="auction.starting_price"></Input>
                      <span v-if="aflag.starting_price">元</span>
                      <span v-else>{{auction.starting_price && auction.starting_price + "元"}}</span>
                      <i @click="change_a('starting_price')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>

                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">手续费：
                      <Select v-if="aflag.fee0" v-model="auction.feetype0" size="large" style="width:100px">
                        <Option v-for="item in feetype" :value="item.value" :key="item.value">{{ item.label }}</Option>
                      </Select>
                      <span v-if="aflag.fee0" style="margin-left: 10px">
                        <Input class="no-border" style="width: 80px" v-model="auction.fee0" size="large" placeholder="" @on-keyup="validateNumber"></Input>
                        <span class="yuan2">{{ {'1':'元','2':'%'}[auction.feetype0] }}</span>
                      </span>

                      <span v-else>{{auction.feetype0 === '1' ? auction.fee0 && auction.fee0 + '元' : auction.fee0 && auction.fee0 + '%'}}</span>
                      <i @click="change_a('fee0')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">场地费：
                      <span v-if="aflag.fee1" style="margin-left: 10px">
                        <Input class="no-border" style="width: 80px" v-model="auction.fee1" size="large" placeholder="" @on-keyup="validateNumber"></Input>
                        <span class="yuan2">{{ {'1':'元','2':'%'}[auction.feetype0] }}</span>
                      </span>
                      <span v-else>{{auction.feetype1 === '1' ? auction.fee1 && auction.fee1 + '元' : auction.fee1 && auction.fee1 + '%'}}</span>
                      <i @click="change_a('fee1')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">综合服务费：
                      <Select v-if="aflag.fee2" v-model="auction.feetype2" size="large" style="width:100px">
                        <Option v-for="item in feetype" :value="item.value" :key="item.value">{{ item.label }}</Option>
                      </Select>
                      <span v-if="aflag.fee2" style="margin-left: 10px">
                        <Input class="no-border" style="width: 50px" v-model="auction.fee2" size="large" placeholder="" @on-keyup="validateNumber"></Input>
                        <span class="yuan2">{{ {'1':'元','2':'%'}[auction.feetype2] }}</span>
                      </span>
                      <span v-else>{{auction.feetype2 === '1' ? auction.fee2 && auction.fee2 + '元' : auction.fee2 && auction.fee2 + '%'}}</span>
                      <i @click="change_a('fee2')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">违章罚款：
                      <span v-if="aflag.fee3" style="margin-left: 10px">
                        <Input class="no-border" style="width: 80px" v-model="auction.fee3" size="large" placeholder="" @on-keyup="validateNumber"></Input>
                        <span class="yuan2">{{ {'1':'元','2':'%'}[auction.feetype0] }}</span>
                      </span>
                      <span v-else>{{auction.feetype3 === '1' ? auction.fee3 && auction.fee3 + '元' : auction.fee3 && auction.fee3 + '%'}}</span>
                      <i @click="change_a('fee3')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="card-v">
                    <div style="width: 330px;white-space: nowrap;">评估费：
                      <Select v-if="aflag.fee5" v-model="auction.feetype5" size="large" style="width:100px">
                        <Option v-for="item in feetype" :value="item.value" :key="item.value">{{ item.label }}</Option>
                      </Select>
                      <span v-if="aflag.fee5" style="margin-left: 10px">
                        <Input class="no-border" style="width: 50px" v-model="auction.fee5" size="large" placeholder="" @on-keyup="validateNumber"></Input>
                        <span class="yuan2">{{ {'1':'元','2':'%'}[auction.feetype2] }}</span>
                      </span>
                      <span v-else>{{auction.feetype5 === '1' ? auction.fee5 && auction.fee5 + '元' : auction.fee5 && auction.fee5 + '%'}}</span>
                      <i @click="change_a('fee5')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v" colspan="2">
                    <div style="width: 380px;white-space: nowrap;">其他费用：
                      <Select v-if="aflag.fee4" v-model="auction.feetype4" size="large" style="width:100px">
                        <Option v-for="item in feetype" :value="item.value" :key="item.value">{{ item.label }}</Option>
                      </Select>
                      <span v-if="aflag.fee4" style="margin-left: 10px"><Input class="no-border" style="width: 80px" v-model="auction.feename4" size="large" placeholder="费用名"></Input></span>
                      <span v-if="aflag.fee4" style="margin-left: 10px">
                        <Input class="no-border" style="width: 90px" v-model="auction.fee4" size="large" placeholder="" @on-keyup="validateNumber"></Input>
                        <span class="yuan2">{{ {'1':'元','2':'%'}[auction.feetype4] }}</span>
                      </span>
                      <span v-else>{{auction.feetype4 === '1' ? auction.fee4 && auction.fee4 + '元' : auction.fee4 && auction.fee4 + '%'}}</span>
                      <i @click="change_a('fee4')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="card-v">
                    <div style="width: 330px;white-space: nowrap;">付款需求：
                      <Select v-if="aflag.pay_req" v-model="auction.pay_req" size="large" style="width:90px">
                        <Option v-for="item in payRequestOption" :value="item.value" :key="item.value">{{ item.label }}</Option>
                      </Select>
                      <span style="margin-left: 10px" v-if="aflag.pay_req && auction.pay_req === '自定义'"><Input style="width:63px" v-model="payRequestInput" size="large" placeholder=""></Input></span>
                      <span v-if="aflag.pay_req" class="content">内付款</span>
                      <span v-if="!aflag.pay_req">{{auction.pay_req && auction.pay_req + '内付款' }}</span>
                      <i @click="change_a('pay_req')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 330px;white-space: nowrap;">过户要求：
                      <Select v-if="aflag.transfer_req" v-model="auction.transfer_req" size="large" style="width:100px">
                        <Option v-for="item in transRequestOption" :value="item.value" :key="item.value">{{ item.label }}</Option>
                      </Select>
                      <span style="margin-left: 10px" v-if="aflag.transfer_req && auction.transfer_req === '自定义'"><Input style="width: 73px" v-model="transRequestInput" size="large" placeholder=""></Input></span>
                      <span v-if="aflag.transfer_req" class="content">内过户</span>
                      <span v-if="!aflag.transfer_req">{{auction.transfer_req && auction.transfer_req + '内过户' }}</span>
                      <i @click="change_a('transfer_req')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 330px;white-space: nowrap;">其他要求：
                      <Input v-if="aflag.other_req" style="width: 188px" v-model="auction.other_req" size="large" placeholder=""></Input>
                      <span v-else>{{ auction.other_req }}</span>
                      <i @click="change_a('other_req')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
              </table>
            </div>
            <div v-else>
              <p>暂无拍卖信息</p>
            </div>
          </Card>
        </div>
        <div style="width: 1190px; margin-top: 20px; display: flex">

          <Card style="width: 100%">
            <div class="info-title">
              <div class="circle" style="background-color: #2d8cf0"></div>
            </div>
            <p style="margin-left: 15px" slot="title">手续基本信息</p>
            <div >
              <table v-if="vehicle.id" style="width: 615px" class="transform-table">
                <tr>
                  <td class="card-v">
                    <div style="width: 215px;white-space: nowrap;">年审有效期：
                      <Input v-if="pflag.annual_verification_vld" type="text" style="width: 124px" v-model="procedureForm.annual_verification_vld"></Input>
                      <span v-else>{{procedureForm.annual_verification_vld}}</span>
                      <i @click="change_p('annual_verification_vld')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 215px;white-space: nowrap;">交强险有效期：
                      <Input v-if="pflag.come_insurance_vld" type="text" style="width: 124px" v-model="procedureForm.come_insurance_vld"></Input>
                      <span v-else>{{procedureForm.come_insurance_vld}}</span>
                      <i @click="change_p('come_insurance_vld')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="card-v">
                    <div style="width: 215px;white-space: nowrap;">商业险有效期：
                      <Input v-if="pflag.commercial_insurance_vld" type="text" style="width: 124px" v-model="procedureForm.commercial_insurance_vld"></Input>
                      <span v-else>{{procedureForm.commercial_insurance_vld}}</span>
                      <i @click="change_p('commercial_insurance_vld')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 215px;white-space: nowrap;">年票有效期：
                      <Input v-if="pflag.annual_ticket_vld" type="text" style="width: 124px" v-model="procedureForm.annual_ticket_vld"></Input>
                      <span v-else>{{procedureForm.annual_ticket_vld}}</span>
                      <i @click="change_p('annual_ticket_vld')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="card-v">
                    <div style="width: 215px;white-space: nowrap;">车船税有效期：
                      <Input v-if="pflag.vehicle_and_vessel_tax_vld" type="text" style="width: 124px" v-model="procedureForm.vehicle_and_vessel_tax_vld"></Input>
                      <span v-else>{{procedureForm.vehicle_and_vessel_tax_vld}}</span>
                      <i @click="change_p('vehicle_and_vessel_tax_vld')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 215px;white-space: nowrap;">违章单数：
                      <Select v-if="pflag.endorsement"  style="width: 180px" v-model="procedureForm.endorsement" size="large">
                        <Option value="0">0单</Option>
                        <Option value="1">1单</Option>
                        <Option value="2">2单</Option>
                        <Option value="3">3单</Option>
                        <Option value="4">4单</Option>
                        <Option value="5">5单</Option>
                        <Option value="6">5单以上</Option>
                      </Select>
                      <span v-else>{{procedureForm.endorsement}}</span>
                      <i @click="change_p('endorsement')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="card-v">
                    <div style="width: 215px;white-space: nowrap;">商业险金额：
                      <Input v-if="pflag.commercial_insurance_price" type="text" style="width: 124px" v-model="procedureForm.commercial_insurance_price"></Input>
                      <span v-else>{{procedureForm.commercial_insurance_price && procedureForm.commercial_insurance_price + '元'}}</span>
                      <i @click="change_p('commercial_insurance_price')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 215px;white-space: nowrap;">保养手续：
                      <Input v-if="pflag.maintenance_procedure" type="text" style="width: 124px" v-model="procedureForm.maintenance_procedure"></Input>
                      <span v-else>{{procedureForm.maintenance_procedure && procedureForm.maintenance_procedure + '元'}}</span>
                      <i @click="change_p('maintenance_procedure')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td colspan="2" class="card-v">
                    <div style="white-space: nowrap;">年审说明：
                      <Select v-if="pflag.annual_verification_info" v-model="procedureForm.annual_verification_info" size="large">
                        <Option value="年审在有效期内"></Option>
                        <Option value="年审已过期，过户前需年审，年审及其费用由买家负责"></Option>
                        <Option value="年审已过期，过户前需年审，年审及其费用由卖家负责"></Option>
                        <Option value="年审已过期，过户前需年审，年审由过户部代为办理"></Option>
                        <Option value="年审可能已过期，过户如需年审，年审及其费用由买家负责"></Option>
                        <Option value="年审可能已过期，过户如需年审，年审及其费用由卖家负责"></Option>
                      </Select>
                      <span v-else>{{procedureForm.annual_verification_info}}</span>
                      <i @click="change_p('annual_verification_info')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td colspan="2" class="card-v">
                    <div style="white-space: nowrap;">违章说明：
                      <Select v-if="pflag.endorsement_info"  v-model="procedureForm.endorsement_info" size="large" @on-change="procedureForm.endorsement_info = procedureForm.endorsement_info">
                        <Option v-for="item in endorsement_list" :value="item.name" :key="item.value">{{ item.name }}</Option>
                      </Select>
                      <span v-else>{{procedureForm.endorsement_info}}</span>
                      <i @click="change_p('endorsement_info')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td colspan="2" class="card-v">
                    <div style="white-space: nowrap;">改装说明：
                      <Select v-if="pflag.modification_info" @on-change="procedureForm.modification_info = procedureForm.modification_info"  v-model="procedureForm.modification_info" size="large">
                        <Option v-for="item in modification_list" :value="item.name" :key="item.value">{{ item.name }}</Option>
                      </Select>
                      <span v-else>{{procedureForm.modification_info}}</span>
                      <i @click="change_p('modification_info')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="card-v">
                    <div style="width: 215px;white-space: nowrap;">维修保养记录：
                      <Radio-group v-if="pflag.maintenance_log"  v-model="procedureForm.maintenance_log">
                        <Radio label="有"><span>有</span></Radio>
                        <Radio label="无"><span>无</span></Radio>
                      </Radio-group>
                      <span v-else>{{procedureForm.maintenance_log}}</span>
                      <i @click="change_p('maintenance_log')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 215px;white-space: nowrap;">新车质保：
                      <Radio-group v-if="pflag.vehicle_warranty" style="width: 100px" v-model="procedureForm.vehicle_warranty">
                        <Radio label="有"><span>有</span></Radio>
                        <Radio label="无"><span>无</span></Radio>
                      </Radio-group>
                      <span v-else>{{procedureForm.vehicle_warranty}}</span>
                      <i @click="change_p('vehicle_warranty')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="card-v">
                    <div style="width: 215px;white-space: nowrap;">行驶证：
                      <Radio-group v-if="pflag.vehicle_license" style="width: 100px" v-model="procedureForm.vehicle_license">
                        <Radio label="有"><span>有</span></Radio>
                        <Radio label="无"><span>无</span></Radio>
                      </Radio-group>
                      <span v-else>{{procedureForm.vehicle_license}}</span>
                      <i @click="change_p('vehicle_license')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 210px;white-space: nowrap;">登记证：
                      <Radio-group v-if="pflag.registration" style="width: 100px" v-model="procedureForm.registration">
                        <Radio label="有"><span>有</span></Radio>
                        <Radio label="无"><span>无</span></Radio>
                      </Radio-group>
                      <span v-else>{{procedureForm.registration}}</span>
                      <i @click="change_p('registration')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="card-v">
                    <div style="width: 215px;white-space: nowrap;">说明书：
                      <Radio-group v-if="pflag.manual"  v-model="procedureForm.manual">
                        <Radio label="有"><span>有</span></Radio>
                        <Radio label="无"><span>无</span></Radio>
                      </Radio-group>
                      <span v-else>{{procedureForm.manual}}</span>
                      <i @click="change_p('manual')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 215px;white-space: nowrap;">原始购车发票：
                      <Radio-group v-if="pflag.invoice"  v-model="procedureForm.invoice">
                        <Radio label="有"><span>有</span></Radio>
                        <Radio label="无"><span>无</span></Radio>
                      </Radio-group>
                      <span v-else>{{procedureForm.invoice}}</span>
                      <i @click="change_p('invoice')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
              </table>
              <div v-else><p>暂无手续信息</p></div>
            </div>
          </Card>
          <div v-if="vehicle.id" style="margin-left: 20px;" class="pic-collapse">
            <Card style="width: 511px; height: 100%;">
              <div class="info-title">
                <div class="circle" style="top: -39px; left: 13px; background-color: #2d8cf0"></div>
              </div>
              <p style="margin-left: 15px" slot="title">相关证件</p>
              <Collapse v-model="pic_value" accordion>
                <Panel name="1">
                  拍卖合同
                  <div slot="content">
                    <div v-if="contractList.length>0">
                    <div style="width: 140px;position: absolute;top: 20px;left: -10px;display: none">
                      <Progress  v-if="percentage !== 0 && percentage !== 100" :percent="percentage" ></Progress>
                    </div>
                    <div style="margin-bottom: 20px;flex-wrap: wrap;" class="flex flex-pack-spacearound flex-align-center">
                      <div v-for="item in contractList" class="contract-photo flex flex-left" style="margin-top: 20px">
                        <div style="margin-top: 5px" class="contract-pic-item2" >
                          <img :src="item.thumb_url"/>
                          <div v-if="item.percentage !== 0 && item.percentage < 100" class="progress">
                            <Progress  :percent="item.percentage" hide-info></Progress>
                          </div>
                          <div class="upload-list-cover">
                            <i style="float: left; margin-left: 40px;width: 40px; height: 40px; margin-top: 16px" class="ivu-icon ivu-icon-ios-eye-outline" @click="viewContract=true; viewContractUrl=item.url;"></i>
                            <div @click="uploadContractForm.id=item.id">
                            <Upload
                              style="float: left;width: 40px; height: 40px; margin-top: 15px"
                              ref="upload"
                              :with-credentials="true"
                                    :data="uploadContractForm"
                                    name="pic"
                                    :show-upload-list="false"
                                    :default-file-list="contractList"
                                    :on-format-error="handleFormatError"
                                    :on-progress="handleUploadProgress"
                                    :before-upload="handleBeforeUpload"
                                    :on-success="handleSuccess"
                                    :on-error="handleError"
                                    accept="image/gif,image/png,image/jpeg,image/jpg,image/bmp"
                                    :format="['jpg','jpeg','png']"
                                    type="drag"

                                    :action="uploadUrl">
                              <i class="ivu-icon ivu-icon-edit"></i>
                              <!--<Icon type="edit"></Icon>-->
                            </Upload></div>
                          </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div v-else>
                      暂无照片
                    </div>
                    <!--</div>-->
                    <div slot="footer"></div>
                  </div>
                </Panel>
                <Panel name="2">
                  登记证
                  <div slot="content">
                    <div v-if="registrationList.length>0">
                      <div style="width: 140px;position: absolute;top: 20px;left: -10px;display: none">
                        <Progress  v-if="percentage !== 0 && percentage !== 100" :percent="percentage" ></Progress>
                      </div>
                      <div style="margin-bottom: 20px;flex-wrap: wrap;" class="flex flex-pack-spacearound flex-align-center">
                        <div v-for="item in registrationList" class="contract-photo flex flex-left" style="margin-top: 20px">
                          <div class="contract-pic-item2" >
                            <img :src="item.thumb_url"/>
                            <div v-if="item.percentage !== 0 && item.percentage < 100" class="progress">
                              <Progress  :percent="item.percentage" hide-info></Progress>
                            </div>
                            <div class="upload-list-cover">
                              <i style="float: left; margin-left: 40px;width: 40px; height: 40px; margin-top: 16px" class="ivu-icon ivu-icon-ios-eye-outline" @click="viewContract=true; viewContractUrl=item.url;"></i>
                              <div @click="uploadRegistrationForm.id=item.id">
                                <Upload
                                  style="float: left;width: 40px; height: 40px; margin-top: 15px"
                                  ref="upload"
                                  :with-credentials="true"
                                  :data="uploadRegistrationForm"
                                  name="pic"
                                  :show-upload-list="false"
                                  :default-file-list="registrationList"
                                  :on-format-error="handleFormatError"
                                  :on-progress="handleUploadProgress"
                                  :before-upload="handleBeforeUpload"
                                  :on-success="handleSuccess"
                                  :on-error="handleError"
                                  accept="image/gif,image/png,image/jpeg,image/jpg,image/bmp"
                                  :format="['jpg','jpeg','png']"
                                  type="drag"
                                  :action="uploadUrl">
                                  <i class="ivu-icon ivu-icon-edit"></i>
                                  <!--<Icon type="edit"></Icon>-->
                                </Upload></div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div v-else>
                      暂无照片
                    </div>
                    <!--</div>-->
                    <div slot="footer"></div>
                  </div>
                </Panel>
                <Panel name="3">
                  行驶证
                  <div slot="content">
                    <div v-if="licenseList.length>0">
                      <div style="width: 140px;position: absolute;top: 20px;left: -10px;display: none">
                        <Progress  v-if="percentage !== 0 && percentage !== 100" :percent="percentage" ></Progress>
                      </div>
                      <div style="margin-bottom: 20px;flex-wrap: wrap;" class="flex flex-pack-spacearound flex-align-center">
                        <div v-for="item in licenseList" class="contract-photo flex flex-left" style="margin-top: 20px">
                          <div class="contract-pic-item2" >
                            <img :src="item.thumb_url"/>
                            <div v-if="item.percentage !== 0 && item.percentage < 100" class="progress">
                              <Progress  :percent="item.percentage" hide-info></Progress>
                            </div>
                            <div class="upload-list-cover">
                              <i style="float: left; margin-left: 40px;width: 40px; height: 40px; margin-top: 16px" class="ivu-icon ivu-icon-ios-eye-outline" @click="viewContract=true; viewContractUrl=item.url;"></i>
                              <div @click="uploadLicenseForm.id=item.id">
                                <Upload
                                  style="float: left;width: 40px; height: 40px; margin-top: 15px"
                                  ref="upload"
                                  :with-credentials="true"
                                  :data="uploadLicenseForm"
                                  name="pic"
                                  :show-upload-list="false"
                                  :default-file-list="licenseList"
                                  :on-format-error="handleFormatError"
                                  :on-progress="handleUploadProgress"
                                  :before-upload="handleBeforeUpload"
                                  :on-success="handleSuccess"
                                  :on-error="handleError"
                                  accept="image/gif,image/png,image/jpeg,image/jpg,image/bmp"
                                  :format="['jpg','jpeg','png']"
                                  type="drag"
                                  :action="uploadUrl">
                                  <i class="ivu-icon ivu-icon-edit"></i>
                                  <!--<Icon type="edit"></Icon>-->
                                </Upload></div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div v-else>
                      暂无照片
                    </div>
                    <!--</div>-->
                    <div slot="footer"></div>
                  </div>
                </Panel>
                <Panel name="4">
                  旧车主证件
                  <div slot="content">
                    <div v-if="ownerList.length>0">
                      <div style="width: 140px;position: absolute;top: 20px;left: -10px;display: none">
                        <Progress  v-if="percentage !== 0 && percentage !== 100" :percent="percentage" ></Progress>
                      </div>
                      <div style="margin-bottom: 20px;flex-wrap: wrap;" class="flex flex-pack-spacearound flex-align-center">
                        <div v-for="item in ownerList" class="contract-photo flex flex-left" style="margin-top: 20px">
                          <div class="contract-pic-item2" >
                            <img :src="item.thumb_url"/>
                            <div v-if="item.percentage !== 0 && item.percentage < 100" class="progress">
                              <Progress  :percent="item.percentage" hide-info></Progress>
                            </div>
                            <div class="upload-list-cover">
                              <i style="float: left; margin-left: 40px;width: 40px; height: 40px; margin-top: 16px" class="ivu-icon ivu-icon-ios-eye-outline" @click="viewContract=true; viewContractUrl=item.url;"></i>
                              <div @click="uploadOwnerForm.id=item.id">
                                <Upload
                                  style="float: left;width: 40px; height: 40px; margin-top: 15px"
                                  ref="upload"
                                  :with-credentials="true"
                                  :data="uploadOwnerForm"
                                  name="pic"
                                  :show-upload-list="false"
                                  :default-file-list="ownerList"
                                  :on-format-error="handleFormatError"
                                  :on-progress="handleUploadProgress"
                                  :before-upload="handleBeforeUpload"
                                  :on-success="handleSuccess"
                                  :on-error="handleError"
                                  accept="image/gif,image/png,image/jpeg,image/jpg,image/bmp"
                                  :format="['jpg','jpeg','png']"
                                  type="drag"

                                  :action="uploadUrl">
                                  <i class="ivu-icon ivu-icon-edit"></i>
                                  <!--<Icon type="edit"></Icon>-->
                                </Upload></div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div v-else>
                      暂无照片
                    </div>
                    <!--</div>-->
                    <div slot="footer"></div>
                  </div>
                </Panel>
              </Collapse>
            </Card>
          </div>
        </div>
        <div>
          <Card style="width: 1190px; margin-top: 20px">
            <div class="info-title">
              <div class="circle" style="background-color: #2d8cf0"></div>
            </div>
            <p style="margin-left: 15px" slot="title">过户基本信息</p>
            <div>
              <table v-if="vehicle.id" class="transform-table">
                <tr>
                  <td colspan="3" class="card-v">
                    <div style="white-space: nowrap;display: flex">看车地址：
                      <Select v-if="tflag.look_addr" @on-change="showSaveAddr = false" style="margin-top: -6px; width: 280px" size="large"  placeholder="常用地址" v-model="transForm.look_addr">
                        <Option  v-for="item in addrList"  :value="item" :key="item">{{item}}</Option>
                      </Select>
                      <Input v-if="tflag.look_addr" @on-blur="inputNewAddr" class="no-border" style="width: 380px; margin-left: 10px; margin-top: -6px"  v-model="transForm.look_addr" size="large" placeholder="请输入看车地址"></Input>
                      <div class="modal-button addr-button" @click="saveNewAddr" v-if="showSaveAddr && tflag.look_addr" type="primary">保存为常用地址</div>
                      <span v-if="!tflag.look_addr">
                       {{transForm.look_addr}}
                      </span>
                      <i @click="change_t('look_addr')" style="margin-left: 10px; margin-top: 4px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>

                </tr>
                <tr>
                  <td class="card-v">
                    <div style=" width: 350px;white-space: nowrap;">看车联系人：
                      <Input v-if="tflag.look_contract" type="text" style="width: 189px" v-model="transForm.look_contract"></Input>
                      <span v-if="!tflag.look_contract">
                       {{transForm.look_contract}}
                      </span>
                      <i @click="change_t('look_contract')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">车辆所在地：
                      <Select v-if="tflag.vehicle_addr" style="width: 80px" size="large" placeholder="请选择省份" v-model="province_id">
                        <Option  v-for="item in provinceList"  :value="item.province_id" :key="item.province_id">{{item.name}}</Option>
                      </Select>
                      <Select v-if="tflag.vehicle_addr" style="width: 105px" size="large" class="gh-select"  placeholder="请选择城市" v-model="city">
                        <Option v-for="item in cityList" :value="item.city_id" :key="item.city_id">{{item.name}}</Option>
                      </Select>
                      <span v-if="!tflag.vehicle_addr">
                       {{transForm.vehicle_addr}}
                      </span>
                      <i @click="change_t('vehicle_addr')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style=" width: 350px;white-space: nowrap;">看车电话：
                      <Input v-if="tflag.look_tel" type="text" style="width: 189px" v-model="transForm.look_tel"></Input>
                      <span v-if="!tflag.look_tel">
                       {{transForm.look_tel}}
                      </span>
                      <i @click="change_t('look_tel')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">跟进服务中心：
                      <Select v-if="tflag.transfer_addr" style="width: 200px" v-model="transForm.transfer_addr" size="large" class="gh-select"  placeholder="请选择过户地点" >
                        <Option v-for="item in ghAddrList" :value="item" :key="item">{{item}}</Option>
                      </Select>
                      <span v-if="!tflag.transfer_addr">
                       {{transForm.transfer_addr}}
                      </span>
                      <i @click="change_t('transfer_addr')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">业务员姓名：
                      <Input v-if="tflag.salename" type="text" style="width: 190px" v-model="transForm.salename"></Input>
                      <span v-else>{{transForm.salename}}</span>
                      <i @click="change_t('salename')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">业务员手机：
                      <Input v-if="tflag.salephone" type="text" style="width: 170px" v-model="transForm.salephone"></Input>
                      <span v-else>{{transForm.salephone}}</span>
                      <i @click="change_t('salephone')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">旧车主：
                      <Input v-if="tflag.old_owner" type="text" style="width: 187px" v-model="transForm.old_owner"></Input>
                      <span v-else>{{transForm.old_owner}}</span>
                      <i @click="change_t('old_owner')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">旧车主类型：
                      <Select v-if="tflag.old_owner_type" style="width: 192px" v-model="transForm.old_owner_type" size="large" class="gh-select"  placeholder="请选择过户地点" >
                        <Option v-for="item in oldOwnerTypeList" :value="item.value" :key="item.value">{{item.name}}</Option>
                      </Select>
                      <span v-if="!tflag.old_owner_type">{{transForm.old_owner_type && oldOwnerTypeList[Number(transForm.old_owner_type) - 1].name}}</span>
                      <i @click="change_t('old_owner_type')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">旧车主联系电话：
                      <Input v-if="tflag.old_owner_tel" type="text" style="width: 138px" v-model="transForm.old_owner_tel"></Input>
                      <span v-else>{{transForm.old_owner_tel}}</span>
                      <i @click="change_t('old_owner_tel')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">过户次数：
                      <Input-number v-if="tflag.transfer_time" :min="0" size="large" style="width: 170px" v-model="transForm.transfer_time"></Input-number>
                      <span v-else>{{transForm.transfer_time}}</span>
                      <i @click="change_t('transfer_time')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">过户相关：
                      <Input v-if="tflag.transfer_about" type="text" style="width: 207px" v-model="transForm.transfer_about"></Input>
                      <span v-else>{{transForm.transfer_about}}</span>
                      <i @click="change_t('transfer_about')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">车辆预计入库时间：
                      <Input v-if="tflag.be_put_in_time" type="text" style="width: 124px" v-model="transForm.be_put_in_time"></Input>
                      <span v-else>{{transForm.be_put_in_time}}</span>
                      <i @click="change_t('be_put_in_time')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td class="card-v">
                    <div style="width: 350px;white-space: nowrap;">购置税：
                      <Radio-group v-if="tflag.purchase_tax" style="width: 220px" v-model="transForm.purchase_tax">
                        <Radio label="有"><span>有</span></Radio>
                        <Radio label="无"><span>无</span></Radio>
                        <Radio label="免"><span>免</span></Radio>
                        <Radio label="丢失"><span>丢失</span></Radio>
                      </Radio-group>
                      <span v-else>{{transForm.purchase_tax}}</span>
                      <i @click="change_t('purchase_tax')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                  <td colspan="2" class="card-v">
                    <div style=" width: 800px">
                      <div style="float: left">过户说明：</div>
                      <Input v-if="tflag.transfer_info" type="textarea" :rows="2" style="width: 600px" v-model="transForm.transfer_info"></Input>
                      <div v-else style="float: left">{{transForm.transfer_info}}</div>
                      <i @click="change_t('transfer_info')" style="margin-left: 10px" class=" i-edit ivu-icon ivu-icon-edit"></i>
                    </div>
                  </td>
                </tr>
              </table>
              <div v-else><p>暂无过户信息</p></div>
            </div>
          </Card>
        </div>
        <carDetection :id="vehicle.id"></carDetection>
        <BackTop></BackTop>
        <Modal width="420px" v-model="lic_modal" title="修改车牌" okText='修改' cancelText='取消修改' :mask-closable="false"
               @on-cancel="cancel">
          <div style="margin-left: 37px"><span style="font-size: 14px">现车牌:</span><span style="font-size: 14px; margin-left:8px"> {{vehicle.licenseplace}}</span></div>
          <div style="margin-left: 20px; margin-bottom: 60px; margin-top: 20px ">
            <span style="font-size: 14px; float: left; margin-top: 6px">修改车牌:</span>
            <Input style="margin-left:8px; float: left; width: 250px" v-model="change_lic"></Input>
          </div>
          <div slot="footer">
            <Button type="primary" size="large" long :loading="lic_loading" @click="lic_change">修改车牌</Button>
          </div>
        </Modal>
        <Modal class="img-modal" title="查看合同" v-model="viewContract">
          <img :src="viewContractUrl" v-if="viewContract" style="width: 100%">
          <div slot="footer"></div>
        </Modal>
      </div>
    </div>
  </div>
</template>
<script>
  import carDetection from './car-detection';

  export default {
    data() {
      return {
        id: '',
        options: [],
        payees: [],
        users: [],
        userData: [],
        storeList: [],
        loading: false,
        lic_modal: false,
        lic_loading: false,
        valuer_loading: false,
        store_loading: false,
        change_lic: '',
        change_valuer: null,
        change_store: null,
        isPackCar: false,
        sale_type_input: '',
        payRequestInput: '',
        transRequestInput: '',
        pic_value: null,
        v_edit: false,
        s_edit: false,
        has_auction: false,
        vflag: null,
        vehicle: {
          id: '', licenseplace: '', brand: '', series: '', model: '', valuer_id: '', valued: null, store_id: '',
          store_name: '', valuer_name: '', valuer_user_name: '', vehicle_type: '', vin: '', cartype: '', bconfiguration: '', client_idcard: '',
          client_name: '', client_phone: '', color: '', criterion: '', displacement: '', engineno: '', factory_date: '',
          factory_date2: '', gearbox: '', getlicence_date: '', getlicence_date2: '', is_engineno_complete: null,
          is_vin_complete: null, mileage: null, modelyear: '', origin_price: '', owner_type: '', record_date: null,
          register_data: null, seat_count: null, sub_status: null, supplementary: '', usage: '', want_price: null,
          wants: null,
        },
        aflag: null,
        auction:{
          auction_type: '', balance_contract_price: null, balance_counttype: null, balance_pay_for_client: null,
          balance_payee_bankAccount: '', balance_payee_id: null, bundling_vehicle: '', client_name: '', client_phone: '',
          deal_price: null, end_time: '', executor: null, executor_phone: null, fee0: null,
          fee1: null, fee2: null, fee3: null, fee4: null, fee5: null, feetype0: '1', feetype1: '1', feetype2: '1',
          feetype3: '1', feetype4: '1', feetype5: '1', feename4: '', id: null, old_auction_id: null, reserve_price: null,
          sale_type: '', start_time: '', starting_price: null, status: null, can_resale: false, pay_req: '',
          transfer_req: '', other_req: '',
        },
        order: {
          isConfirmPay: null,
          order_status: null,
        },
        transForm: {
          look_addr: "", old_owner_type: '', be_put_in_time: "", look_contract: "", look_tel: "", old_owner: "",
          old_owner_tel: "", purchase_tax: "", transfer_about: "", transfer_info: "", transfer_time: "",
          vehicle_addr: '', moreInfo: '', transfer_addr: '', vehicle_addr_cityid: '', vehicle_addr_provinceid: '',
          salephone: '', salename: '',
        },
        tflag: null,
        procedureForm: {
          annual_ticket_vld2: '', annual_ticket_vld: '', annual_verification_info: "", annual_verification_vld2: "",
          come_insurance_vld2: "", commercial_insurance_price: "", commercial_insurance_vld2: "",
          annual_verification_vld: "", come_insurance_vld: "", commercial_insurance_vld: "", endorsement: "",
          endorsement_info: "", invoice: "", maintenance_log: "", maintenance_procedure: "", manual: "",
          modification_info: "", registration: "", vehicle_and_vessel_tax_vld2: "", vehicle_and_vessel_tax_vld: "",
          vehicle_license: "", vehicle_warranty: ""
        },
        pflag: null,
        auctionBFormOption: [
          {value: 4, label: '付成交价+分润'},
          {value: 5, label: '付合同价+分润'},
          {value: 6, label: '付成交价(0分润)'}
        ],
        auctionFormOption: [
          {name: '4S店置换拍卖(车款付4S店)', id: 50001600},
          {name: '私人委托拍卖(车款付4S店)', id: 50001940},
          {name: '4S店置换拍卖(车款付车主)', id: 50001920},
          {name: '私人委托拍卖(车款付车主)', id: 50001603},
          {name: '4S店公务/试驾车(固定资产)', id: 50001604},
          {name: '企业委托拍卖(大客户部专用)', id: 50001660},
          {name: '唯普拍卖(非4S店渠道)', id: 50001602},
          {name: '4S店收购拍卖', id: 50001601},
          {name: '自定义', id: 0}
        ],
        feetype: [
          {value: '1', label: '实际金额'},
          {value: '2', label: '成交比例'}
        ],
        payRequestOption: [
          {value: '72小时', label: '72小时'},
          {value: '48小时', label: '48小时'},
          {value: '24小时', label: '24小时'},
          {value: '自定义', label: '自定义'}
        ],
        transRequestOption: [
          {value: '72小时', label: '72小时'},
          {value: '一周', label: '一周'},
          {value: '两周', label: '两周'},
          {value: '自定义', label: '自定义'}
        ],
        showSaveAddr: false,
        addrList: [],
        cityList: [],
        cityList2: [],
        provinceList: [],
        province_id: '',
        city: '',
        oldOwnerTypeList: [
          {name: '私人', value: '1'}, {name: '国有企业', value: '2'}, {name: '外商投资', value: '3'},
          {name: '私营企业(有限公司)', value: '4'}, {name: '个体户', value: '5'}
          ],
        ghAddrList: [],
        endorsement_list:[
          {name: '交车前的违章由卖家负责，交车后的违章由买家负责', value: 0},
          {name: '所有违章均由买家负责', value: 1},
          {name: '所有违章均由卖家负责', value: 2}
        ],
        modification_list:[
          {name: '如有改装，过户时如需复原，改装及其费用由买家负责', value: 0},
          {name: '如有改装，过户时如需复原，改装及其费用由卖家负责', value: 1},
          {name: '如有改装，过户时如需复原，改装及其费用由过户部代为办理', value: 2},
          {name: '该车无改装', value: 3}
        ],
        contractList: [],
        registrationList: [],
        licenseList: [],
        ownerList: [],
        viewContract: false,
        uploadContractForm: {
          id: null,
          vehicle_id: null,
          type: 'CONTRACT'
        },
        uploadRegistrationForm: {
          id: null,
          vehicle_id: null,
          type: 'REGISTRATION',
        },
        uploadLicenseForm: {
          id: null,
          vehicle_id: null,
          type: 'LICENSE',
        },
        uploadOwnerForm: {
          id: null,
          vehicle_id: this.$route.query.id,
          type: 'OLDOWNER',
        },
        percentage: null,
        uploadUrl: process.env.API + 'pic/vehicle_pic/upload',
      };
    },
    created: function() {
      this.init_status();
      this.loadAddrs();
      this.getProvinces();
    },
    watch: {
      province_id: function (n) {
        this.selectCity(n);
      },
      city: function (n) {
        var province = '';
        for (var k in this.provinceList) {
          if (this.provinceList[k].province_id === this.province_id) {
            province = this.provinceList[k].name;
          }
        }
        var city = '';
        for (var k in this.cityList) {
          if (this.cityList[k].city_id === n) {
            city = this.cityList[k].name;
          }
        }
        this.transForm.vehicle_addr_provinceid = this.province_id;
        this.transForm.vehicle_addr_cityid = n;
        this.loadVaddr (province + city);
      },
    },
    methods: {
      init_status() {
       this.vflag =  {
         vin: false, licenseplace: false, brand: false, series: false, model: false, valuer_id: false, valued: false,
         store_id: false, store_name: false, vehicle_type: false, vin: false, cartype: false, bconfiguration: false,
         client_idcard: false, client_name: false, client_phone: false, color: false, criterion: false,
         displacement: false, engineno: false, factory_date: false, gearbox: false, getlicence_date: false,
         is_engineno_complete: false, is_vin_complete: false, mileage: false, modelyear: false, origin_price: false,
         owner_type: false, record_date: false, register_data: false, seat_count: false, sub_status: false,
         supplementary: false, usage: false, want_price: false, wants: false,
      };
      this.aflag = {
        auction_type: false, balance_contract_price: false, balance_counttype: false, balance_pay_for_client: false,
        balance_payee_id: false, bundling_vehicle: false, client_name: false, client_phone: false, deal_price: false,
        end_time: false, executor: false, executor_phone: false,
        fee0: false, fee1: false, fee2: false, fee3: false, fee4: false, fee5: false,
        feetype0: false, feetype1: false, feetype2: false, feetype3: false, feetype4: false, feetype5: false,
        feename4: false, id: false, old_auction_id: false, reserve_price: false, sale_type: false, start_time: false,
        starting_price: false, status: false, pay_req: false, transfer_req: false, other_req: false,
      };
      this.tflag = {
        look_addr: false, old_owner_type: false, be_put_in_time: false, look_contract: false, look_tel: false,
        old_owner: false, old_owner_tel: false, purchase_tax: false, transfer_about: false, transfer_info: false,
        transfer_time: false, vehicle_addr: false, moreInfo: false, transfer_addr: false, vehicle_addr_cityid: false,
        vehicle_addr_provinceid: false, salephone: false, salename: false,
      };
      this.pflag = {
        annual_ticket_vld2: false, annual_ticket_vld: false, annual_verification_info: false,
        annual_verification_vld2: false, come_insurance_vld2: false, commercial_insurance_price: false,
        commercial_insurance_vld2: false, annual_verification_vld: false, come_insurance_vld: false,
        commercial_insurance_vld: false, endorsement: false, endorsement_info: false, invoice: false,
        maintenance_log: false, maintenance_procedure: false, manual: false, modification_info: false,
        registration: false, vehicle_and_vessel_tax_vld2: false, vehicle_and_vessel_tax_vld: false,
        vehicle_license: false, vehicle_warranty: false
      };
      this.lic_modal = false;
      this.lic_loading = false;
      this.valuer_loading = false;
      this.store_loading = false;
      this.change_lic = '';
      this.change_valuer = null;
      this.change_store = null;
      this.isPackCar = false;
      this.sale_type_input = '';
      this.payRequestInput = '';
      this.transRequestInput = '';
      this.v_edit = false;
      this.s_edit = false;
      this.has_auction = false;

      },
      getLicense() {
        console.log(this.id);
        this.init_status();
        this.uploadContractForm.vehicle_id = this.id;
        this.uploadRegistrationForm.vehicle_id = this.id;
        this.ajax.get('/vehicle/get_vehicle?id=' + this.id).then(rsp => {
          if (rsp.data.code === 0){
            console.log(rsp.data.data);
            for (var k in this.vehicle) {
              this.vehicle[k] = rsp.data.data.vehicle_item[k];
            }
            if (rsp.data.data.auction_item){
              this.has_auction = true;
              for (var x in this.auction) {
                this.auction[x] = rsp.data.data.auction_item[x];
              }
              this.auction.feetype0 = this.auction.feetype0.toString();
              this.auction.feetype1 = this.auction.feetype1.toString();
              this.auction.feetype2 = this.auction.feetype2.toString();
              this.auction.feetype3 = this.auction.feetype3.toString();
              this.auction.feetype4 = this.auction.feetype4.toString();
              this.auction.feetype5 = this.auction.feetype5.toString();
              console.log(this.auction);
            }
            else {
              this.has_auction = false;
            }
            if (rsp.data.data.order_item) {
              for (var y in this.order) {
                this.order[y] = rsp.data.data.order_item[y];
              }
            }
            this.options = [];
            this.users = [];
            this.userData = [];
            this.storeList = [];
            this.payees = [];
          }
        });
        this.ajax.get('/vehicle/info/transfer?id=' + this.id,).then(response => {
          console.log('过户信息', response.data.data);
          var res =  response.data.data;
          if (response.data.code === 0) {
            this.transForm = res;
            this.transForm.transfer_time = Number(res.transfer_time);
            this.province_id = Number(this.transForm.vehicle_addr_provinceid)
          }
        });
        this.ajax.get('/vehicle/info/procedure?id=' + this.id).then(response => {
          console.log('手续信息', response.data.data);
          if (response.data.code === 0) {
            this.procedureForm = response.data.data;
          }
        });
        this.ajax.get('/pic/vehicle_pic/contract/list?vehicle_id='+this.id).then(rsp => {
          this.contractList = rsp.data.data.items;
        });
        this.ajax.get('/pic/vehicle_pic/registration/list?vehicle_id='+this.id).then(rsp => {
          this.registrationList = rsp.data.data.items
        });
        this.ajax.get('/pic/vehicle_pic/license/list?vehicle_id='+this.id).then(rsp => {
          this.licenseList = rsp.data.data.items
        });
        this.ajax.get('/pic/vehicle_pic/oldowner/list?vehicle_id='+this.id).then(rsp => {
          this.ownerList = rsp.data.data.items
        });
      },
      remoteMethod (query) {
        if (query && query.length > 3) {
          this.loading = true;
          this.ajax.get('/vehicle/find_license?licenseplace=' + query).then(rsp => {
            if (rsp.data.code === 0){
              console.log(rsp.data.data);
              this.options = rsp.data.data;
            }
            this.loading = false;
          }, err => {
            this.loading = false;
          });
        }
      },
      valuerMethod (query) {
        this.users = [];
        if (query && query.length > 0) {
          this.loading = true;
          this.ajax.get('/vehicle/find_valuer?userName=' + query).then(rsp => {
            if (rsp.data.code === 0){
              console.log(rsp.data.data);
              this.users = rsp.data.data.sort((a,b) => a.userName.length-b.userName.length);
            }
            this.loading = false;
          }, err => {
            this.loading = false;
          });
        }
      },
      payeeMethod (query) {
        if (query && query.length > 2) {
          this.payees = []
          this.loading = true;
          this.ajax.get('/vehicle/find_payee?text=' + query).then(rsp => {
            if (rsp.data.code === 0){
              console.log(rsp.data.data);
              this.payees = rsp.data.data;
            }
            this.loading = false;
          }, err => {
            this.loading = false;
          });
        }
      },
      change_v(field) {
        var dateform = {};
        dateform['id']= this.vehicle.id;
        dateform['user_id'] = this.$store.state.user.id;
        dateform[field] = this.vehicle[field];
        console.log(dateform);
        if (this.vflag[field]&&dateform['id']) {
          this.ajax.post('/vehicle/update_vehicle', dateform).then(response => {
            console.log('保存结果', response.data.msg);
            if (response.data.code === 0) {
              this.$Message.success('保存成功');
              this.getLicense()
            } else {
            }
          })
        }
        this.vflag[field] = !this.vflag[field];
      },
      change_t(field) {
        var dateform = {};
        dateform['id']= this.vehicle.id;
        dateform['user_id'] = this.$store.state.user.id;
        dateform[field] = this.transForm[field];
        console.log(dateform);
        if (this.tflag[field] && dateform['id']) {
          this.ajax.post('/vehicle/update/transfer', dateform).then(response => {
            console.log('保存结果', response.data.msg);
            if (response.data.code === 0) {
              this.$Message.success('保存成功');
              this.getLicense()
            } else {
            }
          })
        }
        this.tflag[field] = !this.tflag[field];

      },
      change_p(field) {
        var dateform = {};
        dateform['id']= this.vehicle.id;
        dateform['user_id'] = this.$store.state.user.id;
        dateform[field] = this.procedureForm[field];
        console.log(dateform);
        if (this.pflag[field] && dateform['id']) {
          this.ajax.post('/vehicle/update/procedure', dateform).then(response => {
            console.log('保存结果', response.data.msg);
            if (response.data.code === 0) {
              this.$Message.success('保存成功');
              this.getLicense()
            } else {
            }
          })
        }
        this.pflag[field] = !this.pflag[field];

      },
      change_a(field) {
        var dataform = {};
        dataform['id']= this.vehicle.id;
        dataform['user_id'] = this.$store.state.user.id;
        if (field ==='pay_req' && this.auction.pay_req === '自定义') {
          this.auction.pay_req = this.payRequestInput
        }
        if (field ==='transfer_req' && this.auction.pay_req === '自定义') {
          this.auction.transfer_req = this.transRequestInput
        }
        if (field === 'sale_type' && this.auction.sale_type === '自定义') {
          this.auction.sale_type = this.sale_type_input;
        }
        if (field === 'bundling_vehicle' && !this.isPackCar) {
          this.auction.bundling_vehicle = '';
        }
        if (field === 'fee0' || field === 'fee1' || field === 'fee2' || field === 'fee3' || field === 'fee4' || field === 'fee5') {
          dataform['feetype' + field.slice(3)] = this.auction['feetype' + field.slice(3)];
          if (field === 'fee4') {
            dataform['feename4'] = this.auction.feename4;
          }
        }
        if (field === 'balance_counttype' && this.auction.balance_counttype === 5) {
          dataform['balance_contract_price'] = this.auction.balance_contract_price;
        }
        dataform[field] = this.auction[field];
        console.log(dataform);
        if (this.aflag[field]&&dataform['id']) {
          this.ajax.post('/vehicle/update_auction', dataform).then(response => {
            console.log('保存结果', response.data.msg);
            if (response.data.code === 0) {
              this.$Message.success('保存成功');
              this.getLicense()
            } else {
            }
          })
        }
        this.aflag[field] = !this.aflag[field];
      },
      lic_change () {
        if(this.change_lic.length>6){
          this.lic_loading = true;
          setTimeout(() => {
            var dataform = {};
            dataform['id'] = this.vehicle.id;
            dataform['user_id'] = this.$store.state.user.id;
            dataform['licenseplace'] = this.change_lic;
            this.ajax.post('/vehicle/change_license', dataform).then(response => {
              console.log('保存结果', response.data.msg);
              if (response.data.code === 0) {
                this.lic_loading = false;
                this.v_edit = false;
                this.$Message.success('修改成功');
                this.lic_modal = false;
                this.getLicense();
              } else {
                this.$Message.error('修改失败')
              }
            });
          }, 500);
        }
        else {
          this.$Message.warning('输入id过短');
        }

      },
      valuer_change () {
        console.log(this.change_valuer);
        if(this.change_valuer){
          this.valuer_loading = true;
          setTimeout(() => {
            var dataform = {};
            dataform['id'] = this.vehicle.id;
            dataform['user_id'] = this.$store.state.user.id;
            dataform['valuer_id'] = this.change_valuer;
            this.ajax.post('/vehicle/change_valuer', dataform).then(response => {
              console.log('保存结果', response.data.msg);
              if (response.data.code === 0) {
                this.valuer_loading = false;
                this.v_edit = false;
                this.$Message.success('修改成功');
                this.getLicense();
              } else {
                this.$Message.error('修改失败')
              }
            });
          }, 500);
          this.users=[];
          this.userData=[];
          // this.change_valuer = '';
        }
        else {
          // this.$Message.warning('输入车牌过短');
        }
        // this.change_valuer = null;
        //  不知道为什么加了上面这一句就报错? 有大佬帮忙研究下
      },
      try_s_edit(){
        if (this.order.order_status < 65 && this.order.isConfirmPay === 1) {
          this.$Notice.warning({
            title: '禁止修改',
            desc: '请在监管系统取消已收款状态再修改门店',
            duration: 0
          });
        }
        else {
          this.ajax.get('/vehicle/get_all_store')
            .then(rsp => {
              if (rsp.data.code === 0){
                console.log(rsp.data.data);
                this.storeList = rsp.data.data;
              }
            });
          this.s_edit = true;
        }

      },
      store_change () {
        if(this.change_store){
          this.store_loading = true;
          setTimeout(() => {
          var dataform = {};
          dataform['id'] = this.vehicle.id;
          dataform['user_id'] = this.$store.state.user.id;
          dataform['store_id'] = this.change_store;
            this.ajax.post('/vehicle/change_store', dataform).then(response => {
              console.log('保存结果', response.data.msg);
              if (response.data.code === 0) {
                this.store_loading = false;
                this.s_edit = false;
                this.$Message.success('修改成功');
                this.getLicense();
              } else {
                this.$Message.error('修改失败')
              }
            });
          }, 500);
        }
        else {
        }
      },
      cancel () {
        this.$Message.info('已经取消');
      },
      validateNumber (e) {
        if (e.target.value) {
          var m = e.target.value.match(/(([1-9]\d*)|0)(\.\d*)?/g)
          if (!m) {
            e.target.value = ''
          } else if (e.target.value !== m[0]) {
            e.target.value = m[0]
          }
        }
      },
      inputNewAddr(){
        console.log(this.transForm.look_addr );
        if (this.transForm.look_addr ) {
          if (this.addrList.indexOf(this.transForm.look_addr) >= 0) {
            this.showSaveAddr = false
          } else {
            this.showSaveAddr = true
          }
        } else {
          this.showSaveAddr = false
        }
      },
      saveNewAddr(){
        if (this.transForm.look_addr ) {
          this.ajax.post('/area/add_look_addr',{
            addr: this.transForm.look_addr
          }).then(response => {
            console.log('保存结果', response.data.data);
            if (response.data.code === 0) {
              this.$Message.success('保存成功');
              this.showSaveAddr = false;
              this.loadAddrs();
            } else {
              this.$Loading.error('保存失败');
            }
          })
        }
      },
      loadVaddr (addr) {
        this.transForm.vehicle_addr = addr;
      },
      getProvinces () {
        this.ajax.get('/area/provinces').then(response =>  {
          console.log('provinces', response.data.items);
          this.provinceList = response.data.items
        })
      },
      selectCity (id) {
        this.ajax.get('/area/citys?province_id=' + id).then(response =>  {
          this.cityList = response.data.items
          if (this.transForm.vehicle_addr_cityid) {
            this.city = Number(this.transForm.vehicle_addr_cityid)
          }
        })
      },
      loadAddrs () {
        this.ajax.get('/area/look_addr').then(response =>  {
          this.addrList = response.data.items
        });
        this.ajax.get('/area/transfer_addr').then(response =>  {
          this.ghAddrList = response.data.items
          this.ghAddrList.push('其它')
        })
      },
      handleBeforeUpload (file) {
        console.log('handleBeforeUpload',file)
        this.percentage = 0
      },
      handleSuccess (res, file) {
        if (res.code===0) {
          this.ajax.get('/pic/vehicle_pic/contract/list?vehicle_id='+this.id).then(rsp => {
            this.contractList = rsp.data.data.items;
          });
          this.ajax.get('/pic/vehicle_pic/registration/list?vehicle_id='+this.id).then(rsp => {
            this.registrationList = rsp.data.data.items
          });
          this.ajax.get('/pic/vehicle_pic/license/list?vehicle_id='+this.id).then(rsp => {
            this.licenseList = rsp.data.data.items
          });
          this.ajax.get('/pic/vehicle_pic/oldowner/list?vehicle_id='+this.id).then(rsp => {
            this.ownerList = rsp.data.data.items
          });
          this.$emit('save');
          this.$Message.success('修改成功');
        }
      },
      handleUploadProgress (e,file) {
        console.log('handleUploadProgress',file)
        this.percentage = parseInt(e.percent)
      },
      handleFormatError (file) {
        this.$Notice.warning({
          title: '文件格式不正确',
          desc: '文件 ' + file.name + ' 格式不正确，请上传 jpg 或 png 格式的图片。'
        });
      },
      handleError(error, rsp, fileList) {
        console.log(error, rsp, fileList);
        this.$Message.error({content:rsp.msg,duration:5,closable:true})
      },
    },
    filters: {
      get_status: function (value) {
        const status_dict = {
          0: '临时', 1: '潜客', 2: '正在报价', 3: '报价结束', 4: 'C2B线索', 5: '线索',
          10: '待签合同', 11: '待提交', 12: '流拍', 13: '已驳回', 14: '审核中', 15: '编辑再审核', 16: '修改再审核', 17: '区域经理已审核',
          21: '即将开拍', 22: '拍卖中',
          32: '未审核未收款', 33: '已审核未收款', 34: '未审核已收款', 35: '已审核已收款',
          41: '仲裁关闭', 42: '已关闭', 43: '卖家已确认',
          50: '意向中', 51: '未发布', 52: '已发布',
          60: '结束跟进',
        };
        return status_dict[value];
      }
    },
    components: {
      carDetection
    }
  }
</script>
<style lang="less" scoped>
</style>
