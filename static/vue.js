const vm = new Vue({
  el: "#app",
  delimiters: ["[[","]]"],
  data: {},
  methods: {
    // TODO - Get the X and Y coordinate of the cell that was clicked on. Also retrieve the username that clicked on the cell
    getCellCoords: function(){
      axios({
        method: "get",
        url: "/apis/v1"
      }).then(response => {
        console.log(this.response)
      })
    }
  },
  created: function(){

  }
})
