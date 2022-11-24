export const funcs = Object.freeze( [
    { id: 1, text: "Translate" },
    { id: 2, text: "Transcribe" },
] );
export const langs = Object.freeze( [
    { id: 1, text: "Hindi" },
    { id: 2, text: "Bengali" },
] );

export const ider = () => ( +new Date() ).toString( 36 );
const yt2std = ( url ) => {
    let id;
    if ( url.includes( "youtube.com" ) )
        id = url.split( "v=" )[ 1 ].split( "&" )[ 0 ];
    else if ( url.includes( "youtu.be" ) )
        id = url.split( "tu.be" )[ 1 ].split( "/" )[ 1 ];

    return `https://youtube.com/watch?v=${ id }`;
}

export const YT = {
    toURL: yt2std
}

export const ws = new WebSocket( "ws://localhost:3000/" );