angular.module('Sheetify')
  .controller('HomeController', ['$scope', function ($scope) {
	$scope.test = "this is a test";


	$scope.displayText = "Although the term powder horn is sometimes used for any kind of powder flask, strictly it is a sub-category of flask made from a hollowed bovid horn. Powder flasks were made in a great variety of materials and shapes, though ferrous metals that were prone to give off sparks when hit were usually avoided. Stag antler, which could be carved or engraved, was an especially common material, but wood and copper were common, and in India ivory. Apart from the horns, common shapes were the Y formed by the base of an antler (inverted), a usually flattened pear shape with a straight spout (poire-poudre or powder pear is a French term for these), a round flattened shape, and for larger flasks a triangle with concave rounded sides, which unlike the smaller flasks could be stood upright on a surface. Many designs (such as horn and antler types) have a wide sealed opening for filling, and a thin spout for dispensing. Various devices were used to load a precise amount of powder to dispense, as it was important not to load too much or too little powder, or the powder was dispensed into a powder measure or charger (these survive much less often).[2] As early as c. 1600 a German flask had a silver spout with a "
	$scope.dummyData = 'Although the term powder horn is sometimes used for any kind of powder flask, strictly it is a sub-category of flask made from a hollowed bovid horn. Powder flasks were made in a great variety of materials and shapes, though ferrous metals that were prone to give off sparks when hit were usually avoided.'

	$scope.intelligentData = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text."

	$scope.curNote = ''

	$scope.summerize = function(){
		this.curNote = this.dummyData
	}

	$scope.generate = function(){
		this.curNote = this.displayText
	}
	$scope.fluff = function(){
		this.curNote = this.intelligentData
	}

	$scope.simplify = function(){
		this.curNote = this.dummyData
	}

	$scope.empty = function(){
		this.curNote = ''
	}

  }]);

