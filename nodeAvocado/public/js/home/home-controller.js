angular.module('Sheetify')
  .controller('HomeController', ['$scope', function ($scope) {
	$scope.test = "this is a test";

	$scope.defaultDisplay = ''
	$scope.displayText = "They emphasize two distinctions: do activities involve immediate costs or immediate rewards, and are people sophisticated or naive about future self-control problems? Naive people procrastinate immediate-cost activities and preproperate--do too soon--immediate-reward activities. Sophistication mitigates procrastination but exacerbates preproperation. Moreover, with immediate costs, a small present bias can severely harm only naive people, whereas with immediate rewards it can severely harm only sophisticated people. Lessons for savings, addiction, and elsewhere are discussed."
	$scope.summerizeData = "I like to eat tasty, burgers with my cute little sister who likes fat, dogs. "                     
	$scope.dummyData = "Do activities involve immediate costs or immediate rewards, and are people sophisticated or naive about future self-control problems? Naive people procrastinate immediate-cost activities and preproperate--do too soon--immediate-reward activities."
	$scope.intelligentData = " Do action ask quick be or quick wages, and ar mass twist or naif some next willpower job? Naif mass stall immediate-cost action and preproperate--do too soon--immediate-reward action. Sophism palliate cunctation but worsen preproperation. "

	// $scope.displayText = "I like to eat tasty, greasy, fat burgers with my cute little,  greasy,  sister who likes fat, greasy, tasty, dogs."
	// $scope.summerizeData = "I like to eat tasty, burgers with my cute little sister who likes fat, dogs."
	// $scope.dummyData = "I like to eat burgers with my cute little sister who likes dogs."
	$scope.intelligentDog= " I enoy running through delicious hamburgers with my precious lilliputian sister who enjoys Canis familiars."



	$scope.curNote = ''


	$scope.avgWord = ''
	$scope.intelligenceLevel = ''
	$scope.errors = ''

	$scope.on = 0

	$scope.summerize = function(){
		this.curNote = this.intelligentDog
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

