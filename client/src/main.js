import App from './App.svelte';


const get = ( url ) => fetch( url ).then( r => r.text() );
const post = ( url, data ) => fetch( url, {
    method: "POST",
    body: typeof data === "string" ? data : JSON.stringify( data )
} ).then( r => r.text() );



export default new App( {
    target: document.querySelector( '#app' ),
    props: {
        _GET: get,
        _POST: post
    }
} );
