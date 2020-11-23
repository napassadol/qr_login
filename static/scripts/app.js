var app = angular.module("myApp", ["ngRoute"]);

app.config(['$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
}]);

app.controller('loginCtrl', function($scope, $http) {
    var vm = this
    vm.user = {}

    vm.login = function(){
        $http.post("/login", vm.user).then(function (response) {
            console.log(response.data)
            if(response.data.status == true){
                window.location.href = "/room"
            }
            else{
                alert("login fail")
            }
        });
    }

    vm.register = function(){
        window.location.href = "/register"
    }
});

app.controller('registerCtrl', function($scope, $http) {
    var vm = this
    vm.user = {}

    vm.register = function(){
        if(vm.user.password != vm.user.confirm_password){
            alert("password not match")
        }
        $http.post("/send_register", vm.user).then(function (response) {
            console.log(response.data)
            if(response.data.id != undefined){
                alert("register success")
                window.location.href = "/"
            }
            else{
                alert("register fail")
            }
        });
    }
});

app.controller('roomCtrl', function($scope, $http) {
    var vm = this
    vm.user = {}

    checkAdmin()

    function checkAdmin(){
        $http.post("/check_admin").then(function (response) {
            console.log(response.data)
            vm.admin = response.data.admin
        });
    }

    vm.logout = function(){
        $http.post("/logout").then(function (response) {
            console.log(response.data)
            window.location.href = "/"
        });
    }

    vm.editRoom = function(){
        window.location.href = "/edit_room"
    }
});

app.controller('roomEditCtrl', function($scope, $http) {
    var vm = this
    vm.user = {}

    
});
