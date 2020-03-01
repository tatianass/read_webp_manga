myapp.controller('MainCtrl', function ($scope) {
    $scope.showContent = function($fileContent){
        $scope.paths = $fileContent.split(',');
        $scope.split_chapter = '/mg/'
        
        $scope.goChapter = function (choosen_chapter) {
        	document.getElementById(choosen_chapter).scrollIntoView();
        }

        $scope.goTop = function (){
        	document.body.scrollTop = 0; // For Safari
  			document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
        }
    };
});