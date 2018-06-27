<template>
  <div class="login" style="position: relative;">
    <div class="flex flex-center" style="margin: 7% auto 20px auto;position: relative;">
      <Card class="form" style="position: relative">
        <div class="title flex flex-pack-justify">
          <span style="margin-top: -15px;font-size: 20px; color: #000; font-weight: bold">管理端</span>
          <div v-if="!signflag">
            用户登录
          </div>
          <div v-else>
            用户注册
          </div>
        </div>
        <div>
        <Form v-if="!signflag">
          <FormItem label="账号">
          <Input @on-enter="login" class="" v-model="login_form.user" size="large"  placeholder="帐号" style="width: 250px">
          </Input>
          </FormItem>
          <FormItem label="密码" style="margin-top: 39px">
          <Input @on-enter="login" class="" type="password" v-model="login_form.pw" size="large"  placeholder="密码" style="width: 250px;">
          </Input>
          </FormItem>
        </Form>
        <Form v-else :label-width="80">
          <FormItem label="用户名">
            <Input @on-enter="login" class="" v-model="sign_form.user_name" size="large"  placeholder="帐号" style="width: 250px">
            <!--<Icon type="ios-person-outline" slot="prepend"></Icon>-->
            </Input>
          </FormItem>
          <FormItem label="真实姓名" style="margin-top: 20px">
            <Input @on-enter="login" class="" v-model="sign_form.true_name" size="large"  placeholder="密码" style="width: 250px;">
            </Input>
          </FormItem>
          <FormItem label="联系方式" style="margin-top: 20px">
            <Input @on-enter="login" class="" v-model="sign_form.telephone" size="large"  placeholder="密码" style="width: 250px;">
            </Input>
          </FormItem>
          <FormItem label="密码" style="margin-top: 20px">
            <Input @on-enter="login" class="" type="password" v-model="sign_form.pw" size="large"  placeholder="密码" style="width: 250px;">
            </Input>
          </FormItem>
          <FormItem label="重新输入" style="margin-top: 20px">
            <Input @on-enter="login" class="" type="password" v-model="sign_form.r_pw" size="large"  placeholder="密码" style="width: 250px;">
            </Input>
          </FormItem>
        </Form>
        </div>
        <div>
          <Button v-if="!signflag" @click="login" type="primary" class="login-button">登录</Button>
          <Button v-else @click="sign" type="primary" class="login-button">提交</Button>
          <Button @click="signflag = !signflag; init()" type="ghost" class="login-button"><span>{{ signflag && '返回' || '注册'}}</span></Button>
        </div>
      </Card>
    </div>

  </div>
</template>

<script>
  export default {
    data() {
      return {
        login_form: {
          user: '',
          pw: '',
        },
        sign_form: {
          user_name: '',
          true_name: '',
          telephone: '',
          pw: '',
          r_pw: '',
        },
        signflag: false,
      };
    },
    mounted: function () {
      // this.loadCaptcha()
    },
    methods: {
      init: function () {
        this.login_form = {
          user: '',
            pw: '',
        };
        this.sign_form = {
          user_name: '',
          true_name: '',
          telephone: '',
          pw: '',
          r_pw: '',
        };
      },
      login: function () {
        // this.$router.push('/home')
        if (this.login_form.user && this.login_form.pw) {
          this.ajax.post('/admin/login',{
            name: this.login_form.user,
            password: this.login_form.pw,
          }).then(response => {
            if (response.data.code===0 && response.data.data.role === 'ADMIN'){
              this.$store.commit('setUser', response.data.data);
              this.$router.push('/home');
            }
            else {
              this.$Message.error('密码错误');
            }
          });
        } else {
          this.$Message.error('请输入用户名密码');
        }
      },
      sign: function () {
        if (this.sign_form.user_name && this.sign_form.pw && this.sign_form.telephone && this.sign_form.r_pw === this.sign_form.r_pw) {
          this.ajax.post('/admin/sign_in',{
            name: this.sign_form.user_name,
            password: this.sign_form.pw,
            phone: this.sign_form.telephone,
            role: 'ADMIN',
          }).then(response => {
            if (response.data.code===0){
              this.signflag = !this.signflag;
              this.$Message.succeed('注册成功');
              this.init();
            }
          });
        } else {
          this.$Message.error('注册失败')
        }
      },

    }
  };
</script>

<style lang="less">
  .captcha-div {
    img {
      height: 50px;
    }
    button {
      margin-bottom: 24px;
      margin-left: 10px;
    }
    position: absolute;
    right: 39px;
    top: 260px;
  }
</style>
