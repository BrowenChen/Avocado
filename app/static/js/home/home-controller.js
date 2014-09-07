angular.module('Sheetify')
  .controller('HomeController', ['$scope', function ($scope) {
	$scope.test = "this is a test";

	$scope.defaultDisplay = ''
	$scope.displayText = "I like to eat tasty, greasy, fat burgers with my cute little,  greasy,  sister who likes fat, greasy, tasty, dogs."
	$scope.summerizeData = "I like to eat tasty, burgers with my cute little sister who likes fat, dogs."
	$scope.dummyData = "I like to eat burgers with my cute little sister who likes dogs."

	$scope.intelligentData = " I enoy running through delicious hamburgers with my precious lilliputian sister who enjoys Canis familiars."

	$scope.curNote = ''


	$scope.avgWord = ''
	$scope.intelligenceLevel = ''
	$scope.errors = ''

	$scope.on = 0

	$scope.summerize = function(){
		this.curNote = this.summerizeData
		this.defaultDisplay = this.summerizeData
	}

	$scope.generate = function(){
		this.curNote = this.displayText
		this.defaultDisplay = this.displayText


		this.avgWord = '87%'
		this.intelligenceLevel = '32%'
		this.errors = '5'

		// TURN ON COLORS
		this.on = 3
	}
	$scope.fluff = function(){
		this.curNote = this.intelligentData
	}

	$scope.simplify = function(){
		this.curNote = this.dummyData
	}

	$scope.empty = function(){
		this.curNote = ''
		this.defaultDisplay = ''
	}



	$scope.save2ever = function() {
		alert("Saved to evernote!")
	}

  }]);

