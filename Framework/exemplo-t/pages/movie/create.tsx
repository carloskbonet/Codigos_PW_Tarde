import Head from "next/head";
import styles from "@/styles/createMovie.module.css"
import { useEffect, useState } from "react";
import Navbar from "@/components/Navbar";
import Layout from "@/components/Layout";
import Link from "next/link";

export default function createMovie() {

    const [imageUpload, setImageUpload] = useState(undefined);

    // Armazena os generos de filmes recebidos do banco de dados
    const [genres, setGenres]: any = useState(undefined);

    // Armazena os generos SELECIONADOS
    var selectedGenres: Array<string> = [];

    const [formData, setFormData] = useState(
        {
            name: '',
            releaseDate: '',
            imageURL: '',
            videoURL: '',
            description: ''
        }
    );

    function handleCheckboxEdit(event: any, name: string) {
        if (event.target.checked) {
            selectedGenres.push(name);
        }
        else {
            const index = selectedGenres.indexOf(name);

            if (index != undefined)
                selectedGenres.splice(index, 1);
        }
    }

    async function fetchData() {
        try {
            const response = await fetch(`/api/action/genre/select`, {
                method: 'GET'
            });

            const responseJson = await response.json();

            setGenres(responseJson.data);

        }
        catch (err) {
            console.log(err);
        }
    }

    useEffect(() => {
        fetchData();

    }, []);

    function handleImageEdit(event: any) {
        setImageUpload(event.target.files[0]);
    }

    function handleFormEdit(event: any, field: string) {
        setFormData({
            ...formData,
            [field]: event.target.value
        });
    }

    async function formSubmit(event: any) {
        event.preventDefault();

        if (imageUpload == undefined) {
            movieSubmit(event);
            return;
        }

        try {
            const img = new FormData();
            img.append("image", imageUpload);

            const response = await fetch(`/api/action/movie/createImage`, {
                method: 'POST',
                body: img
            });

            const responseJson = await response.json();

            if (response.status != 200) {
                alert(responseJson.message);
            }
            else {
                // criar o filme

                movieSubmit(event, responseJson.secure_url);
            }
        }
        catch (err) {
            alert(err);
        }
    }

    async function movieSubmit(event: any, img = "") {
        event.preventDefault();
        try {
            const response = await fetch(`/api/action/movie/create`,
                {
                    method: "POST",
                    headers: { 'Content-type': 'application/json' },
                    body: JSON.stringify({
                        name: formData.name,
                        releaseDate: formData.releaseDate,
                        description: formData.description,
                        videoURL: formData.videoURL,
                        imageURL: img,
                        genres: selectedGenres
                    })
                }
            );

            const responseJson = await response.json();

            alert(`${responseJson.message}`);

        }
        catch (err: any) {
            alert(err);
        }
    }

    return (
        <main id={styles.main} className="flex min-h-screen flex-col">
            <Head>
                <title>Cadastro de Filmes</title>
            </Head>

            <Navbar>
                
            </Navbar>

            <div>

                <form className={styles.formContainer} onSubmit={formSubmit}>
                    <h2 className={styles.registerText}>Cadastrar Filmes</h2>

                    <input id={styles.input} type="text" placeholder="Nome" onChange={(event) => { handleFormEdit(event, 'name') }} />

                    <p>Data de Lançamento</p>
                    <input id={styles.input} type="date" onChange={(event) => { handleFormEdit(event, 'releaseDate') }} />

                    <p>Imagem do filme</p>
                    <input id={styles.input} type="file" accept=".png .jpg . jpeg .jfif" onChange={handleImageEdit} />

                    <br /><input id={styles.input} type="text" placeholder="Link para o trailer do filme (Youtube)" onChange={(event) => { handleFormEdit(event, 'videoURL') }} />

                    <br /><input id={styles.input} type="text" placeholder="Descrição" onChange={(event) => { handleFormEdit(event, 'description') }} />


                    <div>

                        {
                            genres != undefined && genres instanceof Array ?

                                genres.map(genre => (

                                    <div className={styles.checkboxBox}>
                                        <input type="checkbox" onChange={(e) => { handleCheckboxEdit(e, genre.name) }} />
                                        <label>{genre.name}</label>
                                    </div>

                                ))

                                :

                                <p>No genres</p>
                        }

                    </div>


                    <br /><input id={styles.input} className={styles.sendBtn} type="submit" value="Enviar" />
                </form>
            </div>

        </main>
    );
}