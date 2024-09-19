import { isEmail , checkMinMaxLength } from "./check";


export function userRequest(_name:any , _email:any , _username:any , _password:any, _confirmPassword:any) {

    // usar o simbolo ! é equivalente a "== false" no final da expressão.
    if ( !checkMinMaxLength(_name , 3 , 25) ) {
        return { response: false , message: 'Nome inválido' };
    }

    if ( !isEmail(_email) ) {
        return { response: false , message: 'Email inválido' };
    }

    if ( !checkMinMaxLength(_username , 6 , 15) ) {
        return { response: false , message: 'Username inválido' };
    }

    if ( !checkMinMaxLength(_password, 8 , 32) ) {
        return { response: false, message: 'Senha inválida' };
    }

    if ( !checkMinMaxLength(_confirmPassword , 8 , 32) ) {
        return { response: false , message: 'Segunda senha inválida' };
    }

    return { response: true };

}