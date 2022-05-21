import Vue from 'vue'
import Router from 'vue-router'
import Signin from '@/components/auth/Signin'
import SignUp from '@/components/auth/SignUp'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/auth/signin/',
      name: 'Signin',
      component: Signin
    },
    {
      path: '/auth/signup',
      name: 'SignUp',
      component: SignUp
    }
  ]
})
