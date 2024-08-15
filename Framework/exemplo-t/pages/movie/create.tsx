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

    return (
        <main id={styles.main} className="flex min-h-screen flex-col">
            <Head>
                <title>Cadastro de Filmes</title>
            </Head>

            <div>
                <form className={styles.formContainer}>
                    <h2 className={styles.registerText}>Cadastrar Filmes</h2>

                    <input id={styles.input} type="text" placeholder="Nome" />
                    
                    <p>Data de Lançamento</p>
                    <input id={styles.input} type="date" />

                    <p>Imagem do filme</p>
                    <input id={styles.input} type="file" accept=".png .jpg . jpeg .jfif" />

                    <br /><input id={styles.input} type="text" placeholder="Descrição" />

                    <br /><input id={styles.input} className={styles.sendBtn} type="submit" value="Enviar" />
                </form>
            </div>

        </main>
    );
}