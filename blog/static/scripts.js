/**
 * Created by Owner on 6/24/2014.
 */
function callAjax(){
    $.ajax({
        cache :false,
        url:"/sayhello/",
        success: function(data){
            gems=(data.content);
        }
    });
}
$(document).ready(function(){
    callAjax();
});

(function() {
  var app = angular.module('blogModule', []);

    app.factory('blogPosts', function($http){
        return {
            get : function(params){return $.ajax('/sayhello/', {
                   data : params
                });}

        }
});

  app.directive('blogPosts', function($http,blogPosts){

    blogPosts.get({
        id : '0'
    }).then(function(response){
        console.log(response)
        posts=response.content.posts;
    })
    return {
        controller: function() {
            this.posts=posts;
          this.current = 1;
          this.setCurrent = function(imageNumber){
            this.current = imageNumber || 0;
          };
        },
        templateUrl: "/static/posts.html",
        restrict:'E',
        controllerAs: "postHolder"

    };

  });

  var gems = [
    { name: 'Azurite', price: 2.95 },
    { name: 'Bloodstone', price: 5.95 },
    { name: 'Zircon', price: 3.95 },
    { name: 'Zircon', price: 3.95 },
    { name: 'Zircon', price: 3.95 },
    { name: 'Zircon', price: 3.95 },
    { name: 'Zircon', price: 3.95 },
    { name: 'Zircon', price: 3.95 },
  ];
})();