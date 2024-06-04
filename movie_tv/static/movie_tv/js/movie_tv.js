console.log('js is working')
const hero = Vue.createApp({
    data() {
        return {
            isPopupVisible : false,
            isMiniPopupVisible : {},
            hoverTimeout: null,
            isMovieDetailVisible: {},
            genreFilterVisibility: false
        }
    },
    methods: {
        showPopup(event) {
            event.stopPropagation()
            this.isPopupVisible = true
        },
        hidePopup() {
            this.isPopupVisible = false
        },
        hideMovieDetail(movieId) {
            console.log('You clicked hidemoviedetail')
            if (this.isMovieDetailVisible[movieId]) {
                delete this.isMovieDetailVisible[movieId];
            }
        },
        showMovieDetail(movieId) {
            console.log(`You clicked showmoviedetail, movie: ${movieId}`)
            this.isMovieDetailVisible = {}
            this.isMovieDetailVisible[movieId] = true
        },
        showMiniPopup(movieId) {
            console.log(`You hover and show mini popup, movie ${movieId}`)
            this.isMiniPopupVisible = {};
            this.isMiniPopupVisible[movieId] = true
        },
        handleMovieClick(movieId) {
            console.log(`You hover and show mini popup, movie ${movieId}`)
        },
        hideMiniPopup(movieId) {
            console.log('You hover OUT and HIDE mini popup')
            if (this.isMiniPopupVisible[movieId]) {
                delete this.isMiniPopupVisible[movieId];
            }
        },
        handleMouseOver(movieId) {
            console.log(`You hover and show mini popup, movie ${movieId}`)
            this.hoverTimeout= setTimeout(() => {
                this.showMiniPopup(movieId)
            }, 500)
        },
        handleMouseOut(movieId) {
            clearTimeout(this.hoverTimeout)
            this.hideMiniPopup(movieId)
        },
        handleGenreClick() {
            this.genreFilterVisibility = !this.genreFilterVisibility
        }
    },
    delimiters: ['[[',']]']
})

hero.mount('#hero')

const nav = Vue.createApp({
    data() {
        return {
            searchInputVisibility: 'hidden',
            searchIconVisibility: '',
            isAccountNavVisible: false,
            text:'you reached meeee'
        }
    },
    methods: {
        showSearchInput() {
            this.searchInputVisibility = ''
            this.searchIconVisibility = 'hidden'
        },
        hideSearchInput() {
            console.log('you clicked me')
            if (this.searchInputVisibility === '') {
                this.searchInputVisibility = 'hidden'
                this.searchIconVisibility = ''
            }
        },
        openAccountNav() {
            console.log('you mouseenter on me')
            this.isAccountNavVisible = true
        },
        closeAccountNav() {
            this.isAccountNavVisible = false
        },
        handleAccountClick() {
            this.isAccountNavVisible = !this.isAccountNavVisible
        }
    },
    delimiters: ['[[',']]']
})


// nav.mount('#nav')
