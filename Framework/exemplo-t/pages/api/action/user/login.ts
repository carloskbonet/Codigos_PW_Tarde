import { NextApiRequest , NextApiResponse } from "next";
import { login } from "../../controller/userController";

export default async ( req:NextApiRequest , res:NextApiResponse ) => {
    if ( req.method != 'GET' ) {
        return res.status(403).json({ message: 'Method not allowed' });
    }

    const { email , password } = req.body;

    // Enviar para o controller
    const response = await login(email , password);

    if ( response.status == 200 ) {
        return res.status( response.status ).json( { message: response.message , token: response.token } );
    }
    else {
        return res.status( response.status ).json( { message: response.message } );
    }
}