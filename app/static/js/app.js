// Declare app level module which depends on filters, and services
angular.module('Sheetify', ['ngResource', 'ngRoute', 'ui.bootstrap', 'ui.date'])
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/home/home.html', 
        controller: 'HomeController'})

      .when('/register', {
		templateUrl: 'views/home/register.html',
		controller: 'HomeController'
      })
      .when('/interface', {
        templateUrl: 'views/home/interface.html',
        controller: 'HomeController'
      })
      .when('/review', {
        templateUrl: 'views/home/review.html',
        controller: 'HomeController'
      })
      .otherwise({redirectTo: '/'});
  }]);
