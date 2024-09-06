import { NextApiRequest , NextApiResponse } from "next";
import { createRating } from "../../controller/ratingController";

export default async ( req:NextApiRequest , res:NextApiResponse ) => {
    if ( req.method != 'POST' ) {
        return res.status(405).json({ message: 'Method not allowed' });
    }

    const { value , comment , email , movieName } = req.body;

    // Validar
    if ( value < 0 || value > 5 ) {
        return res.status(400).json( { message: 'Invalid value' } );
    }

    // Enviar para o controller

    const response = await createRating(value , email , movieName , comment);

    return res.status(response.status).json( { message: response.message } );
}