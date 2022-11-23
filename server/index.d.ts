export interface BunRequest {
    method: string;
    request: Request;
    path: string;
    header?: { [key: string]: any };
    params?: { [key: string]: any };
    query?: { [key: string]: any };
    body?: { [key: string]: any };
    blob?: any;
}
export interface BunResponse {
    status (code: number): BunResponse;
    option (option: ResponseInit): BunResponse;
    statusText (text: string): BunResponse;
    json (body: any): void;
    send (body: any): void;
    setHeader (key: string, value: any);
    headers (header: HeadersInit): BunResponse;
    getResponse (): Response;
    getHeader (); //this.options.headers;
    isReady (): boolean; //turn!!this.response;
}