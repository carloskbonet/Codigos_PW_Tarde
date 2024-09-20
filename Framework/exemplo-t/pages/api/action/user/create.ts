import { NextApiRequest , NextApiResponse } from "next";
import { createUserC } from "../../controller/userController";
import { userRequest } from "@/request/userRequest";

export default async ( req:NextApiRequest , res:NextApiResponse ) => {
    if ( req.method != 'POST' ) {
        return res.status(405).json({ message: 'Method not allowed' });
    }

    const { name , email , username , password , cPassword } = req.body;

    // Aplicar request

    const checkRequest = userRequest(name , email , username , password , cPassword);

    if ( checkRequest.response == false ) {
        return res.status(400).json( { message: checkRequest.message } );
    }


    // Enviar para o controller
    const response = await createUserC(name , email , username , password , cPassword);

    return res.status(response.status).json( { message: response.message } );
}