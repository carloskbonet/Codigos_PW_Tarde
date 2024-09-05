import { checkToken } from '@/services/tokenConfig';
import styles from '@/styles/movie.module.css'
import { getCookie } from 'cookies-next';
import { useState , useEffect } from 'react';

export default function movie({ movieName }: any) {

    // Formulário de avaliação
    const [ ratingForm , setRatingForm ] = useState(
        {
            value: 0,
            comment: ''
        }
    );

    const [ data , setData ]:any = useState(undefined);


    function handleFormEdit(event:any , field:string) {
        setRatingForm({
            ...ratingForm,
            [field] : event.target.value
        });
    }

    async function formSubmit(e:any) {
        e.preventDefault();

        try {
            const cookieAuth = getCookie('authorization');

            const tokenInfos = checkToken(cookieAuth);


            const response = await fetch(`/api/action/rating/create`, {
                method: 'POST',
                headers: { 'Content-type' : 'application/json' },
                body: JSON.stringify({
                    value: Number(ratingForm.value),
                    comment: ratingForm.comment,
                    email: tokenInfos.email,
                    movieName: movieName
                })
            });

            const responseJson = await response.json();

            alert(responseJson.message);

        }
        catch (err) {
            console.log(err);
            alert(err);
        }
    }


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

                <form className={styles.formRating} onSubmit={formSubmit}>
                    <h2>Digite uma nota (0 a 5)</h2>
                    <input onChange={(e) => { handleFormEdit(e , 'value') }} className={styles.value} type="number"/><br />
                    <textarea onChange={(e) => { handleFormEdit(e , 'comment') }} className={styles.comment} placeholder='Digite seu Comentário' ></textarea><br />
                    <input className={styles.submitBtn} type="submit" />

                </form>

                <div className={styles.ratings}>
                    <div className={styles.ratingCard}>
                        <label className={styles.rValue}>4/5 Recomendação</label><br />
                        <label className={styles.rUser}>[] User 1</label><br />
                        <label className={styles.rComment}>Comentário do User 1</label>
                    </div>
                    <div className={styles.ratingCard}>
                        <label className={styles.rValue}>4/5 Recomendação</label><br />
                        <label className={styles.rUser}>[] User 1</label><br />
                        <label className={styles.rComment}>Comentário do User 1</label>
                    </div>
                    <div className={styles.ratingCard}>
                        <label className={styles.rValue}>4/5 Recomendação</label><br />
                        <label className={styles.rUser}>[] User 1</label><br />
                        <label className={styles.rComment}>Comentário do User 1</label>
                    </div>
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