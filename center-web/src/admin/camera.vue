<template>
  <div>
    <div class="home-page">
      <!--首页-->
      <div>
        <div style="flex-wrap: wrap;" class="flex flex-pack-spacearound">
          <Card style="width: 280px; height: 280px; margin-left: 20px; margin-bottom: 30px; text-align: center">
            <Upload
              style="margin-left: -15px;margin-top: 8px; float: left;width: 280px; height: 280px"
              ref="upload"
              :with-credentials="true"
              name="pic"
              :show-upload-list="false"
              :on-format-error="handleFormatError"
              :on-progress="handleUploadProgress"
              :before-upload="handleBeforeUpload"
              :on-success="handleSuccess"
              :on-error="handleError"
              accept="image/gif,image/png,image/jpeg,image/jpg,image/bmp"
              :format="['jpg','jpeg','png']"
              type="drag"
              :action="uploadUrl">
              <!--<div>--><div>
              <Icon type="camera" size="200"></Icon></div>
              <span style="margin-top:20px;font-size: 16px; font-weight: bold;">摄像头1</span>
            </Upload>
          </Card>
          <Card style="width: 280px; height: 280px; margin-left: 20px; margin-bottom: 30px; text-align: center">
            <Upload
              style="margin-left: -15px;margin-top: 8px; float: left;width: 280px; height: 280px"
              ref="upload"
              :with-credentials="true"
              name="pic"
              :show-upload-list="false"
              :on-format-error="handleFormatError"
              :on-progress="handleUploadProgress"
              :before-upload="handleBeforeUpload"
              :on-success="handleSuccess"
              :on-error="handleError"
              accept="image/gif,image/png,image/jpeg,image/jpg,image/bmp"
              :format="['jpg','jpeg','png']"
              type="drag"
              :action="uploadUrl">
              <!--<div>--><div>
              <Icon type="camera" size="200"></Icon></div>
              <span style="margin-top:20px;font-size: 16px; font-weight: bold;">摄像头2</span>
            </Upload>
          </Card>
          <Card style="width: 280px; height: 280px; margin-left: 20px; margin-bottom: 30px; text-align: center">
            <Upload
              style="margin-left: -15px;margin-top: 8px; float: left;width: 280px; height: 280px"
              ref="upload"
              :with-credentials="true"
              name="pic"
              :show-upload-list="false"
              :on-format-error="handleFormatError"
              :on-progress="handleUploadProgress"
              :before-upload="handleBeforeUpload"
              :on-success="handleSuccess1"
              :on-error="handleError"
              accept="image/gif,image/png,image/jpeg,image/jpg,image/bmp"
              :format="['jpg','jpeg','png']"
              type="drag"
              :action="uploadUrl">
              <!--<div>--><div>
              <Icon type="camera" size="200"></Icon></div>
              <span style="margin-top:20px;font-size: 16px; font-weight: bold;">摄像头3</span>
            </Upload>
          </Card>
          <Card style="width: 280px; height: 280px; margin-left: 20px; margin-bottom: 30px; text-align: center">
            <Upload
              style="margin-left: -15px;margin-top: 8px; float: left;width: 280px; height: 280px"
              ref="upload"
              :with-credentials="true"
              name="pic"
              :show-upload-list="false"
              :on-format-error="handleFormatError"
              :on-progress="handleUploadProgress"
              :before-upload="handleBeforeUpload"
              :on-success="handleSuccess1"
              :on-error="handleError"
              accept="image/gif,image/png,image/jpeg,image/jpg,image/bmp"
              :format="['jpg','jpeg','png']"
              type="drag"
              :action="uploadUrl">
              <!--<div>--><div>
              <Icon type="camera" size="200"></Icon></div>
              <span style="margin-top:20px;font-size: 16px; font-weight: bold;">摄像头4</span>
            </Upload>
          </Card>
        </div>
        <div v-if="io.length>0" v-for="(item, index) in io" :key="index">
          <Alert v-if="item.io" type="success" style="font-size: 16px">{{item.license + ' 于 ' + item.time + '进入小区' }}</Alert>
          <Alert v-if="!item.io" type="warning" style="font-size: 16px">{{item.license + ' 于 ' + item.time + '离开小区' }}</Alert>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
      data(){
        return {
          license: '',
          io: [],
          uploadUrl: process.env.API + 'admin/upload',
        }
      },
      methods: {
        handleBeforeUpload (file) {
        },
        handleSuccess (res, file) {
          if (res.code===0) {
            this.license = res.data.license;
            console.log(this.license);
            this.io.unshift({license: res.data.license, time: res.data.time, io:true});
            this.$Message.info('识别到车辆'+this.license+'进入小区')
          }
        },
        handleSuccess1 (res, file) {
          if (res.code===0) {
            this.license = res.data.license;
            console.log(this.license);
            this.io.unshift({license: res.data.license, time: res.data.time, io:false});
            this.$Message.warning('识别到车辆'+this.license+'小区')
          }
        },
        handleUploadProgress (e,file) {
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
