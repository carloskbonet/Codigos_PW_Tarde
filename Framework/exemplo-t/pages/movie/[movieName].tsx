import { checkToken } from '@/services/tokenConfig';
import styles from '@/styles/movie.module.css'
import { getCookie } from 'cookies-next';
import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import Navbar from '@/components/Navbar';

export default function movie({ movieName }: any) {
    const router = useRouter();

    // Formulário de avaliação
    const [ratingForm, setRatingForm] = useState(
        {
            value: 0,
            comment: ''
        }
    );

    const [data, setData]: any = useState(undefined);


    function handleFormEdit(event: any, field: string) {
        setRatingForm({
            ...ratingForm,
            [field]: event.target.value
        });
        console.log(ratingForm)
    }

    async function formSubmit(e: any) {
        e.preventDefault();

        try {
            const cookieAuth = getCookie('authorization');

            const tokenInfos = checkToken(cookieAuth);


            const response = await fetch(`/api/action/rating/create`, {
                method: 'POST',
                headers: { 'Content-type': 'application/json' },
                body: JSON.stringify({
                    value: Number(ratingForm.value),
                    comment: ratingForm.comment,
                    email: tokenInfos.email,
                    movieName: movieName
                })
            });

            const responseJson = await response.json();

            alert(responseJson.message);
            router.reload();

        }
        catch (err) {
            console.log(err);
            alert(err);
        }
    }


    async function fetchData() {
        try {
            const response = await fetch(`/api/action/movie/find?name=` + movieName, {
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


    async function deleteComment(event:any) {
        event.preventDefault();
        try {

            const cookieAuth = getCookie('authorization');

            const tokenInfos = checkToken(cookieAuth);

            const response = await fetch(`/api/action/rating/delete`, {
                method: 'DELETE',
                headers: { 'Content-type' : 'application/json' },
                body: JSON.stringify({
                    email: tokenInfos.email,
                    moviename: movieName
                })
            });

            const responseJson = await response.json();

            alert(responseJson.message);
            router.reload();

        }
        catch (err) {
            console.log(err);
        }
    }




    return (
        <main id={styles.main} className="flex min-h-screen flex-col">
            <Navbar>
                
            </Navbar>

            {
                data != undefined ?

                    <div className={styles.page}>
                        <div className={styles.movie}>
                            <img src={data.imageURL} alt="" className={styles.img} />
                            <div className={styles.movieInfos}>
                                <h2>{data.name}</h2>
                                <p>{data.releaseDate}</p>
                                <p>{data.description}</p>
                                
                                {
                                    data.genres != undefined ?

                                    data.genres.map( (genre:any) => (
                                        <p>{genre.name}</p>
                                    ) )

                                    :

                                    <p>Sem Generos</p>

                                }

                            </div>
                        </div>

                        <iframe className={styles.video} height="350" src={`https://www.youtube.com/embed/` + data.videoURL}>
                        </iframe>

                        <form className={styles.formRating} onSubmit={formSubmit}>

                            <div className={styles.star_rating}>

                                <input className={styles.radio_hide} type="radio" id='star_5' name='stars' value='5' onChange={(e) => { handleFormEdit(e, 'value') }} />
                                <label className={styles.radio_star} htmlFor='star_5' ></label>

                                <input className={styles.radio_hide} type="radio" id='star_4' name='stars' value='4' onChange={(e) => { handleFormEdit(e, 'value') }} />
                                <label className={styles.radio_star} htmlFor='star_4' ></label>

                                <input className={styles.radio_hide} type="radio" id='star_3' name='stars' value='3' onChange={(e) => { handleFormEdit(e, 'value') }} />
                                <label className={styles.radio_star} htmlFor='star_3' ></label>

                                <input className={styles.radio_hide} type="radio" id='star_2' name='stars' value='2' onChange={(e) => { handleFormEdit(e, 'value') }} />
                                <label className={styles.radio_star} htmlFor='star_2' ></label>

                                <input className={styles.radio_hide} type="radio" id='star_1' name='stars' value='1' onChange={(e) => { handleFormEdit(e, 'value') }} />
                                <label className={styles.radio_star} htmlFor='star_1' ></label>


                            </div>


                            <textarea onChange={(e) => { handleFormEdit(e, 'comment') }} className={styles.comment} placeholder='Digite seu Comentário' ></textarea><br />
                            <input className={styles.submitBtn} type="submit" />
                            
                            
                            <br /><br />
                            <button onClick={deleteComment} className={styles.submitBtn}>Excluir Comentário</button>
                        </form>

                        <div className={styles.ratings}>

                            {

                                data.ratings.map((rating: any) => (

                                    <div className={styles.ratingCard}>
                                        <div className={styles.rInfos}>
                                            <label className={styles.rUser}> {rating.user.username} </label>
                                            <label className={styles.rValue}> {rating.value} /5 Recomendação</label><br />
                                        </div>
                                        <div className={styles.rComment}>
                                            <label>{rating.comment}</label>
                                        </div>
                                    </div>


                                ))


                            }

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