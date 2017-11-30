 $(document).ready(function(){
	$('#exampleModal').on('show.bs.modal', function (event) {
		var button = $(event.relatedTarget)
		var recipient = button.data('whatever') 
		var modal = $(this)
		// modal.find('.modal-title').text('New message to ' + recipient)
		modal.find('.modal-body input').val(recipient)
	  })
   
    $("#btns").click(function(){
     alert('p');
    });
});
		
		
		var urlMovies     = 'http://localhost:8000/movies';
		var urlRentMovies = 'http://localhost:8000/rentmovies/';
		var urlRentedMovies = 'http://localhost:8000/returnmovie/';
		

	new Vue({
			el: '#main',
			mounted: function() {
				this.getMovies();
				this.getRentedMovies();
			},
			data: function () {
				return {
					lists: [],
					rented_movies_lists : [],
					current_item : {}
				}
			},
			methods: {
				showModal : function(item){
					this.current_item = item;
					$('#exampleModal').modal();
				},
				getRentedMovies : function(){
					axios.get(urlRentedMovies).then(res => {
						this.rented_movies_lists = res.data;
					})
				},
				getMovies: function() {
					axios.get(urlMovies).then(res => {
						this.lists = res.data;
						console.log(this.lists);

						this.lists.map((item) => item.Quantity = 1);
					});
				},
				rentmovies: function (item) {
					axios.post(urlRentMovies, item).then(res => {
						// aqui tienes tu respuesta
						console.log(res.data)
					}).catch(console.error)
				}
			}
		});