import Head from "next/head";
import styles from "@/styles/createMovie.module.css"
import { useState } from "react";

export default function createMovie() {

    const [ formData , setFormData ] = useState(
        {
            name: '',
            releaseDate: '',
            imageURL: '',
            videoURL: '',
            description: ''
        }
    );

    function handleFormEdit(event:any , field:string) {
        setFormData({
            ...formData,
            [field]: event.target.value
        });
    }

    async function formSubmit(event:any) {
        event.preventDefault();
        try {
            const response = await fetch(`/api/action/movie/create`,
                {
                    method: "POST",
                    headers: { 'Content-type' : 'application/json' },
                    body: JSON.stringify(formData)
                }
            );

            const responseJson = await response.json();

            alert(`${responseJson}`);

        }
        catch(err:any) {
            console.log(err);
        }
    }

    return (
        <main id={styles.main} className="flex min-h-screen flex-col">
            <Head>
                <title>Cadastro de Filmes</title>
            </Head>

            <div>
                <form className={styles.formContainer} onSubmit={formSubmit}>
                    <h2 className={styles.registerText}>Cadastrar Filmes</h2>

                    <input id={styles.input} type="text" placeholder="Nome" onChange={(event) => {handleFormEdit(event, 'name')}} />
                    
                    <p>Data de Lançamento</p>
                    <input id={styles.input} type="date" onChange={(event) => {handleFormEdit(event, 'releaseDate')}} />

                    <p>Imagem do filme</p>
                    <input id={styles.input} type="file" accept=".png .jpg . jpeg .jfif" />

                    <br /><input id={styles.input} type="text" placeholder="Link para o trailer do filme (Youtube)" onChange={(event) => {handleFormEdit(event, 'videoURL')}} />

                    <br /><input id={styles.input} type="text" placeholder="Descrição" onChange={(event) => {handleFormEdit(event, 'description')}} />

                    <br /><input id={styles.input} className={styles.sendBtn} type="submit" value="Enviar" />
                </form>
            </div>

        </main>
    );
}