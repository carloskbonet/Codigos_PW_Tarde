import styles from '@/styles/movie.module.css'

export default function movie({ movieName }: any) {

    return (
        <main id={styles.main} className="flex min-h-screen flex-col">

            <div className={styles.page}>
                <div className={styles.movie}>
                    <img src="/card.jfif" alt="" className={styles.img} />
                    <div className={styles.movieInfos}>
                        <h2>Nome do Filme</h2>
                        <p>Data de Lançamento   </p>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                        <p>Generos</p>
                    </div>
                </div>

                <iframe className={styles.video} height="350" src="https://www.youtube.com/embed/tgbNymZ7vqY">
                </iframe>

                <div className="Avaliações">

                </div>
            </div>
        </main>
    );
}


export function getServerSideProps(context: any) {

    const { movieName } = context.query;

    return {
        props: { movieName }
    }
}