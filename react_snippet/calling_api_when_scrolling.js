  componentDidMount: function () {
    window.addEventListener('scroll', this.handleScroll)
  },

  handleScroll:function (e) {
    // var totalScrolled =
    // $(window).scrollTop() + $(window).innerHeight
    // if (totalScrolled + 1 > $(window).height()) {
    //   this.loadMoreSubCampaignsWhileScrolling()
    // }
    console.log("window height", $(window).height());
    console.log("scrollTop", $(window).scrollTop());

    var totalScrolled = $(window).height() + $(window).scrollTop();
    var documentHeight =   $(document).height() - 1 ; //this 1 is kind of important
    console.log("totalScrolled", totalScrolled);
    console.log("documentHeight", documentHeight);
    if(totalScrolled > documentHeight) {
        //make api call or do other stuff
      //this.props.campaignsActions.getNewSubCampaigns();
    }
