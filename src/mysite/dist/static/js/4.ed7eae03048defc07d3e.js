webpackJsonp([4],{ToOk:function(t,e){},TsOZ:function(t,e,a){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n={components:{Mypagination:a("ZILr").a},data:function(){return{input:"",total:2,pageSize:1,tableData:[{question_title:"On one of her trips to New York several years ago, Eudora Welty decided to take a couple of New York friends out to dinner. They settled in at a comfortable East Side cafe and within minutes, another customer was approaching their table.",question_number:"20"}]}},methods:{handleEdit:function(){},handleDelete:function(){}}},i={render:function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"total"},[t._m(0),t._v(" "),a("div",{staticClass:"user"},[a("div",{staticClass:"userheader"},[a("el-input",{attrs:{placeholder:"请输入内容"},model:{value:t.input,callback:function(e){t.input=e},expression:"input"}}),t._v(" "),a("el-button",{attrs:{type:"primary"}},[t._v("查询")]),t._v(" "),a("el-button",{attrs:{type:"primary"}},[t._v("添加")])],1),t._v(" "),a("div",{staticClass:"wrapper"},[a("el-table",{staticStyle:{width:"100%"},attrs:{border:"",data:t.tableData}},[a("el-table-column",{attrs:{type:"selection",width:"55"}}),t._v(" "),a("el-table-column",{attrs:{prop:"question_title",label:"题目名称",width:"900"}}),t._v(" "),a("el-table-column",{attrs:{prop:"question_number",label:"所含小题数量",width:"180"}}),t._v(" "),a("el-table-column",{attrs:{prop:"operate",label:"操作"},scopedSlots:t._u([{key:"default",fn:function(e){return[a("el-button",{attrs:{size:"mini"},on:{click:function(a){return t.handleEdit(e.$index,e.row)}}},[t._v("编辑")]),t._v(" "),a("el-button",{attrs:{size:"mini",type:"danger"},on:{click:function(a){return t.handleDelete(e.$index,e.row)}}},[t._v("删除")])]}}])})],1)],1),t._v(" "),a("div",[a("Mypagination",{attrs:{total:t.total,pageSize:t.pageSize}})],1)])])},staticRenderFns:[function(){var t=this.$createElement,e=this._self._c||t;return e("div",{staticClass:"title1"},[e("h4",[this._v("首页/题库管理/阅读理解")])])}]};var r=a("VU/8")(n,i,!1,function(t){a("ToOk")},"data-v-5717ab6b",null);e.default=r.exports}});
//# sourceMappingURL=4.ed7eae03048defc07d3e.js.map