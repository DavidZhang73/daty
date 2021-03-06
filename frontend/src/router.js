import Vue from 'vue'
import Router from 'vue-router'

import Home from './views/Home'
import About from './views/About'

import User from './views/user/User'
import Login from './views/user/Login'
import Signin from './views/user/Signin'
import EmailCheck from './views/user/EmailCheck'
import SigninSuccess from './views/user/SigninSuccess'
import ForgetPassword from './views/user/ForgetPassword'
import ForgetPasswordReset from "./views/user/ForgetPasswordReset"
import ForgetPasswordResetSuccess from './views/user/ForgetPasswordResetSuccess'

import Center from './views/center/Center'
import CollectionList from './views/center/CollectionList'
import AddNewCollection from './views/center/AddNewCollection'
import EditCollection from './views/center/EditCollection'
import FileUploadAndDownload from './views/center/FileUploadAndDownload'
import GroupList from './views/center/GroupList'
import UserInfo from './views/center/UserInfo'
import UserPassword from './views/center/UserPassword'
import AddNewGroup from './views/center/AddNewGroup'
import EditUserGroup from './views/center/EditUserGroup'

import NotFound from './views/NotFound'

Vue.use(Router);

export default new Router({
    mode: 'hash',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/about',
            name: 'about',
            component: About
        },
        {
            path: '/user',
            component: User,
            children: [
                {
                    path: 'login',
                    name: 'login',
                    component: Login,
                },
                {
                    path: 'signin',
                    name: 'signin',
                    component: Signin
                },
                {
                    path: 'emailCheck',
                    name: 'emailCheck',
                    component: EmailCheck
                },
                {
                    path: 'signinSuccess',
                    name: 'signinSuccess',
                    component: SigninSuccess
                },
                {
                    path: 'forgetPassword',
                    name: 'forgetPassword',
                    component: ForgetPassword,
                },
                {
                    path: 'forgetPassword/reset/:uuid',
                    name: 'forgetPasswordReset',
                    component: ForgetPasswordReset,
                },
                {
                    path: 'forgetPassword/resetSuccess',
                    name: 'forgetPasswordResetSuccess',
                    component: ForgetPasswordResetSuccess,
                },
            ]
        },
        {
            path: '/center',
            component: Center,
            children: [
                {
                    path: 'collectionList',
                    name: 'collectionList',
                    component: CollectionList
                },
                {
                    path: 'addNewCollection',
                    name: 'addNewCollection',
                    component: AddNewCollection
                },
                {
                    path: 'editCollection/:id',
                    name: 'editCollection',
                    component: EditCollection,
                    props: true
                },
                {
                    path: 'fileUploadAndDownload/:id',
                    name: 'fileUploadAndDownload',
                    component: FileUploadAndDownload,
                    props: true
                },
                {
                    path: 'groupList',
                    name: 'groupList',
                    component: GroupList,
                },
                {
                    path: 'editUserGroup/:id',
                    name: 'editUserGroup',
                    component: EditUserGroup,
                    props: true,
                },
                {
                    path: 'addNewGroup',
                    name: 'addNewGroup',
                    component: AddNewGroup,
                },
                {
                    path: 'userInfo',
                    name: 'userInfo',
                    component: UserInfo
                },
                {
                    path: 'userPassword',
                    name: 'userPassword',
                    component: UserPassword
                }
            ]
        },
        {
            path: '*',
            name: 'notfound',
            component: NotFound
        }

    ]
})
