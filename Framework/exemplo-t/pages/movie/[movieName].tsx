import styles from '@/styles/movie.module.css'
import { useState , useEffect } from 'react';

export default function movie({ movieName }: any) {
    const [ data , setData ]:any = useState(undefined);

    async function fetchData() {
        try {
            const response = await fetch(`/api/action/movie/find?name=` +movieName , {
                method: 'GET'
            });

            const responseJson = await response.json();

            setData(responseJson.data);
        }
        catch (err) {
            console.log(err);
            alert('Algo deu Errado');
        }
    }

    useEffect(() => {

        fetchData();

    }, [])

    return (
        <main id={styles.main} className="flex min-h-screen flex-col">
            { 
            data !=  undefined ?

            <div className={styles.page}>
                <div className={styles.movie}>
                    <img src={data.imageURL} alt="" className={styles.img} />
                    <div className={styles.movieInfos}>
                        <h2>{data.name}</h2>
                        <p>{data.releaseDate}</p>
                        <p>{data.description}</p>
                        <p>Generos</p>
                    </div>
                </div>

                <iframe className={styles.video} height="350" src={`https://www.youtube.com/embed/`+data.videoURL}>
                </iframe>

                <div className={styles.formRating}>
                    <h2>Digite uma nota (0 a 5)</h2>
                    <input className={styles.value} type="number" value='0' /><br />
                    <textarea className={styles.comment} placeholder='Digite seu Comentário' ></textarea><br />
                    <input className={styles.submitBtn} type="submit" />

                </div>
            </div>

            :

            <p>Erro 404 Filme não encontrado</p>

            }
        </main>
    );
}


export function getServerSideProps(context: any) {

    const { movieName } = context.query;

    return {
        props: { movieName }
    }
}