import { createUser, findUserByEmail, findUserByUsername } from '../model/user';

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