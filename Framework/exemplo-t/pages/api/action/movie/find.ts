import { NextApiRequest , NextApiResponse } from "next";
import { findMovieByNameC } from "../../controller/movieController";

export default async ( req:NextApiRequest , res:NextApiResponse ) => {
    if ( req.method != 'GET' ) {
        return res.status(403).json({ message: 'Method not allowed' });
    }

    const {name}:any = req.query;

    // Enviar para o controller
    const response = await findMovieByNameC(name);

    if ( response.status == 200 ) {
        return res.status(response.status).json( { message: response.message , data: response.data } )
    }
    else {
        return res.status(response.status).json( { message: response.message } )
    }
}