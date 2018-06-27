<template>
  <div>
    <Card style="width: 1190px; margin-top: 20px">
      <div class="info-title">
        <div class="circle" style="background-color: #2d8cf0"></div>
      </div>
      <p style="margin-left: 15px" slot="title">车辆检测信息</p>
      <Tabs v-if="id" style="margin-top: -5px" class="detectTabs" value="photo">
        <TabPane label="车辆拍照" name="photo">
          <div v-if="carPhoto.length>0">
            <div style="display: inline-flex" v-for="k in carPhoto">
              <div style="display: inline-flex;">
                <div style="width: 140px;position: absolute;top: 20px;left: -10px;display: none">
                  <Progress  v-if="percentage !== 0 && percentage !== 100" :percent="percentage" ></Progress>
                </div>
                <div style="text-align:center; margin-bottom: 20px; margin-left: 20px; flex-wrap: wrap;" class="flex-pack-spacearound flex-align-center">
                  <div class="contract-pic-item2">
                      <img :src="k.thumb_url"/>
                      <div v-if="k.percentage !== 0 && k.percentage < 100" class="progress">
                        <Progress  :percent="k.percentage" hide-info></Progress>
                      </div>
                      <div style="height: 96%" class="upload-list-cover">
                        <i style="float: left; margin-left: 40px;width: 40px; height: 40px; margin-top: 16px" class="ivu-icon ivu-icon-ios-eye-outline" @click="viewPhoto=true; viewPhotoUrl=k.url;"></i>
                        <div @click="uploadPhotoForm.id=k.id, uploadPhotoForm.name=k.name">
                          <Upload
                            style="float: left;width: 40px; height: 40px; margin-top: 15px"
                            ref="upload"
                            :with-credentials="true"
                            :data="uploadPhotoForm"
                            name="pic"
                            :show-upload-list="false"
                            :default-file-list="k[0]"
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
                          </Upload>
                        </div>
                      </div>
                    </div>
                  {{ k.name }}
                </div>
              </div>
            </div>
          </div>
          <div v-else>
            暂无照片
          </div>
          <!--</div>-->


          <!--</div>-->
          <div slot="footer"></div>





        </TabPane>
      </Tabs>
      <div v-else><p>暂无车辆信息</p></div>
    </Card>


    <Modal class="img-modal" title="查看图片" v-model="viewPhoto">
      <img :src="viewPhotoUrl" v-if="viewPhoto" style="width: 100%">
      <div slot="footer"></div>
    </Modal>
  </div>
</template>

<script>
    export default {
      props: ["id"],
      data(){
        return {
          uploadUrl: process.env.API + 'pic/vehicle_pic/upload',
          viewPhoto: false,
          uploadPhotoForm: {id: null, name: '', vehicle_id: null, type: 'PHOTO'},
          carPhoto:[],
          percentage: null,
        }
      },
      created: function () {
      },
      watch: {
        id:function () {
          this.loadinfo();
        }
      },
      methods: {
        loadinfo () {
          this.ajax.get('pic/vehicle_pic/photo/list?vehicle_id=' + this.id,).then(response => {
            console.log('车辆图片', response.data.data);
            var res = response.data.data.items;
            this.carPhoto = res;
            console.log(this.carPhoto)
          })
        },
        handleBeforeUpload (file) {
          console.log('handleBeforeUpload',file)
          this.percentage = 0
        },
        handleSuccess (res, file) {
          if (res.code===0) {
            this.loadinfo();
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
      }

    }
</script>

<style scoped>

</style>
