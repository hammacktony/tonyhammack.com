(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d237cc7"],{fd3f:function(t,e,a){"use strict";a.r(e);var s=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"blog"},["personal"==t.$route.params.blog?a("custom-header",{attrs:{heading:"My "+t.$route.params.blog+" Blog",image:t.personalImage}}):"technical"==t.$route.params.blog?a("custom-header",{attrs:{heading:"My "+t.$route.params.blog+" Blog",image:t.technicalImage}}):a("custom-header",{attrs:{heading:t.heading,subheading:t.subheading,image:t.otherImage}}),a("div",{staticClass:"col-lg-8 col-md-9 mx-auto"},[a("div",{staticClass:"post-preview",staticStyle:{"text-align":"center"},attrs:{id:"posts"}},t._l(t.posts,function(t){return a("div",[a("post-description",{attrs:{title:t.title,slug:t.slug,date:t.created_at}}),a("hr")],1)}),0)])],1)},o=[],n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{attrs:{id:"post-description"}},[a("router-link",{attrs:{to:{name:"blog-post",params:{blog:t.$route.params.blog,slug:t.slug}}}},[a("h2",{staticClass:"post-title post"},[t._v(t._s(t.title))])]),a("p",{staticClass:"post-meta"},[t._v("Posted by Tony Hammack on "+t._s(t._f("moment")(t.date,"dddd, MMMM Do YYYY")))])],1)},i=[],l={name:"PostDescription",props:{blog:String,title:String,slug:String,date:String}},r=l,c=a("2877"),g=Object(c["a"])(r,n,i,!1,null,null,null),p=g.exports,u=a("bc3a");function d(t){return"http://localhost:8000/api/blog/"+t}var h={components:{"post-description":p},data:function(){return{heading:"Excuse Me...",subheading:"Sorry, that page does not exist.",personalImage:"blog/img/blog-header.jpg",technicalImage:"blog/img/laptop-blog.jpg",otherImage:"blog/img/glitch.png",posts:[]}},created:function(){this.fetchData()},watch:{$route:"fetchData"},methods:{fetchData:function(){var t=this,e=d(this.$route.params.blog);u.get(e).then(function(e){t.posts=e.data}).catch(function(t){console.log(t)})}}},m=h,b=Object(c["a"])(m,s,o,!1,null,null,null);e["default"]=b.exports}}]);
//# sourceMappingURL=chunk-2d237cc7.e21820e6.js.map