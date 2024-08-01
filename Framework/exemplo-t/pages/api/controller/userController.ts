import { createUser, findUserByEmail, findUserByUsername, findUserLogin } from '../model/user';
import { generateToken } from '@/services/tokenConfig';

export async function createUserC(_name:string , _email:string , _username:string , _password:string, _cPassword:string) {
    try {
        
        // Verificações do controller
        if ( _password != _cPassword ) {
            return { status: 400 , message: 'passwords dont match' };
        }

        // Verificar atributos únicos
        const userByEmail = await findUserByEmail(_email);

        if ( userByEmail != undefined ) {
            return { status: 403 , message: 'Email already registered' };
        }

        const userByUsername = await findUserByUsername(_username);

        if ( userByUsername != undefined ) {
            return { status: 403 , message: 'Username already registered' };
        }

        // Criar a Model
        const user = await createUser(_name , _email , _username , _password);

        return { status: 201 , message: 'User created', data: user };

    }
    catch (err) {
        return { status: 500, message: 'Something went wrong' };
    }
}


export async function login(_email:string , _password:string) {
    try {
        const userLogin = await findUserLogin(_email , _password);

        if ( userLogin == undefined ) {
            return { status: 404, message: 'Incorrect Email or Password' };
        }
        else {
            const _token = generateToken(_email);

            return { status: 200, message: 'Logged In', token: _token };
        }
    }
    catch(err) {
        return { status: 500, message: 'Something went wrong' };
    }
}