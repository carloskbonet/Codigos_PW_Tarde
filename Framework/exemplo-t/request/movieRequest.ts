import { checkMinMaxLength } from "./check";

export function movieRequest(_name:any , _releaseDate:any, _link:any , _description:any) {

    if ( !checkMinMaxLength(_name , 1 , 32 ) ){
        return { response: false , message: 'Nome inválido' };
    }

    //  Formato aceito: 2024-09-19
    if ( !checkMinMaxLength(_releaseDate , 10 , 10 ) ) {
        return { response: false , message: 'Data inválida' };
    }
    
    if ( !checkMinMaxLength(_link, 5 , 10) ) {
        return { response: false , message: 'Link inválido. Digite apenas o código do video.' };
    }

    if ( !checkMinMaxLength(_description , 0 , 1000) ) {
        return { response: false , message: 'Descrição Inválida. Limite de 1000 caracteres' };
    }

    return { response: true }
}