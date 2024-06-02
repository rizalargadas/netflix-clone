console.log('js is working')
const hero = Vue.createApp({
    data() {
        return {
            isPopupVisible : false,
            isMiniPopupVisible : {},
            message: 'you reached me',
            hoverTimeout: null,
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
        showMiniPopup(movieId) {
            console.log(`You hover and show mini popup, movie ${movieId}`)
            // event.stopPropagation()
            this.isMiniPopupVisible = {};
            this.isMiniPopupVisible[movieId] = true
        },
        hideMiniPopup(movieId) {
            console.log('You hover OUT and HIDE mini popup')
            if (this.isMiniPopupVisible[movieId]) {
                delete this.isMiniPopupVisible[movieId];
            }
        },
        handleMouseOver(movieId) {
            this.hoverTimeout= setTimeout(() => {
                this.showMiniPopup(movieId)
            }, 500)
        },
        handleMouseOut(movieId) {
            clearTimeout(this.hoverTimeout)
            this.hideMiniPopup(movieId)
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
