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